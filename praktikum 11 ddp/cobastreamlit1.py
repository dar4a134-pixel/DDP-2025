import streamlit as st

st.title('Aplikasi Data Diri')
st.header('Biodata Pribadi') 

nama = st.text_input('Nama', max_chars=10)
st.write(f'Nama saya adalah {nama}')

with st.form("Biodata"):
        st.write("Masukan biodata anda")
        nama = st.text_input("Nama")
        email = st.text_input("Email")
        usia = st.number_input("Usia",min_value=0, max_value=100, step=1)
        
    
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(f'Nama saya adalah {nama}, email saya {email} dan usia saya {usia}')