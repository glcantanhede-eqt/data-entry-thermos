import streamlit as st
from supabase import create_client, Client


# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_select(_conn, table_name, atributes):
    return _conn.table(_table_name).select(atributes).execute()


@st.cache_data(ttl=600)
def run_insert(_conn, _table_name, values):
    return _conn.table(_table_name).insert(values).execute()








