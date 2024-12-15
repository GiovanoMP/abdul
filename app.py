import streamlit as st

# Título da aplicação
st.title('INTERPOL - ALERTA INTERNACIONAL')

# Texto procurado em vermelho
st.markdown('<h2 style="color: red;">Procurado por crimes em múltiplas jurisdições</h2>', unsafe_allow_html=True)

# Exibir a imagem centralizada
st.image('images/procurado.png', use_column_width=True)

# Informações sobre o procurado
st.markdown('<h1 style="color: red;">Nome: Abdul Al-Gaúcho Bin Chimarrão</h1>', unsafe_allow_html=True)
st.write('Nacionalidade: Saudita')

st.markdown('<h3 style="color: red;">Crimes atribuídos:</h3>', unsafe_allow_html=True)
st.markdown('- Contrabando internacional de erva-mate em caravanas de camelos.\n- Introdução ilegal de churrasco gaúcho no mercado saudita, causando colapso no setor de kebabs.\n- Participação em corridas clandestinas de camelos enquanto usava bombacha.\n- Uso indevido de turbante para esconder pacotes de costela premium.', unsafe_allow_html=True)

st.write('Fontes confiáveis indicam que Abdul fugiu para o Brasil e foi avistado nas redondezas de Porto Alegre.')

st.markdown('<h3 style="color: red;">Recompensa:</h3>', unsafe_allow_html=True)
st.write('Qualquer informação que leve à captura de Abdul será recompensada com 10 kg de costela premium e 1 barril de petróleo.')
