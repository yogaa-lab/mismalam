import streamlit as st

# Mengatur judul tab browser
st.set_page_config(
    page_title="Aplikasi Pertamaku",
    page_icon="✨"
)

# Menampilkan judul dan teks di web
st.title("Aplikasi Streamlit Pertamaku!")
st.write(
    "Halo dunia! Jika kamu bisa melihat halaman ini, "
    "berarti kamu sudah **berhasil** meng-upload dan "
    "mendeploy aplikasi Streamlit dari GitHub."
)

# Garis pembatas
st.divider()

# Input sederhana
nama = st.text_input("Siapa namamu?")

# Tombol interaktif
if st.button("Klik Saya!"):
    if nama:
        st.success(
            f"Halo, {nama}! Selamat belajar Streamlit. Kamu hebat!"
        )
        st.balloons()  # Memunculkan animasi balon
    else:
        st.warning("Isi namamu dulu di kotak atas ya!")