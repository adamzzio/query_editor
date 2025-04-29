# ===== Import Library =====
# - Web Apps
import streamlit as st

# ===== Set Title =====
st.title('Notes')

# ===== Set Subheader =====
st.subheader('/ᐠ ˵> ˕ <˵マ')

st.markdown('<hr>', unsafe_allow_html=True)

# ===== Set Paragraph =====
st.text('Summary Notes')
st.text('Biar ga pusing pindah2 tab/halaman')
st.text('Lu pasti bisa grei, asli! ⋆｡‧˚ʚ🧸ɞ˚‧｡⋆!')

# ===== Code Embed =====
with st.expander('SELECT'):
    st.write('Pake select buat ambil kolom yang ingin dipake')
    st.code('''
    SELECT * 
    FROM USERS
    ''', language='sql')

with st.expander('ALIAS'):
    st.write('Gunain alias buat ngasih nama kolom/table, better digunain kalo namanya kepanjangan')
    st.code('''
    SELECT SUM(AMOUNT) AS TOTAL_REVENUE 
    FROM USERS
    ''', language='sql')

with st.expander('DISTINCT'):
    st.write('DISTINCT dipake buat nyari unique values ya, misal konteks shipping, Gee pengen tahu destinasinya kemana aja sih, bisa pake ini')
    st.code('''
    SELECT DISTINCT(DESTINATION_CITY) AS DEST_CITY 
    FROM SHIPMENT
    ''', language='sql')

with st.expander('WHERE'):
    st.write('WHERE dipake buat filter data KHUSUS buat data NON-AGREGAT ya!!!')
    st.code('''
    SELECT * 
    FROM PAYMENTS
    WHERE STATUS = 'Paid'
    ''', language='sql')

with st.expander('LIKE'):
    st.write('Fungsi LIKE sama kek fungsi RegEx yaa kalo di Python')
    st.write('% ini MULTI-character, kalo _ ini SINGLE-character')
    st.write('Cari user dengan awalan nama Adam')
    st.code('''
    SELECT * 
    FROM USERS
    WHERE NAME LIKE "Adam%"
    ''', language='sql')

with st.expander('IN'):
    st.write('IN berguna kek WHERE tapi filternya lebih dari 1')
    st.write('Misal nyari yang destinasi shipping di Jawa, kan provinsinya banyak tuh')
    st.code('''
    SELECT * 
    FROM SHIPMENT
    WHERE DESTINATION_PROVINCE IN ("Jawa Timur", "Jawa Tengah", "Jawa Barat")
    ''', language='sql')

with st.expander('NOT'):
    st.write('NOT berguna kek WHERE di mana dia berfungsi sebagai negasi')
    st.write('Misal nyari yang destinasi shipping di Non-Jawa, tinggal di NOT in aja')
    st.code('''
    SELECT * 
    FROM SHIPMENT
    WHERE DESTINATION_PROVINCE NOT IN ("Jawa Timur", "Jawa Tengah", "Jawa Barat")
    ''', language='sql')

with st.expander('BETWEEN'):
    st.write('Kalo BETWEEN kepake misal filternya berupa RANGE')
    st.write('BETWEEN bisa digunakan baik untuk NUMERIC maupun DATE yaaa')
    st.code('''
    SELECT * 
    FROM PRODUCT
    WHERE PRICE BETWEEN 10000 AND 50000
    ''', language='sql')

    st.code('''
    SELECT * 
    FROM SHIPMENT
    WHERE CREATED_AT BETWEEN '01-01-2024' AND '31-12-2024'
    ''', language='sql')

with st.expander('AND OR'):
    st.write('Filter juga, pelengkap WHERE, in case kalo kondisinya lebih dari 1')
    st.write('Kalo AND kepake saat kondisi keduanya dibutuhkan, misal Status = Paid dan Pay_Method harus Gopay')
    st.code('''
        SELECT * 
        FROM PAYMENT
        WHERE STATUS = 'Paid' AND PAY_METHOD = 'Gopay'
        ''', language='sql')

    st.write('Kalo OR, filternya juga sama 2, tapi gapapa kalo misal yang terpenuhi cuma 1 doang, ga harus 2 kek AND')
    st.code('''
    SELECT * 
    FROM PAYMENT
    WHERE STATUS = 'Paid' OR PAY_METHOD = 'Gopay'
    ''', language='sql')

with st.expander('AGGREGATE'):
    st.write('Fungsi aggregate ada banyak ya, ada COUNT, SUM, MIN, MAX, AVG')
    st.code('''
    SELECT
        COUNT(ID) AS TOTAL_TRX,
        SUM(AMOUNT) AS TOTAL_AMOUNT,
        AVG(AMOUNT) AS AVG_AMOUNT,
        MIN(AMOUNT) AS MIN_AMOUNT,
        MAX(AMOUNT) MAS MAX_AMOUNT 
    FROM PAYMENTS
    ''', language='sql')

with st.expander('HAVING'):
    st.write('Berhubung masih di AGGREGATE, kita bahas HAVING.')
    st.write('HAVING sama kek WHERE tapi khusus buat data yang udah agregat')
    st.code('''
    SELECT
        COUNT(ID) AS TOTAL_TRX,
        SUM(AMOUNT) AS TOTAL_AMOUNT,
        AVG(AMOUNT) AS AVG_AMOUNT,
        MIN(AMOUNT) AS MIN_AMOUNT,
        MAX(AMOUNT) MAS MAX_AMOUNT 
    FROM PAYMENTS
    HAVING TOTAL_AMOUNT > 500000
    ''', language='sql')

with st.expander('GROUP BY'):
    st.write('GROUP BY jelas untuk grouping by dimension ya, misal group by user')
    st.write('GROUP BY ini sering digunakan setelah data di-aggregate')
    st.code('''
    SELECT
        COUNT(ID) AS TOTAL_TRX,
        SUM(AMOUNT) AS TOTAL_AMOUNT,
        AVG(AMOUNT) AS AVG_AMOUNT,
        MIN(AMOUNT) AS MIN_AMOUNT,
        MAX(AMOUNT) MAS MAX_AMOUNT 
    FROM PAYMENTS
    GROUP BY USER_ID
    ''', language='sql')

with st.expander('ORDER BY'):
    st.write('ORDER BY buat urutin data, defaultnya ASCENDING')
    st.write('Kalo ada GROUP BY, kepakenya abis GROUP BY yaa, jangan dibalik')
    st.code('''
    SELECT
        COUNT(ID) AS TOTAL_TRX,
        SUM(AMOUNT) AS TOTAL_AMOUNT,
        AVG(AMOUNT) AS AVG_AMOUNT,
        MIN(AMOUNT) AS MIN_AMOUNT,
        MAX(AMOUNT) MAS MAX_AMOUNT 
    FROM PAYMENTS
    GROUP BY USER_ID
    ORDER BY TOTAL_AMOUNT
    ''', language='sql')

    st.write('Kalo mau DESCENDING, tinggal tambahin DESC aja')
    st.code('''
    SELECT
        COUNT(ID) AS TOTAL_TRX,
        SUM(AMOUNT) AS TOTAL_AMOUNT,
        AVG(AMOUNT) AS AVG_AMOUNT,
        MIN(AMOUNT) AS MIN_AMOUNT,
        MAX(AMOUNT) MAS MAX_AMOUNT 
    FROM PAYMENTS
    GROUP BY USER_ID
    ORDER BY TOTAL_AMOUNT DESC
    ''', language='sql')

    st.write('Kalo mau MULTIPLE SORT, tinggal pake koma aja')
    st.code('''
    SELECT
        COUNT(ID) AS TOTAL_TRX,
        SUM(AMOUNT) AS TOTAL_AMOUNT,
        AVG(AMOUNT) AS AVG_AMOUNT,
        MIN(AMOUNT) AS MIN_AMOUNT,
        MAX(AMOUNT) MAS MAX_AMOUNT 
    FROM PAYMENTS
    GROUP BY USER_ID
    ORDER BY TOTAL_AMOUNT DESC, TOTAL_TRX
    ''', language='sql')

with st.expander('JOINS'):
    st.write('Dah ikutin table di bawah aja, cukup pahami betul2 aja usecasenya kapan pake INNER, kapan LEFT, dll')
    st.write('Syntax-nya pake yang bawah aja, lebih pasti')
    st.image('joins.png', use_container_width=True)

    # SQL Queries for different JOIN types
    inner_join = """
    SELECT u.ID, u.Name, p.PaymentDate, p.Amount
    FROM USERS u
    INNER JOIN PAYMENT p ON u.ID = p.USER_ID;
    """

    left_inclusive = """
    SELECT u.ID, u.Name, p.PaymentDate, p.Amount
    FROM USERS u
    LEFT JOIN PAYMENT p ON u.ID = p.USER_ID;
    """

    left_exclusive = """
    SELECT u.ID, u.Name
    FROM USERS u
    LEFT JOIN PAYMENT p ON u.ID = p.USER_ID
    WHERE p.USER_ID IS NULL;
    """

    right_inclusive = """
    SELECT u.ID, u.Name, p.PaymentDate, p.Amount
    FROM USERS u
    RIGHT JOIN PAYMENT p ON u.ID = p.USER_ID;
    """

    right_exclusive = """
    SELECT p.USER_ID, p.PaymentDate, p.Amount
    FROM PAYMENT p
    LEFT JOIN USERS u ON u.ID = p.USER_ID
    WHERE u.ID IS NULL;
    """

    full_outer_inclusive = """
    SELECT u.ID, u.Name, p.PaymentDate, p.Amount
    FROM USERS u
    FULL OUTER JOIN PAYMENT p ON u.ID = p.USER_ID;
    """

    full_outer_exclusive = """
    SELECT u.ID, u.Name
    FROM USERS u
    FULL OUTER JOIN PAYMENT p ON u.ID = p.USER_ID
    WHERE u.ID IS NULL
    UNION
    SELECT p.USER_ID, p.PaymentDate
    FROM PAYMENT p
    FULL OUTER JOIN USERS u ON u.ID = p.USER_ID
    WHERE p.USER_ID IS NULL;
    """

    # Display each SQL query using st.code
    st.write('Inner Join')
    st.code(inner_join, language="sql")
    st.write('Left Incluse Join')
    st.code(left_inclusive, language="sql")
    st.write('Left Exclusive Join')
    st.code(left_exclusive, language="sql")
    st.write('Right Inclusive Join')
    st.code(right_inclusive, language="sql")
    st.write('Right Exclusive Join')
    st.code(right_exclusive, language="sql")
    st.write('Full Outer Inclusive Join')
    st.code(full_outer_inclusive, language="sql")
    st.write('Full Outer Exclusive Join')
    st.code(full_outer_exclusive, language="sql")

with st.expander('UNION'):
    st.write('Kalo UNION, misal kedua table kolomnya sama dan ingin digabungin, berarti kan tinggal DITUMPUK, maka pake UNION')
    st.image('union.jpg')
    st.code('''
    SELECT ID, Name, Email
    FROM USERS_A
    UNION
    SELECT ID, Name, Email
    FROM USERS_B;
    ''', language='sql')

with st.expander('CASE'):
    st.write('Kalo CASE ini sama kek IF kalo di Python, misal total_trx < 10 low, 10-20 medium, >20 loyal, maka bisa pake CASE')
    st.write('Btw ga harus numerik ya, di kategorik juga bisa')
    st.code('''
    SELECT 
        USER_ID,
        COUNT(*) AS PaymentCount,
        CASE
            WHEN COUNT(*) < 10 THEN 'Low'
            WHEN COUNT(*) BETWEEN 10 AND 20 THEN 'Medium'
            WHEN COUNT(*) > 20 THEN 'Loyal'
            ELSE 'Unknown'  -- In case there are null or unexpected values
        END AS LoyaltyLevel
    FROM PAYMENT
    GROUP BY USER_ID;
    ''', language='sql')

with st.expander('VIEWS'):
    st.write('Cuma buat views atau table sementara aja, dipake ketika query cukup panjang dan backend ga ingin query terlalu berat')
    st.write('Penggunaan OR REPLACE sesuai kebutuhan aja, aku biasanya pake')
    st.code('''
    CREATE OR REPLACE VIEW LoyaltyLevelView AS
    SELECT 
        USER_ID,
        COUNT(*) AS PaymentCount,
        CASE
            WHEN COUNT(*) < 10 THEN 'Low'
            WHEN COUNT(*) BETWEEN 10 AND 20 THEN 'Medium'
            WHEN COUNT(*) > 20 THEN 'Loyal'
            ELSE 'Unknown'  -- In case there are null or unexpected values
        END AS LoyaltyLevel
    FROM PAYMENT
    GROUP BY USER_ID;
    ''', language='sql')