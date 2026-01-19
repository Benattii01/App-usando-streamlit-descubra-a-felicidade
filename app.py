import streamlit as st  
import pandas as pd

model3 = pd.read_pickle('model_feliz3.pkl')
#frase de inicio 
st.markdown("# Profissional de Dados descubra se você é Feliz! ")
st.markdown("Teste diferentes cenários explorando como as variáveis podem influenciar sua felicidade ")
#separndo colunas 
col1, col2, col3 = st.columns(3) 

with col1:
    video_game = st.radio('curte video game?',["sim","não"])
    futebol = st.radio('curte futebol?',['sim','não'])
with col2:
    livros = st.radio('curte livros?',['sim','não'])
    tabuleiro = st.radio('curte jogos de tabuleiro?',['sim','não'])
with col3: 
    f1 = st.radio('curte formula 1 ?',['sim','não'])
    mma = st.radio('curte MMA ?',['sim','não'])

idade = st.number_input('Sua idade',18,100)

redes_opt = ['linkedIn','twich','YouTube','Istagram','Amigos','Twitter/X','Outra rede']
cursos_opt = ['0','1','2','3','mais de 3']
ufs = ['AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MT', 'PA', 'PB',
       'PE', 'PR', 'RJ', 'RN', 'RS', 'SC', 'SP']
areas_formação = ['Exatas', 'Biológicas', 'Humanas']
tempo_area =  ['Mais de 4 anos' ,'Não atuo', 'De 1 ano a 2 anos', 'De 0 a 6 meses',
 'de 2 anos a 4 anos', 'De 6 meses a 1 ano']
senioridade = ['Sênior' ,'Iniciante', 'Júnior' ,'Pleno', 'Gerência' ,'Coordenação',
 'Especialista', 'Diretoria' ,'C-Level']

col1, col2 = st.columns(2)
with col1:
    redes = st.selectbox('como conheceu Téo me why?',options = redes_opt)
    area = st.selectbox('Area de formação',areas_formação)
    tempo = st.selectbox('Quanto tempo na area',tempo_area)
with col2: 
    cursos = st.selectbox('Quantos cursos acompanhou do Téo Me Why?', cursos_opt)
    uf = st.selectbox('Seus estado',ufs)
    senioridade1 = st.selectbox('Posiçãona cadeira',senioridade)

data = {'Como conheceu o Téo Me Why?':redes,
        'Quantos cursos acompanhou do Téo Me Why?':cursos, 
        'Curte games?':video_game,
        'Curte futebol?': futebol, 
        'Curte livros?': livros, 
        'Curte jogos de tabuleiro?': tabuleiro,
        'Curte jogos de fórmula 1?': f1, 
        'Curte jogos de MMA?':mma, 
        'Idade': idade,
        'Estado que mora atualmente': uf, 
        'Área de Formação': area,
        'Tempo que atua na área de dados':tempo, 
        'Posição da cadeira (senioridade)':senioridade1,
        }
data1 ={'Curte games?':video_game,
        'Curte futebol?': futebol, 
        'Curte livros?': livros, 
        'Curte jogos de tabuleiro?': tabuleiro,
        'Curte jogos de fórmula 1?': f1, 
        'Curte jogos de MMA?':mma, 
        'Idade': idade,
        }
data2 = {'Como conheceu o Téo Me Why?':redes,
        'Quantos cursos acompanhou do Téo Me Why?':cursos, 
        'Estado que mora atualmente': uf, 
        'Área de Formação': area,
        'Tempo que atua na área de dados':tempo, 
        'Posição da cadeira (senioridade)':senioridade1,
        }

#transformar meus dados em um dataframe 
df_dummy = pd.DataFrame([data2])
df_num = pd.DataFrame([data1])
df = df_num.replace({'sim': 1, 'não': 0})

#variaveis que vou transformar em dummys
dummy_vars = [
    'Como conheceu o Téo Me Why?',
    'Quantos cursos acompanhou do Téo Me Why?',
    'Estado que mora atualmente',	
    'Área de Formação',	
    'Tempo que atua na área de dados',	
    'Posição da cadeira (senioridade)',
]

#transformando em dummy
df2 = pd.get_dummies(df_dummy[dummy_vars]).astype(int)

df_final = pd.concat(
    [df.reset_index(drop=True), df2.reset_index(drop=True)],
    axis=1
)

df_template = pd.DataFrame(columns=['Como conheceu o Téo Me Why?_Amigos',
       'Como conheceu o Téo Me Why?_Instagram',
       'Como conheceu o Téo Me Why?_LinkedIn',
       'Como conheceu o Téo Me Why?_Outra rede social',
       'Como conheceu o Téo Me Why?_Twitch',
       'Como conheceu o Téo Me Why?_Twitter / X',
       'Como conheceu o Téo Me Why?_YouTube',
       'Quantos cursos acompanhou do Téo Me Why?_0',
       'Quantos cursos acompanhou do Téo Me Why?_1',
       'Quantos cursos acompanhou do Téo Me Why?_2',
       'Quantos cursos acompanhou do Téo Me Why?_3',
       'Quantos cursos acompanhou do Téo Me Why?_Mais que 3',
       'Estado que mora atualmente_AM', 'Estado que mora atualmente_BA',
       'Estado que mora atualmente_CE', 'Estado que mora atualmente_DF',
       'Estado que mora atualmente_ES', 'Estado que mora atualmente_GO',
       'Estado que mora atualmente_MA', 'Estado que mora atualmente_MG',
       'Estado que mora atualmente_MT', 'Estado que mora atualmente_PA',
       'Estado que mora atualmente_PB', 'Estado que mora atualmente_PE',
       'Estado que mora atualmente_PR', 'Estado que mora atualmente_RJ',
       'Estado que mora atualmente_RN', 'Estado que mora atualmente_RS',
       'Estado que mora atualmente_SC', 'Estado que mora atualmente_SP',
       'Área de Formação_Biológicas', 'Área de Formação_Exatas',
       'Área de Formação_Humanas',
       'Tempo que atua na área de dados_De 0 a 6 meses',
       'Tempo que atua na área de dados_De 1 ano a 2 anos',
       'Tempo que atua na área de dados_De 6 meses a 1 ano',
       'Tempo que atua na área de dados_Mais de 4 anos',
       'Tempo que atua na área de dados_Não atuo',
       'Tempo que atua na área de dados_de 2 anos a 4 anos',
       'Posição da cadeira (senioridade)_C-Level',
       'Posição da cadeira (senioridade)_Coordenação',
       'Posição da cadeira (senioridade)_Diretoria',
       'Posição da cadeira (senioridade)_Especialista',
       'Posição da cadeira (senioridade)_Gerência',
       'Posição da cadeira (senioridade)_Iniciante',
       'Posição da cadeira (senioridade)_Júnior',
       'Posição da cadeira (senioridade)_Pleno',
       'Posição da cadeira (senioridade)_Sênior', 
       'Curte games?',
       'Curte futebol?', 
       'Curte livros?', 
       'Curte jogos de tabuleiro?',
       'Curte jogos de fórmula 1?', 
       'Curte jogos de MMA?', 
       'Idade',
       ])

#acrescentar modelo 
df = pd.concat([df_template,df_final]).fillna(0)

#st.data_editor(df)

proba = model3['model'].predict_proba(df[model3['features']])[:,1][0]

if proba > 0.7:
    st.success(f"Você é uma pessoa feliz! Probabilidade: {100 * proba:.0f}%")

elif proba > 0.4:
    st.warning(f"Você é uma pessoa meio feliz! Probabilidade: {100 * proba:.0f}%")

else:
    st.error(f"Você é uma pessoa nada feliz! Probabilidade: {100 * proba:.0f}%")
