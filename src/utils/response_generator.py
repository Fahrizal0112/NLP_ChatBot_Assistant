import random
from typing import Dict, List

class ResponseGenerator:
    def __init__(self, responses_data: Dict):
        self.responses = responses_data
        self.fallback_responses = [
            "Maaf, saya kurang mengerti. Bisa dijelaskan dengan cara lain?",
            "Mohon maaf, bisa diulangi dengan kata-kata yang berbeda?",
            "Saya masih belajar. Bisa tolong diperjelas maksudnya?"
        ]
        
    def generate_response(self, intent: str, entities: Dict = None) -> str:
        if not intent or intent not in [i["tag"] for i in self.responses["intents"]]:
            return random.choice(self.fallback_responses)
        
        matching_intent = None
        for intent_data in self.responses["intents"]:
            if intent_data["tag"] == intent:
                matching_intent = intent_data
                break
        
        if not matching_intent:
            return "Maaf, saya tidak mengerti permintaan Anda."
        
        response = random.choice(matching_intent["responses"])
        return response