import pandas as pd
import streamlit as st


df = pd.read_csv("data/PALAVRAS.csv",encoding='utf-8')

st.title("Dicionário")

categoria= st.selectbox(
    label="Comece Selecionando uma Categoria:",
    placeholder="Digite Algo",
    options= df[df['CATEGORIA'].notna()]['CATEGORIA'].unique()
)

if categoria:
    df_palavras = df[(df['PALAVRA'].notna()) & (df['SIGNIFICADO'].notna())]
    palavras_validas = df_palavras[df_palavras['CATEGORIA'] == categoria]['PALAVRA'].sort_values()

    palavra = st.selectbox(
        label='Pesquise por uma Palavra',
        placeholder='Digite Algo',
        options=palavras_validas
    )

    if palavra:
        st.markdown("<style>img {border-radius:10px;}</style>", unsafe_allow_html=True)

        linha = df_palavras[df_palavras['PALAVRA']==palavra].iloc[0]

        tipo = str(linha['TIPO']) if pd.notna(linha['TIPO']) else ""

        st.markdown(f"#### {linha['PALAVRA'].upper()} {'- '+f'_{tipo}_' if tipo!='' else ''}")
        st.markdown(f":blue-background[Significado:] {linha['SIGNIFICADO']}")
        st.markdown(f":grey-background[Exemplo:] {linha['EXEMPLO']}")

        if pd.notna(linha['IMAGEM']):
            st.image(linha['IMAGEM'], use_container_width=True)

        # Exibir sinônimos, se disponíveis
        if pd.notna(linha['SINÔNIMO']):
            st.write(f"Sinônimos de {palavra}:")
            for sinonimo in linha['SINÔNIMO'].split(','):
                st.markdown(f'* {sinonimo.title()}')
        else:
            st.text('Sinônimos indisponíveis no momento.')
