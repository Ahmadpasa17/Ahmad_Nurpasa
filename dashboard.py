import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

pwd = os.getcwd()

def byseason(df):
    season_rent = df[df['year'] == 2011].groupby(by='season')['count'].sum()
    return season_rent

def bymonth(df):
    month_rent = df[df['year'] == 2012].groupby(by='month')['count'].sum()
    return month_rent

# import dataframe
day_df = pd.read_csv('C:\\Users\\Asus\\Downloads\\Submission\\dashboard\\day_data.csv')

# Menyiapkan dataframe yang dikelompokkan
byseason_df = byseason(day_df)
bymonth_df = bymonth(day_df)

st.header('Dashboard Bike Sharing')
st.markdown("""
<div style="text-align: justify">
  Dashboard ini menyajikan visualisasi data yang menggambarkan penggunaan sepeda pada tahun 2011 dan 2012.
</div>
""", unsafe_allow_html=True)

st.markdown("\n")

st.subheader('Persentase penggunaan rental sepeda berdasarkan musim di 2011')


# Menampilkan plot
fig, ax = plt.subplots(figsize=(8, 8))
season = ('fall', 'summer', 'winter', 'spring')
values = [419650, 347316, 326137, 150000]
colors = ('#8B4513', '#FFF8DC', '#93C572', '#E67F0D')
explode = (0.1, 0, 0, 0)

ax.pie(values, labels=season, autopct='%1.1f%%', colors=colors, explode=explode)
st.pyplot(fig)

st.markdown("\n")

st.subheader('Jumlah penggunaan rental sepeda berdasarkan bulan di 2012')

# Berdasarkan Bulan
fig, ax = plt.subplots(figsize=(12, 5))

sns.barplot(x=bymonth_df.index, y=bymonth_df.values)

plt.xlabel("month")
plt.ylabel("values")
plt.title("Monthly Distribution")
plt.xticks(rotation=20)

ax.set_ylabel('values')
ax.set_xlabel('month')
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)
st.pyplot(fig)

st.caption('Copyright (c) Ahmad Nurpasa 2023')
