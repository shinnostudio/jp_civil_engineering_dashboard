import pandas as pd
import streamlit as st
import pydeck as pdk
import plotly.express as px

st.title('日本のICT土木に関するデータ')
st.header('ICT土木工事件数（国土交通省直轄工事）')
st.write("Data Source :  [国土交通省 - ICT施工の普及拡大に向けた取組](https://www.mlit.go.jp/sogoseisaku/constplan/content/001493469.pdf)")


#Data Source
df_civil_eng_count = pd.read_csv('./csv_data/jp_ict_civil_engineering_count.csv', encoding='shift_jis')

st.subheader('工事種別毎の件数')

df_public_count_by_category = df_civil_eng_count[(df_civil_eng_count['工種'] != '合計') & (df_civil_eng_count['データ種別'] == '公告件数')]
df_public_count_by_category['件数'] = df_public_count_by_category['件数'].astype(int)
max_count = df_public_count_by_category['件数'].max() + 100


df_count_by_category = df_civil_eng_count[df_civil_eng_count['工種'] != '合計']
df_count_by_category['件数'] = df_count_by_category['件数'].astype(int)
max_count = df_count_by_category['件数'].max() + 100

fig = px.bar(
    df_count_by_category,
    x = '工種',
    y = '件数',
    color = 'データ種別',
    animation_frame = '集計年',
    barmode='group',
    range_y = [0, max_count]
)
st.plotly_chart(fig)


st.subheader('合計件数')

df_public_count_sum = df_civil_eng_count[(df_civil_eng_count['工種'] == '合計') & (df_civil_eng_count['データ種別'] != '実施率')]
df_public_count_sum['件数'] = df_public_count_sum['件数'].astype(int)
max_count = df_public_count_sum['件数'].max() + 100

fig = px.bar(
    df_public_count_sum,
    x = '集計年',
    y = '件数',
    color = 'データ種別',
    barmode='group',
    range_y = [0, max_count]
)
st.plotly_chart(fig)



st.header('業種別許可業者数')
st.write("Data Source :  [国土交通省 - 建設業許可業者数調査の結果について ](https://www.mlit.go.jp/report/press/content/001478910.pdf)")

#Data Source
df_licensed_contractors_number = pd.read_csv('./csv_data/jp_licensed_contractors_number.csv', encoding='shift_jis')

fig = px.bar(
    df_licensed_contractors_number,
    x = '集計年',
    y = '事業者数',
    color = '業種',
    barmode='group'
)
st.plotly_chart(fig)


st.header('資本階層別事業者数（R4）')
st.write("Data Source :  [国土交通省 - 建設業許可業者数調査の結果について ](https://www.mlit.go.jp/report/press/content/001478910.pdf)")

#Data Source
df_contractors_by_capital = pd.read_csv('./csv_data/jp_contractors_by_capital.csv', encoding='shift_jis')

fig = px.bar(
    df_contractors_by_capital,
    x = '資本金階層',
    y = '事業者数',
    color = '業種',
    barmode='group'
)
st.plotly_chart(fig)