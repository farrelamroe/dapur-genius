# 🍳 DapurGenius AI - Zero Waste Cooking Assistant

**DapurGenius** adalah chatbot asisten masak berbasis AI yang dirancang untuk membantu pengguna mengurangi limbah makanan (*zero waste*). Chatbot ini membantu pengguna menemukan ide resep kreatif berdasarkan bahan-bahan sisa yang tersedia di kulkas mereka.

Dibangun menggunakan **Streamlit**, **LangChain**, dan ditenagai oleh **Groq (Llama 3.3)** untuk performa inferensi yang super cepat dan akurat.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![Groq](https://img.shields.io/badge/AI-Groq_Llama3-orange)

## ✨ Fitur Utama

* **🔍 Smart Recipe Generation:** Input bahan apa saja (misal: "tahu, sisa ayam, wortel"), dan AI akan membuatkan resep lengkap.
* **⚙️ Parameter Terkustomisasi:**
    * **Tingkat Kesulitan:** Pemula, Menengah, atau MasterChef.
    * **Waktu Masak:** Sesuaikan dengan ketersediaan waktumu (10 - 120 menit).
* **🧠 Contextual Memory:** Chatbot mengingat percakapan sebelumnya, sehingga kamu bisa meminta revisi resep (misal: "Ganti cabainya jadi merica aja").
* **💬 Persona Unik:** Gaya bahasa chef yang santai, humoris, dan suportif.
* **⚡ Powered by Groq:** Menggunakan model `llama-3.3-70b-versatile` yang sangat cepat dan gratis.

## 🛠️ Tech Stack

* **Bahasa Pemrograman:** Python
* **Framework UI:** Streamlit
* **Orchestrator:** LangChain (Community & Core)
* **LLM Provider:** Groq API (Llama 3.3)
* **Environment Management:** python-dotenv

## 🚀 Cara Menjalankan Project (Instalasi)

Ikuti langkah-langkah ini untuk menjalankan DapurGenius di komputer lokal kamu.

### 1. Clone Repository
```bash
git clone [https://github.com/username-anda/DapurGenius.git](https://github.com/username-anda/DapurGenius.git)
cd DapurGenius