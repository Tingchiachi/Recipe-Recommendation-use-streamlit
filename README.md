# Recipe-Recommendation-use-streamlit
食譜推薦

## Python套件
使用streamlit創建Web app

### st.write()使用方法

st.write(data_frame) : Displays the DataFrame as a table.

st.write(func) : Displays information about a function.

st.write(markdown)

### 繪圖功能
st.line_chart()

st.bar_chart()

## 食譜網站
爬取兩個網站的食譜
>get_recipe.ipynb中get_icook為爬取icook，get_recipe為爬取cookpad
1. [icook](https://icook.tw/)
2. [cookpad](https://cookpad.com/tw/home)

## 飲食習慣
依據台灣人最常的幾種進行區分，分成台式、義式、日式三種料理方式。

## 使用方法
輸入今天想吃的國家料理及食材數量、種類，最後就會推薦適當的食譜！
>使用recipe.py
![image](https://github.com/Tingchiachi/Recipe-Recommendation-use-streamlit/blob/main/streamlit.png)
