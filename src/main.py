from models.intent_model import IntentClassifier
from utils.response_generator import ResponseGenerator
import json
from config.config import ChatbotConfig
from models.database import Order, init_db

class CakeShopChatbot:
    def __init__(self):
        self.config = ChatbotConfig()
        
        with open(self.config.TRAINING_DATA_PATH, 'r') as f:
            self.training_data = json.load(f)
            
        self.intent_classifier = IntentClassifier()
        self.intent_classifier.train(self.training_data)
        
        self.response_generator = ResponseGenerator(self.training_data)
        
        self.Session = init_db()
        if not self.Session:
            print("Warning: Running without database connection")
        
        self.conversation_state = {
            "current_order": {
                "customer_name": None,
                "flavor": None,
                "size": None,
                "quantity": 1,
                "address": None
            },
            "ordering_stage": None
        }
        
    def process_message(self, message: str) -> str:
        intent, confidence = self.intent_classifier.predict(message)
        entities = self.intent_classifier.extract_entities(message)
        
        if intent == "order_cake":
            self.conversation_state["ordering_stage"] = "name"
            return "Mohon masukkan nama Anda:"
            
        if self.conversation_state["ordering_stage"] == "name":
            self.conversation_state["current_order"]["customer_name"] = message
            self.conversation_state["ordering_stage"] = "flavor"
            return "Silakan pilih rasa kue (coklat/vanilla/strawberry):"
            
        elif self.conversation_state["ordering_stage"] == "flavor":
            if entities.get("flavor"):
                self.conversation_state["current_order"]["flavor"] = entities["flavor"]
                self.conversation_state["ordering_stage"] = "size"
                return "Pilih ukuran kue (S/M/L):"
                
        elif self.conversation_state["ordering_stage"] == "size":
            if entities.get("size"):
                self.conversation_state["current_order"]["size"] = entities["size"]
                self.conversation_state["ordering_stage"] = "quantity"
                return "Berapa jumlah kue yang ingin dipesan?"
                
        elif self.conversation_state["ordering_stage"] == "quantity":
            try:
                quantity = int(message)
                self.conversation_state["current_order"]["quantity"] = quantity
                self.conversation_state["ordering_stage"] = "address"
                return "Mohon masukkan alamat pengiriman:"
            except ValueError:
                return "Mohon masukkan jumlah dalam angka"
                
        elif self.conversation_state["ordering_stage"] == "address":
            self.conversation_state["current_order"]["address"] = message
            self.conversation_state["ordering_stage"] = "confirmation"
            return self._generate_order_summary()
            
        elif self.conversation_state["ordering_stage"] == "confirmation":
            if intent == "confirmation":
                return self._save_order()
            else:
                return "Mohon konfirmasi pesanan Anda (ketik 'setuju' untuk konfirmasi)"
        
        return self.response_generator.generate_response(intent, entities)
    
    def _generate_order_summary(self) -> str:
        order = self.conversation_state["current_order"]
        return f"""
Mohon konfirmasi pesanan Anda:
Nama: {order['customer_name']}
Rasa: {order['flavor']}
Ukuran: {order['size']}
Jumlah: {order['quantity']}
Alamat: {order['address']}

Total Harga: Rp{self._calculate_price():,}

Ketik 'setuju' untuk konfirmasi pesanan
"""
    
    def _calculate_price(self) -> float:
        price_list = {
            'small': 150000,
            'medium': 250000, 
            'large': 350000,
            's': 150000,
            'm': 250000,
            'l': 350000
        }
        order = self.conversation_state["current_order"]
        size = order.get('size', '').lower()
        quantity = order.get('quantity', 0)
        
        print(f"DEBUG - Size: {size}, Quantity: {quantity}")
        
        base_price = price_list.get(size, 0)
        total_price = base_price * quantity
        
        print(f"DEBUG - Base price: {base_price}, Total: {total_price}")
        
        return total_price
    
    def _save_order(self) -> str:
        if self.Session is None:
            return "Maaf, tidak bisa menyimpan pesanan karena database tidak terkoneksi. Pesanan Anda: \n" + self._generate_order_summary()
            
        session = None
        try:
            session = self.Session()
            
            order_data = self.conversation_state["current_order"]
            new_order = Order(
                customer_name=order_data["customer_name"],
                flavor=order_data["flavor"],
                size=order_data["size"],
                quantity=order_data["quantity"],
                address=order_data["address"],
                price=self._calculate_price(),
                status="pending"
            )
            
            session.add(new_order)
            session.commit()
            
            self.conversation_state = {
                "current_order": {},
                "ordering_stage": None
            }
            
            return f"Pesanan berhasil disimpan dengan ID: {new_order.id}. Terima kasih telah memesan!"
            
        except Exception as e:
            print(f"Error saving order: {str(e)}")
            if session:
                session.rollback()
            return "Maaf, terjadi kesalahan dalam menyimpan pesanan. Mohon coba lagi."
            
        finally:
            if session:
                session.close()

def main():
    chatbot = CakeShopChatbot()
    
    print("Cake Shop Chatbot siap melayani (ketik 'keluar' untuk mengakhiri)")
    
    while True:
        user_input = input("Anda: ")
        
        if user_input.lower() == "keluar":
            print("Terima kasih telah menggunakan layanan kami!")
            break
            
        response = chatbot.process_message(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()