from models.intent_model import IntentClassifier
from utils.response_generator import ResponseGenerator
import json
from config.config import ChatbotConfig

class CakeShopChatbot:
    def __init__(self):
        self.config = ChatbotConfig()
        
        # Load training data
        with open(self.config.TRAINING_DATA_PATH, 'r') as f:
            self.training_data = json.load(f)
            
        # Initialize models
        self.intent_classifier = IntentClassifier()
        self.intent_classifier.train(self.training_data)
        
        # Initialize response generator
        self.response_generator = ResponseGenerator(self.training_data)
        
    def process_message(self, message: str) -> str:
        # Predict intent
        intent, confidence = self.intent_classifier.predict(message)
        
        # Check confidence threshold
        if confidence < self.config.CONFIDENCE_THRESHOLD:
            return "Maaf, saya tidak yakin dengan maksud Anda. Bisa tolong diperjelas?"
            
        # Generate response
        response = self.response_generator.generate_response(intent)
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