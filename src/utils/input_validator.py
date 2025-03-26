class InputValidator:
    @staticmethod
    def validate_quantity(quantity: int) -> bool:
        return isinstance(quantity, int) and 0 < quantity <= 10
        
    @staticmethod
    def validate_size(size: str) -> bool:
        valid_sizes = ["small", "medium", "large"]
        return size.lower() in valid_sizes
        
    @staticmethod
    def validate_flavor(flavor: str) -> bool:
        valid_flavors = ["chocolate", "vanilla", "strawberry"]
        return flavor.lower() in valid_flavors 