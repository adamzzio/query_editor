# ===== Import Library =====
# - Data
import pandas as pd
import psycopg2

# - Web Apps
import streamlit as st

# ===== Load Secrets =====
uri = st.secrets['uri']

# ===== Set Title =====
st.title('Query Editor')

# ===== Set Subheader =====
st.subheader('⎛⎝ ≽  >  ⩊   < ≼ ⎠⎞')

st.markdown('<hr>', unsafe_allow_html=True)

# ===== Set Paragraph =====
st.text('Query aja langsung, biar ga ribet lu-nya')

st.text('Langsung tulis SQL-nya aja')

st.text('See the magic 🪄!')

# ===== Input untuk menulis query SQL =====
query_input = st.text_area("Tulis query SQL-mu di sini:", height=200)

# ===== Tombol Submit untuk menjalankan query =====
if st.button('Submit'):
    if query_input.strip():
        try:
            # Koneksi ke database PostgreSQL
            conn = psycopg2.connect(
                uri
            )
            # Menjalankan query yang dimasukkan oleh pengguna
            df = pd.read_sql(query_input, conn)

            # Tampilkan hasil query dalam bentuk tabel
            st.write("Query Hasil:")
            st.dataframe(df, use_container_width=True)

            # Menutup koneksi
            conn.close()

        except Exception as e:
            # Menangani error jika query gagal
            st.error("Query error, silakan cek table view dulu")
            st.error(f"Error: {e}")
    else:
        st.error("Silakan masukkan query SQL terlebih dahulu.")
