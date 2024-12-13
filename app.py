import pandas as pd
import streamlit as st

df = pd.read_csv('data.csv',encoding='utf-8')
df= df[df['PALAVRA'].notna() & (df['PALAVRA'] != '')]

st.title("Dicionário")

palavra = st.selectbox(
    label='Pesquise por uma Palavra',
    placeholder='Digite',
    options=df.sort_values('PALAVRA')
)

if palavra:
    linha = df[df['PALAVRA']==palavra].iloc[0]

    st.subheader(linha['PALAVRA'].upper())
    st.markdown(f":blue-background[Significado:] {linha['SIGNIFICADO']}")
    st.markdown(f":blue-background[Exemplo:] {linha['EXEMPLO']}")

    st.write(f"Sinônimos de {palavra}:")
    for significado in linha['SINÔNIMO'].split(','):
        st.markdown(f'- {significado.title()}')
    
