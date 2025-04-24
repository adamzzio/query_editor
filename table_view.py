# ===== Import Library =====
# - Data
import pandas as pd
import psycopg2

# - Web Apps
import streamlit as st

# ===== Load Secrets =====
uri = st.secrets['uri']

# ===== Set Title =====
st.title('Table View')

# ===== Set Subheader =====
st.subheader('View your data!')

st.markdown('<hr>', unsafe_allow_html=True)

# ===== Set Paragraph =====
st.text('Kalo tadi insert, nah ini view')

st.text(
    'Dah tinggal pilih aja table mana yang mau di-view')

st.text('See the magic 🪄!')


# ===== Fungsi untuk mengambil nama-nama tabel dari database =====
def get_table_names():
    try:
        # Koneksi ke database PostgreSQL
        conn = psycopg2.connect(
            uri
        )
        cur = conn.cursor()

        # Query untuk mengambil nama-nama tabel di public schema
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")

        # Ambil hasil query
        tables = cur.fetchall()

        # Hanya mengambil nama tabel dari hasil query
        table_names = [table[0] for table in tables]

        # Menutup koneksi
        cur.close()
        conn.close()

        return table_names

    except Exception as e:
        st.error(f"Error: {e}")
        return []


# ===== Tampilkan Multiselect untuk Memilih Tabel =====
table_names = get_table_names()

if table_names:
    table_view = st.multiselect(
        "Pilih tabel untuk dilihat:",
        options=table_names,
        default=None
    )

    # Menambahkan tombol Submit
    if st.button('Submit'):
        # Jika ada tabel yang dipilih, tampilkan data
        if table_view:
            for table_name in table_view:
                try:
                    # Koneksi kembali untuk mengambil data dari tabel yang dipilih
                    conn = psycopg2.connect(
                        uri
                    )
                    query = f"SELECT * FROM {table_name};"
                    df = pd.read_sql(query, conn)
                    # Tampilkan keterangan tabel dan data
                    st.write(f"**Table name : {table_name}**")
                    st.dataframe(df, use_container_width=True)
                    conn.close()
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.text("Silakan pilih tabel untuk melihat data.")
else:
    st.text("Tidak ada tabel yang ditemukan.")
