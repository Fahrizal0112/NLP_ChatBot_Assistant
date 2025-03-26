from main import CakeShopChatbot

def main():
    # Inisialisasi chatbot
    chatbot = CakeShopChatbot()
    
    print("=== Selamat Datang di Toko Kue Chat Bot ===")
    print("Ketik 'keluar' untuk mengakhiri percakapan")
    
    while True:
        user_input = input("\nAnda: ")
        
        if user_input.lower() == 'keluar':
            print("Terima kasih telah menggunakan layanan kami!")
            break
            
        response = chatbot.process_message(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main() 