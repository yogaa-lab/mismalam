import streamlit as st

# mengatur judul tab browser
 st.set_page_config(page_title="aplikasi pertamaku", page_icon="+")

 # menampilkan judul dan teks di web
 st.title("a plikasi streamlit pertamaku!")
st.write("halo dunia! jika kamu bisa melihat halaman ini, berarti kamu sudah **berhasil** meng-upload dan mendeploy aplikasi streamlit dari github.")

st.divider() # garis pembatas

 # input sederhana
  nama = st.text_input("siapa namamu?")

 # tombol interaktif
 if st.button("klik saya!"):
   if nama:
       st.succes(f"halo, {nama}! selamat belajar streamlit. kamu hebat!")
       st.ballons() # memunculkan animasi balon
   else:
       st.warning("isi namamu dulu di kotak atas ya!")