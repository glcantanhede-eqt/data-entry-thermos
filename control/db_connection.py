import streamlit as st
from supabase import create_client, Client
from supabase.lib.client_options import ClientOptions
import asyncio


# Initialize connection.
@st.cache_resource(ttl=600)
def init_connection():
    opts = ClientOptions().replace(schema="data_entry")
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key, options=opts)


async def log_in(_conn, credentials):
    response = await _conn.auth.sign_in_with_password(credentials)
    asyncio.sleep(3)
    return response

# Perform query.
# Uses st.cache_resource to only rerun when the query changes or after 10 min.

def run_select(_conn, _table_name, atributes):
    return _conn.table(_table_name).select(atributes).execute()

# Perform insert.
def run_insert(_conn, _table_name, values):
    return _conn.table(_table_name).insert(values, returning='minimal').execute()







