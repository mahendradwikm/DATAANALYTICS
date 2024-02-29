import streamlit as st 
import pandas as pd

 
st.write(
    """
    # ASSALAMUALAIKUM GAES
    bismillah data analyst wkkwwk
    """
)

import streamlit as st
import pandas as pd
 
st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))


st.title('Belajar Analisis Data')
st.header('Pengembangan Dashboard')
st.subheader('Pengembangan Dashboard')
st.caption('Copyright (c) 2023')

code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
 
st.dataframe(data=df, width=500, height=150)

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df)

st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

import matplotlib.pyplot as plt
import numpy as np
 
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)


# Menuliskan teks dengan ukuran font yang diubah
st.write(
    """
    <span style="font-size:40px"> INPUT NAMA DLU BG</span>
    """,
    unsafe_allow_html=True
)
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)


st.write(
    """
    <span style="font-size:26px"> Coba deskripsiin diri lu bg</span>
    """,
    unsafe_allow_html=True
)
text = st.text_area('Desc')
st.write('Description: ', text)


st.write(
    """
    <span style="font-size:26px"> Info umur?</span>
    """,
    unsafe_allow_html=True
)
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

import datetime


st.write("""<span style="font-size:26px"> Lahir kapan bg?</span>""",unsafe_allow_html=True)
date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)

st.write("""<span style="font-size:26px"> Upload dataset dlu bg</span>""",unsafe_allow_html=True)
uploaded_file = st.file_uploader('Choose a CSV file')
 
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

st.write("""<span style="font-size:26px"> skrg selfie dlu, CISSSSS</span>""",unsafe_allow_html=True)
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)


st.write("""<span style="font-size:26px"> Kalo gabut pencet ini bg</span>""",unsafe_allow_html=True)
if st.button('Say hello'):
    st.write('Hello there')


st.write("""<span style="font-size:26px"> Apakah km suka makan siang gratis?</span>""",unsafe_allow_html=True)
agree = st.checkbox('I agree')
 
if agree:
    st.write('FIX 02')


import streamlit as st

# Teks pertanyaan tentang genre film
st.write("""<span style="font-size:26px"> Genre film fav apa bg?</span>""", unsafe_allow_html=True)

# Pilihan antara radio button atau select box
option = st.radio("Choose your preference:", ["Radio Button", "Select Box"])

# Jika user memilih radio button
if option == "Radio Button":
    genre = st.radio(
        label="What's your favorite movie genre",
        options=('Comedy', 'Drama', 'Documentary'),
        key='radio'
    )
# Jika user memilih select box
else:
    genre = st.selectbox(
        label="What's your favorite movie genre",
        options=('Comedy', 'Drama', 'Documentary'),
        key='select'
    )

# Tampilkan pilihan genre yang dipilih
st.write("Your favorite movie genre is:", genre)



st.write("""<span style="font-size:26px"> Kalo makan biasannya abis di range brp bang?</span>""", unsafe_allow_html=True)

values = st.slider(
    label='Select a range of values (dalam ribuan)',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)