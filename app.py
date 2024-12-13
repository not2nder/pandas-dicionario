import pandas as pd
import streamlit as st


data = {
    "Comunicação e Linguagem": "data/comunicação.csv",
    "Sentimentos e Emoções": "data/sentimentos.csv",
    "Comportamentos Humanos": "data/comportamentos.csv",
}

st.title("Dicionário")

categorias= st.multiselect(
    label="Comece Selecionando uma Categoria:",
    placeholder="Digite Algo",
    options=data
)

if categorias:
    li = []
    for categoria in categorias:
        df = pd.read_csv(data[categoria],encoding='utf-8')
        li.append(df)

    df = pd.concat(li,axis=0,ignore_index=True)
    df = df[df['PALAVRA'].notna() & (df['PALAVRA'] != '')]

    palavra = st.selectbox(
        label='Pesquise por uma Palavra',
        placeholder='Digite Algo',
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
        
