# ===== Import Library =====
# - Web Apps
import streamlit as st

# ===== Set Title =====
st.title('Python Support')

# ===== Set Subheader =====
st.subheader('⸜(｡˃ ᵕ ˂ )⸝♡')

st.markdown('<hr>', unsafe_allow_html=True)

# ===== Set Paragraph =====
st.text('Barangkali lebih nyaman lewat Python')
st.text('Connectnya ikutin cara di bawah aja, abis itu tinggal query biasa')
st.text('Fighting ⋆｡‧˚ʚ🧸ɞ˚‧｡⋆!')

# ===== Code Embed =====
st.code('''
!pip install psycopg2-binary

import psycopg2
import pandas as pd

url = "xx"

# Connection string
conn = psycopg2.connect(url)

# Query untuk mengambil data
query = "SELECT * FROM table_name"  # Ganti 'table_name' dengan nama tabel yang ingin ditampilkan

# Mengambil data ke dalam DataFrame
df = pd.read_sql_query(query, conn)

# Tutup koneksi
conn.close()
''', language='python')
