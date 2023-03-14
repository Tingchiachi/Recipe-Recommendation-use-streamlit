import sqlite3
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

conn = sqlite3.connect('Recipe.db')
taiwanese = pd.read_csv("C:/Users/USER/OneDrive/Documents/111-1/statistical consulting/final/台式1_1220.csv")
taiwanese.sort_values('Name', inplace=True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
cursor = conn.cursor()
taiwanese.to_sql('Taiwan_Recipe', conn, if_exists='replace', index=False)
conn.commit()

italy = pd.read_csv("C:/Users/USER/OneDrive/Documents/111-1/statistical consulting/final/義式1_1220.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
cursor = conn.cursor()
italy.to_sql('Italy_Recipe', conn, if_exists='replace', index=False)
conn.commit()

country = st.text_input('你今天想吃哪國的料理？')
if country == '義大利':
    ingrid_num = st.sidebar.text_input("How many ingredients do you have today?")
    if int(ingrid_num) == 1:
        ingrid1 = st.text_input('Input your first ingredient.', key=0)
        df = pd.read_sql(f"SELECT * FROM Italy_Recipe WHERE Ingredient LIKE '%{ingrid1}%'", conn)
    if int(ingrid_num) == 2:
        ingrid1 = st.text_input('Input your first ingredient.', key=0)
        ingrid2 = st.text_input('Input your second ingredient.', key=1)
        df = pd.read_sql(f"SELECT * FROM Italy_Recipe WHERE Ingredient LIKE '%{ingrid1}%' AND Ingredient LIKE '%{ingrid2}%'", conn)
    if int(ingrid_num) == 3:
        ingrid1 = st.text_input('Input your first ingredient.', key=0)
        ingrid2 = st.text_input('Input your second ingredient.', key=1)
        ingrid3 = st.text_input('Input your third ingredient.', key=2)
        df = pd.read_sql(f"SELECT * FROM Italy_Recipe WHERE Ingredient LIKE '%{ingrid1}%' AND Ingredient LIKE '%{ingrid2}%' AND Ingredient LIKE '%{ingrid3}%'", conn)
    if int(ingrid_num) == 4:
        ingrid1 =st.text_input('Input your first ingredient.', key=0)
        ingrid2 =st.text_input('Input your second ingredient.', key=1)
        ingrid3 =st.text_input('Input your third ingredient.', key=2)
        ingrid4 =st.text_input('Input your fourth ingredient.', key=3)
        df = pd.read_sql(f"SELECT * FROM Italy_Recipe WHERE Ingredient LIKE '%{ingrid1}%' AND Ingredient LIKE '%{ingrid2}%' AND Ingredient LIKE '%{ingrid3}%' AND Ingredient LIKE '%{ingrid4}%'", conn)
    if int(ingrid_num) == 5:
        ingrid1 =st.text_input('Input your first ingredient.', key=0)
        ingrid2 =st.text_input('Input your second ingredient.', key=1)
        ingrid3 =st.text_input('Input your third ingredient.', key=2)
        ingrid4 =st.text_input('Input your fourth ingredient.', key=3)
        ingrid5 =st.text_input('Input your fifth ingredient.', key=4)
        df=pd.read_sql(f"SELECT * FROM Italy_Recipe WHERE Ingredient LIKE '%{ingrid1}%' AND Ingredient LIKE '%{ingrid2}%' AND Ingredient LIKE '%{ingrid3}%' AND Ingredient LIKE '%{ingrid4}%' AND Ingredient LIKE '%{ingrid5}%'", conn)
    if int(ingrid_num) == 10:
        ingrid1 =st.text_input('Input your second ingredient.', key=0)
        ingrid2 =st.text_input('Input your second ingredient.', key=1)
        ingrid3 =st.text_input('Input your second ingredient.', key=2)
        ingrid4 =st.text_input('Input your second ingredient.', key=3)
        ingrid5 =st.text_input('Input your second ingredient.', key=4)
        ingrid6 =st.text_input('Input your second ingredient.', key=5)
        ingrid7 =st.text_input('Input your second ingredient.', key=6)
        ingrid8 =st.text_input('Input your second ingredient.', key=7)
        ingrid9 =st.text_input('Input your second ingredient.', key=8)
        ingrid10 =st.text_input('Input your second ingredient.', key=9)
        df = pd.read_sql(f"SELECT * FROM Italy_Recipe WHERE Ingredient LIKE '%{ingrid1}%' AND Ingredient LIKE '%{ingrid2}%' AND Ingredient LIKE '%{ingrid3}%' AND Ingredient LIKE '%{ingrid4}%' AND Ingredient LIKE '%{ingrid5}%' AND Ingredient LIKE '%{ingrid6}%' AND Ingredient LIKE '%{ingrid7}%' AND Ingredient LIKE '%{ingrid8}%' AND Ingredient LIKE '%{ingrid9}%' AND Ingredient LIKE '%{ingrid10}%'", conn)
    # html_temp1 = """<img style="display: block;-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://img-global.cpcdn.com/recipes/7204ffef2970ae3c/1360x964cq70/%E4%B8%80%E9%8D%8B%E5%88%B0%E5%BA%95%E7%B0%A1%E6%98%93%E5%8F%B0%E5%BC%8F-%E8%8F%9C%E8%84%AF%E9%B7%84%E6%B9%AF-%E9%A3%9F%E8%AD%9C%E6%88%90%E5%93%81%E7%85%A7%E7%89%87.webp" width="1337" height="947">"""
    # components.html(html_temp1, height=800, width=1000, scrolling=True)
    for i in range(len(df['Name'])):
        st.write(df['Name'][i])
if country == '台灣':
    ingrid_num = st.sidebar.text_input("How many ingredients do you have today?")
    if int(ingrid_num) == 1:
        ingrid1 = st.text_input('Input your first ingredient.', key=0)
        df = pd.read_sql(f"SELECT * FROM Taiwan_Recipe WHERE Ingredient LIKE '%{ingrid1}%'", conn)
    if int(ingrid_num) == 2:
        ingrid1 = st.text_input('Input your first ingredient.', key=0)
        ingrid2 = st.text_input('Input your second ingredient.', key=1)
        df = pd.read_sql(f"SELECT * FROM Taiwan_Recipe WHERE Ingredient LIKE '%{ingrid1}%' AND Ingredient LIKE '%{ingrid2}%'", conn)
    if int(ingrid_num) == 3:
        ingrid1 = st.text_input('Input your first ingredient.', key=0)
        ingrid2 = st.text_input('Input your second ingredient.', key=1)
        ingrid3 = st.text_input('Input your third ingredient.', key=2)
        df = pd.read_sql(f"SELECT * FROM Taiwan_Recipe WHERE Ingredient LIKE '%{ingrid1}%' AND Ingredient LIKE '%{ingrid2}%' AND Ingredient LIKE '%{ingrid3}%'", conn)
    if int(ingrid_num) == 4:
        ingrid1 =st.text_input('Input your first ingredient.', key=0)
        ingrid2 =st.text_input('Input your second ingredient.', key=1)
        ingrid3 =st.text_input('Input your third ingredient.', key=2)
        ingrid4 =st.text_input('Input your fourth ingredient.', key=3)
        df = pd.read_sql(f"SELECT * FROM Taiwan_Recipe WHERE Ingredient LIKE '%{ingrid1}%' AND Ingredient LIKE '%{ingrid2}%' AND Ingredient LIKE '%{ingrid3}%' AND Ingredient LIKE '%{ingrid4}%'", conn)
    if int(ingrid_num) == 5:
        ingrid1 =st.text_input('Input your first ingredient.', key=0)
        ingrid2 =st.text_input('Input your second ingredient.', key=1)
        ingrid3 =st.text_input('Input your third ingredient.', key=2)
        ingrid4 =st.text_input('Input your fourth ingredient.', key=3)
        ingrid5 =st.text_input('Input your fifth ingredient.', key=4)
        df=pd.read_sql(f"SELECT * FROM Taiwan_Recipe WHERE Ingredient LIKE '%{ingrid1}%' AND Ingredient LIKE '%{ingrid2}%' AND Ingredient LIKE '%{ingrid3}%' AND Ingredient LIKE '%{ingrid4}%' AND Ingredient LIKE '%{ingrid5}%'", conn)
        # if ingrid_num == 6:
        #      pd.read_sql(f"SELECT * FROM Taiwan_Recipe WHERE Ingredient LIKE '%{ingrid1}%' AND Ingredient LIKE '%{ingrid2}%' AND Ingredient LIKE '%{ingrid3}%' AND Ingredient LIKE '%{ingrid4}%' AND Ingredient LIKE '%{ingrid5}%' AND Ingredient LIKE '%{ingrid6}%'", conn)
        # if ingrid_num == 7:
        #      pd.read_sql(f"SELECT * FROM Taiwan_Recipe WHERE Ingredient LIKE '%{ingrid1}%' AND Ingredient LIKE '%{ingrid2}%' AND Ingredient LIKE '%{ingrid3}%' AND Ingredient LIKE '%{ingrid4}%' AND Ingredient LIKE '%{ingrid5}%' AND Ingredient LIKE '%{ingrid6}%' AND Ingredient LIKE '%{ingrid7}%'", conn)
        # if ingrid_num == 8:
        #      pd.read_sql(f"SELECT * FROM Taiwan_Recipe WHERE Ingredient LIKE '%{ingrid1}%' AND Ingredient LIKE '%{ingrid2}%' AND Ingredient LIKE '%{ingrid3}%' AND Ingredient LIKE '%{ingrid4}%' AND Ingredient LIKE '%{ingrid5}%' AND Ingredient LIKE '%{ingrid6}%' AND Ingredient LIKE '%{ingrid7}% AND Ingredient LIKE '%{ingrid8}%'", conn)
        # if ingrid_num == 9:
        #      pd.read_sql(f"SELECT * FROM Taiwan_Recipe WHERE Ingredient LIKE '%{ingrid1}%' AND Ingredient LIKE '%{ingrid2}%' AND Ingredient LIKE '%{ingrid3}%' AND Ingredient LIKE '%{ingrid4}%' AND Ingredient LIKE '%{ingrid5}%' AND Ingredient LIKE '%{ingrid6}%' AND Ingredient LIKE '%{ingrid7}% AND Ingredient LIKE '%{ingrid8}% AND Ingredient LIKE '%{ingrid9}%'", conn)
    if int(ingrid_num) == 10:
        ingrid1 =st.text_input('Input your second ingredient.', key=0)
        ingrid2 =st.text_input('Input your second ingredient.', key=1)
        ingrid3 =st.text_input('Input your second ingredient.', key=2)
        ingrid4 =st.text_input('Input your second ingredient.', key=3)
        ingrid5 =st.text_input('Input your second ingredient.', key=4)
        ingrid6 =st.text_input('Input your second ingredient.', key=5)
        ingrid7 =st.text_input('Input your second ingredient.', key=6)
        ingrid8 =st.text_input('Input your second ingredient.', key=7)
        ingrid9 =st.text_input('Input your second ingredient.', key=8)
        ingrid10 =st.text_input('Input your second ingredient.', key=9)
        df = pd.read_sql(f"SELECT * FROM Taiwan_Recipe WHERE Ingredient LIKE '%{ingrid1}%' AND Ingredient LIKE '%{ingrid2}%' AND Ingredient LIKE '%{ingrid3}%' AND Ingredient LIKE '%{ingrid4}%' AND Ingredient LIKE '%{ingrid5}%' AND Ingredient LIKE '%{ingrid6}%' AND Ingredient LIKE '%{ingrid7}%' AND Ingredient LIKE '%{ingrid8}%' AND Ingredient LIKE '%{ingrid9}%' AND Ingredient LIKE '%{ingrid10}%'", conn)
    # html_temp1 = """<img style="display: block;-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://img-global.cpcdn.com/recipes/7204ffef2970ae3c/1360x964cq70/%E4%B8%80%E9%8D%8B%E5%88%B0%E5%BA%95%E7%B0%A1%E6%98%93%E5%8F%B0%E5%BC%8F-%E8%8F%9C%E8%84%AF%E9%B7%84%E6%B9%AF-%E9%A3%9F%E8%AD%9C%E6%88%90%E5%93%81%E7%85%A7%E7%89%87.webp" width="1337" height="947">"""
    # components.html(html_temp1, height=800, width=1000, scrolling=True)
    for i in range(len(df['Name'])):
        st.write(df['Name'][i])