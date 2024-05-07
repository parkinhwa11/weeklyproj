import streamlit as st
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    database = 'weekproject',
    user = 'weekproject',
    password = '1234'
)

if conn.is_connected():
    db_info = conn.get_server_info()
    st.write('server_version :',db_info)

cur = conn.cursor()
@st.cache_data
def make_df(region):
    cur.execute(f'SELECT * FROM {region};')
    records = cur.fetchall()
    st.markdown(region)
    return pd.DataFrame(records, columns = ['id','spot','link'])
def to_link(region):
    df = make_df(region)
    st.data_editor(
        df,
        column_config={
            "link": st.column_config.LinkColumn(
                "site",
                help="You can find useful information through this site!",
            )
        },
        hide_index=True,
    )
to_link('gangwon')
to_link('gyeonggi')
to_link('gyeongnam')
to_link('gyeongbuk')
to_link('daegu')
to_link('gwangju')
to_link('daejeon')
to_link('busan')
to_link('seoul')
to_link('sejong')
to_link('incheon')
to_link('jeonnam')
to_link('jeonbuk')
to_link('jeju')
to_link('chungnam')
to_link('chungbuk')
to_link('ulsan')

