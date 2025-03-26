import random
from typing import Dict, List

class ResponseGenerator:
    def __init__(self, responses_data: Dict):
        self.responses = responses_data
        
    def generate_response(self, intent: str, entities: List = None) -> str:
        if intent not in self.responses:
            return "Maaf, saya tidak mengerti permintaan Anda."
            
        possible_responses = self.responses[intent]["responses"]
        return random.choice(possible_responses)