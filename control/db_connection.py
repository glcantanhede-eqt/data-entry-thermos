import streamlit as st
from supabase import create_client, Client
from supabase.lib.client_options import ClientOptions


# Initialize connection.
@st.cache_resource
def init_connection():
    opts = ClientOptions().replace(schema="data_entry")
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key, options=opts)

# Perform query.
# Uses st.cache_resource to only rerun when the query changes or after 10 min.
@st.cache_resource(ttl=600)
def run_select(conn, _table_name, atributes):
    return conn.table(_table_name).select(atributes).execute()

# Perform insert.
@st.cache_resource(ttl=600)
def run_insert(conn, _table_name, values):
    return conn.table(_table_name).insert(values).execute()







