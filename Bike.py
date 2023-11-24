# -*- coding: utf-8 -*-
"""Copy of Templat-notebook

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/107sNXkJbQFTOyBzR2gc_CE0D_1bvVUO8

# Proyek Analisis Data: Nama dataset
- Nama: JISRON MALIK
- Email: jisron94@gmail.com
- Id Dicoding: jisron94
"""



"""## Menentukan Pertanyaan Bisnis

- pertanyaan 1
  Faktor yang membuat user memilih untuk menggunakan sepeda?
- pertanyaan 2
  Bagaimana perubahan perilaku user dalam penggunaan sepeda?

## Menyiapkan semua library yang dibutuhkan
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import streamlit as st

with st.echo():
    st.write('''import pandas as pd
    from pandas import DataFrame
    import matplotlib.pyplot as plt
    # %matplotlib inline
    import seaborn as sns''')



"""## Data Wrangling

### Gathering Data
"""

df = pd.read_csv('day.csv', delimiter=",")
df.head()

"""Meload data yang akan digunakan dengan menggunakan library pandas untuk meload file data berupa excel dengan format csv serta menampilkan 5 data teratas

### Assessing Data
"""
dinf = df.info()
st.dataframe(dinf)

"""selanjutnya kita mencek info yang terdapat dalam data untuk melihat type data dan total data yang ada

### Cleaning Data
"""

df.isna().sum()

"""proses selanjutnya kita melakukan pengecekan data kosong yang ada dengan menggunakan fitur isna() sehingga kita mengetahui apakahaterdapat dapat kosong pada data yang akan kita gunakan, berdasarkan hasil diatas tidak terdapat data kosong sehingga kita dapat langsung menggunakan data diatas."""

df.duplicated().sum()

"""setelah mencek data kosong selanjutnya kita juga melihat apakah terdapat data duplikat dalam data kita karena sangat berpengaruh dalam proses selanjutnya, berdasarkan hasil tersebut data kita tidak terdapat data duplikat sehingga data kita dapat dikatakan bersih

## Exploratory Data Analysis (EDA)
"""

df2 = df.groupby(['season','weathersit']).agg({
    'temp': 'mean',
    'atemp': 'mean',
    'hum': 'mean',
    'windspeed' : 'mean',
    'cnt':'mean',
})
df3 = df2.mask(df2>1,df2/10000).round(2)
df3

"""Disini kita melakukan explorasi data yang akan digunakan untuk proses analisis kedepannya, disini kita telah melakukan pemilihan data yang akan digunakan.

### Explore ...
"""

df3.corr()

"""Selanjutnya kita melakukan analisi berdasarkan nilai korelasi tersebut, kita dapat menyimpulkan bahwa kolom windspeed di atas tidak memiliki korelasi karena nilainya mendekati nol.
kita akan membuat dataframe baru tanpa menggunakan kolom windspeed
"""

df4 = df3.drop(columns=['windspeed'])
df4.corr()

"""disini kita telah melakukan eksekusi data sehingga data yang kita miliki dapat digunakan untuk analisis

## Visualization & Explanatory Analysis

### Pertanyaan 1: Faktor yang membuat user memilih untuk menggunakan sepeda?
"""

df4.nlargest(n=10, columns=['cnt'])

"""disini kita menampilkan urutan 10 data teratas agar dapat mendapatkan insight terhadap data yang kita miliki"""

plt.figure(figsize=(8, 4))
plt.title('BIKE', size=15)
df4['cnt'].plot(kind='bar')
df4['temp'].plot(kind='line')
df4['atemp'].plot(kind='line')
df4['hum'].plot(kind='line')
plt.gca().spines[['top', 'right']].set_visible(False)
plt.legend()
st.pyplot(plt)

"""disini kita melakukan visualisasi data dengan menggabungkan diagram garis dan batang agar data kita dapat mudah dicerna"""

heat = sns.heatmap(df4, annot=True)
st.pyplot(heat.fig)

"""disini kita menggunakan heatmap untuk melihat nilai-nilai terbaik dalam data yang kita punya

### Pertanyaan 2:

Bagaimana perubahan perilaku user dalam penggunaan sepeda?
"""

dfs2 = df.groupby(['yr','season']).agg({
    'temp': 'mean',
    'atemp': 'mean',
    'hum': 'mean',
    'cnt':'mean',
})
dfs3 = dfs2.mask(dfs2>1,dfs2/10000).round(2)
dfs3

"""disini kita melakukan pemilihan data agar daat digunakan sesuai dengan kebutuh data yang kita inginkan. Disini saya menggunakan data berdasarkan tahun dan musim"""

plt.figure(figsize=(8, 4))
plt.title('BIKE by YEARS', size=15)
dfs3['temp'].plot(kind='line')
dfs3['atemp'].plot(kind='line')
dfs3['cnt'].plot(kind='line')
plt.legend()
plt.gca().spines[['top', 'right']].set_visible(False)

"""Disini kita menampilkan grafik berdasarkan data yang telah kita pilih sebelumnya

## Conclusion

- Conclution pertanyaan 1

  Terlihat dalam data diatas ada beberapa faktor yang mempengaruhi pengambilan keputusan user dalam memilih untuk menggunakan sepeda, terlihat bahwa rata-rata penggunaan sepeda terbanyak terjadi pada saat nilai temp berada diantara 0.4-0.72, nilai atemp berada diantara 0.4-0.67 dan nilai hum berada diantara 0.55-0.75 dimana pada rentan nilai tersebut tubuh manusia merasa nyaman untuk beraktivitas diluar ruangan.

- Conclution pertanyaan 2

  Berdasarkan pada data dua tahun terakhir dapat diketahui bahwa perilaku user dalam menggunakan sepeda lebih disukai pada saat keaadan cuaca hangat dan kondisi cuaca dalam keadaan relatif cerah, terlihat juga bahwa telah menjadi sebuah tren dalam penggunaan sepeda pada saat season 2 hingga season 3 sehingga dapat disediakan jumlah sepeda yang jauh lebih banyak dibandingkan pada saat season awal dan akhir tahun dikarenakan suhu udara cenderung lebih rendah dan keadaan cuaca tidak memungkinkan untuk bersepeda.
"""
