from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import numpy as np
from typing import Dict, List, Tuple

class IntentClassifier:
    def __init__(self):
        import nltk
        nltk.download('punkt')
        nltk.download('stopwords')
        
        factory = StemmerFactory()
        self.stemmer = factory.create_stemmer()
        self.intents = {}
        
    def preprocess_text(self, text: str) -> List[str]:
        tokens = word_tokenize(text.lower())
        tokens = [self.stemmer.stem(token) for token in tokens]
        return tokens
        
    def train(self, training_data: Dict):
        for intent in training_data["intents"]:
            self.intents[intent["tag"]] = {
                "patterns": [self.preprocess_text(pattern) 
                           for pattern in intent["patterns"]],
                "responses": intent["responses"]
            }

    def predict(self, text: str) -> Tuple[str, float]:
        text_tokens = self.preprocess_text(text)
        
        best_score = 0
        best_intent = None
        
        for intent_name, intent_data in self.intents.items():
            for pattern in intent_data["patterns"]:
                common_words = set(text_tokens) & set(pattern)
                score = len(common_words) / max(len(text_tokens), len(pattern))
                
                if score > best_score:
                    best_score = score
                    best_intent = intent_name
        
        return best_intent, best_score
        
    def _calculate_similarity(self, tokens1: List[str], tokens2: List[str]) -> float:
        common_words = set(tokens1) & set(tokens2)
        return len(common_words) / max(len(tokens1), len(tokens2))

    def extract_entities(self, text: str) -> Dict:
        tokens = self.preprocess_text(text)
        entities = {
            "size": None,
            "flavor": None,
            "quantity": None
        }
        
        size_patterns = ["kecil", "sedang", "besar", "s", "m", "l"]
        flavor_patterns = ["coklat", "vanilla", "strawberry"]
        
        for token in tokens:
            if token in flavor_patterns:
                entities["flavor"] = token
            if token in size_patterns:
                entities["size"] = token
            try:
                num = int(token)
                entities["quantity"] = str(num)
            except ValueError:
                continue
            
        return entities