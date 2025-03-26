from models.intent_model import IntentClassifier
from utils.response_generator import ResponseGenerator
import json
from config.config import ChatbotConfig

class CakeShopChatbot:
    def __init__(self):
        self.config = ChatbotConfig()
    
        try:
            with open(self.config.TRAINING_DATA_PATH, 'r') as f:
                self.training_data = json.load(f)
        except Exception as e:
            raise
        
        self.intent_classifier = IntentClassifier()
        self.intent_classifier.train(self.training_data)
        
        self.response_generator = ResponseGenerator(self.training_data)
        
        self.conversation_state = {
            "current_order": {},
            "ordering_stage": None
        }
        
    def process_message(self, message: str) -> str:
        
        intent, confidence = self.intent_classifier.predict(message)
        
        if confidence < self.config.CONFIDENCE_THRESHOLD:
            return "Maaf, saya tidak yakin dengan maksud Anda. Bisa tolong diperjelas?"
        
        entities = self.intent_classifier.extract_entities(message)
        
        if intent == "order_cake":
            self.conversation_state["ordering_stage"] = "flavor"
            self.conversation_state["current_order"].update(entities)
        
        response = self.response_generator.generate_response(intent, entities)
        
        return response

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