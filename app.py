# ===== Import Library =====
import streamlit as st

# ===== Set Page Config =====
st.set_page_config(page_title="SQL Editor", page_icon=":bar_chart:", layout="wide")

# ===== Set Page =====
dashboard_page = st.Page("dashboard.py", title="Dashboard", icon=":material/query_stats:")
add_table_page = st.Page("add_table.py", title="Add Table", icon=":material/playlist_add:")
table_view_page = st.Page("table_view.py", title="Table View", icon=":material/table:")
query_editor_page = st.Page("query_editor.py", title="Query Editor", icon=":material/edit_note:")

# ===== Set Navigation =====
pg = st.navigation([dashboard_page, add_table_page,
                    table_view_page, query_editor_page])
pg.run()