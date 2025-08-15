# 🚀 Beginner ETL Pipeline: Crypto Market Data

## 📌 Overview
This project demonstrates a **beginner-friendly ETL (Extract, Transform, Load) pipeline** for fetching cryptocurrency market data from the **CoinGecko API**, transforming it into a simplified dataset, and loading it into a **PostgreSQL** database.

The aim is to simulate a real-world **Data Engineering workflow** and practice:
- API data extraction
- Data transformation with Pandas
- Data loading into relational databases
- Logging for monitoring ETL jobs

---

## 🛠 Tech Stack
- **Python** (pandas, requests, sqlalchemy, psycopg2)
- **PostgreSQL**
- **CoinGecko API**
- **Logging Module**

---

## ⚙️ Architecture
```plaintext
           +-----------------+
           |  CoinGecko API  |
           +--------+--------+
                    |
                    ▼
             [Extract.py]
                    |
                    ▼
             [Transform.py]
                    |
                    ▼
               [Load.py]
                    |
                    ▼
          PostgreSQL (crypto_simple table)
