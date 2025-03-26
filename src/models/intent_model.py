import spacy
import numpy as np
from typing import dict, list, Tuple

class IntentClassifier:
    def __init__(sekf):
        self.nlp = spacy.load("id_core_news_lg")
        self.intents = {}

    def train(self, training_data: Dict):
        for intent in training_data["intents"]:
            self.intents[intent["tag"]] = {
                "patterns": [self.nlp(pattern) for pattern in intent["patterns"]],
                "responses": intent["responses"]
            }

    def predict(self, text: str) -> Tuple[str, float]:
        text_vector = self.nlp(text)
        
        best_score = 0
        best_intent = None
        
        for intent_name, intent_data in self.intents.items():
            for pattern in intent_data["patterns"]:
                similarity = text_vector.similarity(pattern)
                if similarity > best_score:
                    best_score = similarity
                    best_intent = intent_name
                    
        return best_intent, best_score