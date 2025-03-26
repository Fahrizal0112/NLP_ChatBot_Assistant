
## Intent yang Didukung

- greeting: Sapaan
- order_cake: Pemesanan kue
- cake_flavor: Pemilihan rasa
- cake_size: Pemilihan ukuran
- cake_details: Informasi detail kue
- price_inquiry: Pertanyaan harga
- payment_method: Metode pembayaran
- delivery_info: Informasi pengiriman
- custom_cake: Kue custom

## Pengembangan

Untuk menambah kemampuan chatbot, Anda dapat:

1. Menambah patterns di `training_data.json`
2. Menyesuaikan threshold confidence di `config.py`
3. Menambah entity recognition di `intent_model.py`
4. Mengustomisasi respons di `response_generator.py`

## Database Schema

```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    flavor VARCHAR(50) NOT NULL,
    size VARCHAR(10) NOT NULL,
    quantity INTEGER NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    address TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Kontribusi

Silakan berkontribusi dengan membuat pull request atau melaporkan issues.

## Lisensi

[MIT License](LICENSE)