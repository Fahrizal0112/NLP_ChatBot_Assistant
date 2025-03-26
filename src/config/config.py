class ChatbotConfig:
    TRAINING_DATA_PATH = "src/data/training_data.json"
    RESPONSES_PATH = "src/data/responses.json"
    
    CONFIDENCE_THRESHOLD = 0.3
    
    SUPPORTED_INTENTS = [
        "greeting",
        "order_cake",
        "check_price",
        "check_availability",
        "goodbye"
    ]