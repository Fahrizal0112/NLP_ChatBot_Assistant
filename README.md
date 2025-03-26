# Chatbot Toko Kue

Chatbot pintar untuk pemesanan kue yang dibangun dengan Python. Menggunakan NLP (Natural Language Processing) untuk memahami permintaan pelanggan dan memproses pesanan kue.

## Fitur

- 🤖 Natural Language Processing untuk memahami input pengguna
- 🍰 Pemesanan kue dengan berbagai rasa dan ukuran
- 💰 Informasi harga otomatis
- 🚚 Informasi pengiriman
- 💳 Informasi metode pembayaran
- ✨ Dukungan untuk kue custom
- 📝 Penyimpanan pesanan di database PostgreSQL

## Rasa dan Ukuran Kue

### Rasa
- Coklat
- Vanilla
- Strawberry

### Ukuran
- S (15cm) - Rp150.000
- M (20cm) - Rp250.000
- L (25cm) - Rp350.000

## Persyaratan Sistem

```bash
Python 3.8+
PostgreSQL 12+
```

## Instalasi

1. Clone repository ini
```bash
git clone <repository-url>
cd chatbot-toko-kue
```

2. Buat virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# atau
.venv\Scripts\activate     # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Setup database
```bash
# Buat database PostgreSQL
createdb cake_shop_db

# Setup environment variables
cp .env.example .env
# Edit .env dengan kredensial database Anda
```

5. Jalankan aplikasi
```bash
python src/run.py
```

## Struktur Proyek
src/
├── config/
│ ├── config.py # Konfigurasi aplikasi
│ └── database.py # Konfigurasi database
├── data/
│ └── training_data.json # Data training untuk NLP
├── models/
│ ├── database.py # Model database
│ └── intent_model.py # Model NLP
├── utils/
│ ├── input_validator.py # Validasi input
│ └── response_generator.py # Generator respons
├── main.py # Logic utama aplikasi
└── run.py # Entry point aplikasi


## Penggunaan

Chatbot dapat memahami berbagai jenis pertanyaan dan permintaan, termasuk:

1. Sapaan
User: "Halo"
Bot: "Halo! Selamat datang di Toko Kue kami!"

2. Pemesanan
User: "Saya mau pesan kue"
Bot: "Tentu! Kue apa yang ingin Anda pesan?"

3. Informasi Harga
User: "Berapa harga kue coklat ukuran M?"
Bot: "Harga kue coklat ukuran M adalah Rp250.000"

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

# Database Configuration
DB_USER=postgres
DB_PASS=your_password_here
DB_HOST=localhost
DB_NAME=cake_shop_db
DB_PORT=5432

# Application Configuration
CONFIDENCE_THRESHOLD=0.3

nltk==3.8.1
spacy==3.7.2
python-dotenv==1.0.0
numpy==1.24.3
fuzzywuzzy==0.18.0
python-Levenshtein==0.12.2
sqlalchemy==1.4.41
psycopg2-binary==2.9.3

MIT License

Copyright (c) 2025 Muchammad Fahrizal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.