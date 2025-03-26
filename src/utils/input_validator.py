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

    @staticmethod
    def validate_order_data(order_data: dict) -> tuple[bool, str]:
        if not order_data.get("customer_name"):
            return False, "Mohon masukkan nama Anda"
            
        if not order_data.get("flavor"):
            return False, "Mohon pilih rasa kue (coklat/vanilla/strawberry)"
            
        if not order_data.get("size"):
            return False, "Mohon pilih ukuran kue (S/M/L)"
            
        if not order_data.get("quantity") or order_data["quantity"] < 1:
            return False, "Mohon masukkan jumlah pesanan yang valid"
            
        if not order_data.get("address"):
            return False, "Mohon masukkan alamat pengiriman"
            
        return True, "Data pesanan lengkap" 