from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import numpy as np
from typing import Dict, List, Tuple
from fuzzywuzzy import fuzz

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
        text1 = " ".join(tokens1)
        text2 = " ".join(tokens2)
        
        ratio = fuzz.ratio(text1, text2) / 100
        partial_ratio = fuzz.partial_ratio(text1, text2) / 100
        token_sort_ratio = fuzz.token_sort_ratio(text1, text2) / 100
        
        return max(ratio, partial_ratio, token_sort_ratio)

    def extract_entities(self, text: str) -> Dict:
        tokens = self.preprocess_text(text)
        entities = {
            "size": None,
            "flavor": None,
            "quantity": None,
            "price_range": None
        }
        
        size_patterns = {
            "s": "small",
            "m": "medium",
            "l": "large",
            "kecil": "small",
            "sedang": "medium",
            "besar": "large"
        }
        
        flavor_patterns = {
            "coklat": "chocolate",
            "vanilla": "vanilla",
            "vanila": "vanilla",
            "stroberi": "strawberry",
            "strawberry": "strawberry"
        }
        
        words = text.lower().split()
        for i, word in enumerate(words):
            if word in flavor_patterns:
                entities["flavor"] = flavor_patterns[word]
            
            if word in size_patterns:
                entities["size"] = size_patterns[word]
            
            try:
                num = int(word)
                if num > 0:
                    entities["quantity"] = num
            except ValueError:
                numeric_words = {"satu": 1, "dua": 2, "tiga": 3, "empat": 4, "lima": 5}
                if word in numeric_words:
                    entities["quantity"] = numeric_words[word]
                
        return entities