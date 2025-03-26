import random
from typing import Dict, List

class ResponseGenerator:
    def __init__(self, responses_data: Dict):
        self.responses = responses_data
        
    def generate_response(self, intent: str, entities: Dict = None) -> str:
        
        matching_intent = None
        for intent_data in self.responses["intents"]:
            if intent_data["tag"] == intent:
                matching_intent = intent_data
                break
        
        if not matching_intent:
            return "Maaf, saya tidak mengerti permintaan Anda."
        
        response = random.choice(matching_intent["responses"])
        return response