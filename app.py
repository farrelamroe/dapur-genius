import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

st.set_page_config(page_title="DapurGenius AI", page_icon="🍳")

st.title("🍳 DapurGenius: Masak Enak (Auto-Login)")
st.markdown("""
*Halo! Saya Chef Genius. Sebutkan bahan-bahan sisa di kulkasmu, 
dan saya akan sulap menjadi resep istimewa!*
""")

with st.sidebar:
    st.header("⚙️ Konfigurasi Dapur")
    # Input API Key DIHAPUS karena sudah pakai .env
    difficulty = st.selectbox("Tingkat Kesulitan", [
                              "Pemula (Sat-set)", "Menengah", "MasterChef"])
    waktu_masak = st.slider("Waktu Memasak (menit)", 10, 120, 30)

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error(
        "⚠️ API Key tidak ditemukan! Pastikan file .env sudah dibuat dan berisi GROQ_API_KEY.")
    st.stop() 


if "messages" not in st.session_state:
    st.session_state.messages = []

try:
    # Inisialisasi Model Groq
    llm = ChatGroq(
        temperature=0.7,
        model_name="llama-3.3-70b-versatile",
        api_key=api_key
    )

    # Definisi System Prompt (Persona)
    system_instruction = f"""
    Anda adalah DapurGenius, chef asisten yang ramah, lucu, dan kreatif.
    Tugas utama: Membuat resep berdasarkan bahan yang diinput user.
    Aturan:
    1. Gunakan bahasa Indonesia yang gaul dan santai.
    2. Resep harus sesuai tingkat kesulitan: {difficulty}.
    3. Estimasi waktu masak maksimal: {waktu_masak} menit.
    4. Berikan tips agar bahan tidak terbuang.
    5. Format: Nama Masakan, Bahan, Cara, dan 'Tips Chef'.
    """

    # Menampilkan chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input User
    if prompt := st.chat_input("Punya bahan apa hari ini?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            messages = [SystemMessage(content=system_instruction)]
            for msg in st.session_state.messages[-5:]:
                if msg["role"] == "user":
                    messages.append(HumanMessage(content=msg["content"]))

            response = llm.invoke(messages)
            st.markdown(response.content)
            st.session_state.messages.append(
                {"role": "assistant", "content": response.content})

except Exception as e:
    st.error(f"Terjadi kesalahan koneksi: {e}")
