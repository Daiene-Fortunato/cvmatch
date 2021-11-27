import streamlit as st
import pdfplumber
import nltk
import numpy as np
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
nltk.download('punkt')
nltk.download('stopwords')


st.set_page_config(page_title = 'MatchCV - Powered by Daiene Fortunato',  
				   layout = 'centered', 
				   initial_sidebar_state = 'auto')

vagas = pd.read_excel('vagas.xlsx', sheet_name = None)
n_vagas = len(vagas.keys())
nome_vagas = list(vagas.keys())
vagas = [vagas[nome_vagas[i]] for i in range(n_vagas)]

def MatchCV(textoCRU, vaga, limite = 3):
    
    lista_de_palavras = nltk.tokenize.word_tokenize(textoCRU)
    lista_de_palavras = [palavra.lower() for palavra in lista_de_palavras]
    pontuacao = ['(',')',';',':','[',']',',','–','(',')','/','|','-','%','@']
    stop_words = nltk.corpus.stopwords.words('portuguese')
    keywords = [palavra for palavra in lista_de_palavras if not palavra in stop_words and not palavra in pontuacao]
    textocv = " ".join(s for s in keywords)
    pesos = list(vaga['pesos'])
    palavras_chaves = list(vaga['palavras-chave'])
    cont = [textocv.count(pc) for pc in palavras_chaves]

    def aux(x, limite):
        return x if x <= limite else limite

    cont = [aux(i, limite) for i in cont]
    pmax = np.sum(np.array(pesos) * limite) 
    score = ((np.array(cont) * pesos).sum()/pmax).round(4)

    return score

st.markdown('# :page_facing_up:​CVMatch:page_facing_up:​')
st.markdown('## Analisando e comparando currículos com vagas de trabalho')
st.markdown('---')
st.markdown('## Carregue o PDF de um ou mais currículos que você deseja analizar')

PDFs = st.file_uploader('O arquivo deve ter no máximo 10mb e ter a extenção ".pdf"',
				 type = ['pdf'],
				 accept_multiple_files = True)

st.markdown('## Carregue o arquivo de vagas com as alterações que deseja')

vagasxlsx = st.file_uploader('O arquivo deve ter no máximo 10mb e ter a extenção ".xlsx"',
                 type = ['xlsx'],
                 accept_multiple_files = False)

if st.button('Dar Match'):

    vagas = pd.read_excel(vagasxlsx, sheet_name = None)
    n_vagas = len(vagas.keys())
    nome_vagas = list(vagas.keys())
    vagas = [vagas[nome_vagas[i]] for i in range(n_vagas)]
    lista_de_cvs = []
    for arquivoPDF in PDFs:
        if arquivoPDF is not None:
            cv = pdfplumber.load(arquivoPDF)
            primeira_pagina = cv.pages[0]
            textoCRU = primeira_pagina.extract_text()
            lista_de_cvs.append(textoCRU)

    pessoas = [[MatchCV(cv, vaga) for vaga in vagas] for cv in lista_de_cvs] 
    matchs = pd.DataFrame(pessoas, columns = nome_vagas)
    st.write(matchs)

 