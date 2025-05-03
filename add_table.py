# ===== Import Library =====
# - Data
import pandas as pd
import psycopg2

# - Web Apps
import streamlit as st

# - Extras
import re

# ===== Load Secrets =====
uri = st.secrets['uri']

# ===== Set Title =====
st.title('Add Table')

# ===== Set Subheader =====
st.subheader('(•˕ •マ.ᐟ')

st.markdown('<hr>', unsafe_allow_html=True)

# ===== Set Paragraph =====
st.text('Sesuai nama, ini buat masukin datanya')

st.text(
    'Jadi tinggal siapin aja datanya di Excel, upload ke sini, kasih nama table, trus submit, dah deh auto jadi tablenya di db dan bisa diakses secara langsung!')

st.text('See the magic 🪄!')

# ===== Table Name Input =====
# - Fungsi untuk memvalidasi input
def validate_input(input_text):
    # Menggunakan regular expression untuk memeriksa apakah input hanya mengandung huruf dan _
    if re.match("^[a-zA-Z_]+$", input_text):
        return True
    return False


# - Fungsi untuk menentukan tipe data kolom berdasarkan dtypes pandas
def determine_column_type(dtype):
    if dtype == 'object':  # String type
        return "VARCHAR"
    elif dtype == 'float64':  # Floating point type
        return "FLOAT"
    elif dtype == 'int64':  # Integer type
        return "BIGINT"
    elif dtype == 'bool':  # Boolean type
        return "BOOLEAN"
    elif dtype == 'datetime64[ns]':  # Datetime type
        return "DATE"  # We'll handle the formatting separately
    else:
        return "VARCHAR"  # Default to VARCHAR if the type is unknown


# - Input dari pengguna
table_input = st.text_input("Masukkan nama table (hanya huruf dan underscore):")

# - XLSX Input
data = st.file_uploader('Masukkan data Excel', type=['xlsx'])

# ===== Validasi Submit =====
if st.button('Submit'):
    if not table_input or not data:
        st.error("Isi dulu bjir form-nya! 😡")
    else:
        if validate_input(table_input):
            st.success("Input valid!")
            df = pd.read_excel(data)
            # Menjamin format tanggal konsisten dalam bentuk Short Date (DD/MM/YYYY)
            for col in df.select_dtypes(include=['datetime64[ns]']).columns:
                df[col] = df[col].dt.strftime('%d/%m/%Y')  # Format ulang ke DD/MM/YYYY
                
            st.write(f'Table Name: {table_input}')
            st.dataframe(df, use_container_width=True)

            # Create SQL Query for CREATE TABLE with dynamic column types based on dtype
            columns = []
            for col, dtype in df.dtypes.items():  # Using .dtypes to get column types
                col_type = determine_column_type(dtype)  # Determine column type based on dtype
                columns.append(f"{col} {col_type}")

            # Modify CREATE TABLE query to use DROP TABLE if exists
            drop_table_query = f"DROP TABLE IF EXISTS {table_input};"
            create_table_query = f"CREATE TABLE {table_input} ({', '.join(columns)});"

            # Display CREATE TABLE query
            st.code(drop_table_query, language='sql')
            st.code(create_table_query, language='sql')

            # Replace NaN with None (which will translate to NULL in SQL)
            df = df.where(pd.notnull(df), None)
            
            # Create SQL Query for INSERT INTO
            insert_queries = []
            for _, row in df.iterrows():
                row_values = []
                for value in row:
                    if value is None:
                        row_values.append("NULL")
                    elif isinstance(value, str):
                        # Escape single quotes to prevent SQL injection or syntax errors
                        value_escaped = value.replace("'", "''")
                        row_values.append(f"'{value_escaped}'")
                    else:
                        row_values.append(str(value))
                
                values = ', '.join(row_values)
                insert_query = f"INSERT INTO {table_input} ({', '.join(df.columns)}) VALUES ({values});"
                insert_queries.append(insert_query)

            # Tampilkan query insert
            for insert_query in insert_queries:
                st.code(insert_query, language='sql')

            # ===== Menjalankan Query ke PostgreSQL =====
            try:
                # Koneksi ke database PostgreSQL
                conn = psycopg2.connect(
                    uri
                )
                cur = conn.cursor()

                # Menjalankan DROP TABLE (untuk menghapus tabel jika ada)
                cur.execute(drop_table_query)

                # Menjalankan CREATE TABLE
                cur.execute(create_table_query)

                # Menjalankan semua query INSERT INTO
                for insert_query in insert_queries:
                    cur.execute(insert_query)

                # Commit transaksi
                conn.commit()

                # Tampilkan pesan sukses
                st.success("Table and data have been successfully inserted into the database!")

            except Exception as e:
                # Menangani error jika terjadi
                st.error(f"Error: {e}")
                conn.rollback()

            finally:
                # Menutup koneksi dan cursor
                cur.close()
                conn.close()

        else:
            st.error("Teks hanya boleh mengandung huruf dan underscore (_). Silakan coba lagi.")
