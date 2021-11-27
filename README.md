![Licensa MIT](https://img.shields.io/github/license/Daiene-Fortunato/Projeto_CVMatch)![GitHub repo size](https://img.shields.io/github/repo-size/Daiene-Fortunato/Projeto_CVMatch) ![GitHub top language](https://img.shields.io/github/languages/top/Daiene-Fortunato/Projeto_CVMatch)

# :page_facing_up: CVMatch :page_facing_up: - Seja bem-vindo(a)!

​		Projeto de **Data Science** para iniciantes que desejam aprender a executar o tratamento e análise de dados simples através da programação. Tem o objetivo de **automatizar** a análise de  currículos para comparar e pontuar a relação das palavras-chaves encontradas com os modelos de vagas de trabalho da área de desenvolvimento de software.

​		Analisar currículos é difícil; tanto para o candidato que precisa garantir a qualidade da sua apresentação, quanto para o recrutador que tem pouco tempo para selecionar ou excluir o documento entre uma pilha. Automatizar essa avaliação inicial pode beneficiar e muito ambas as partes, o candidato obtém uma ideia da qualidade do seu texto e pode editar as partes que ficaram aquém, o recrutador pode escolher entrevistar apenas os melhores resultados, assim economiza tempo.  

Quer aprender um jeito fácil de programar e obter esse recurso? Eu te ajudo.

### Preparação

------

Há duas maneiras de utilizar o código:

1. Através do [Google Colab](https://colab.research.google.com/), você não vai precisar instalar nada e poderá ver na tela o resultado da comparação.
2. Através do seu ambiente local, para essa escolha tenha atenção especial aos requisitos informados, pois será necessário baixar uma IDE, módulos e etc.

​	Obs: eu não vou te ensinar a fazer o deploy deste projeto, mas se for fazer use o [Streamlit Share](https://share.streamlit.io/) ou o [Heroku](https://heroku.com/), são gratuitos e fáceis de usar.

### Usando o Google Colab (recomendado)

------

​		O Google Colab é uma ferramenta de programação em nuvem que permite a utilização de algumas linguagens como Python, R, Julia e Swift em conjunto com textos e imagens. Além disso, o ambiente é colaborativo, você pode fragmentar e rodar todo o código, fazer testes, desenvolver versões e compartilhar resultados com seus amigos e colegas de trabalho. 

Para executar o CVMatch no google colab você vai precisar:

1. Possuir uma conta google e acessar o colab [aqui](https://colab.research.google.com/)
2. Inserir o código exatamente como nesse [arquivo](https://github.com/Daiene-Fortunato/cvmatch/blob/main/colab.ipynb)
3. Adicionar na pasta do ambiente o seu "curriculo.pdf"
4. Adicionar na pasta do ambiente o arquivo "vagas.xlsx" com alterações (leia: VAGAS.md)
5. Copiar e inserir no código o caminho dos seus arquivos
6. Rodar cada seção em ordem (1,2,3,4) para visualizar a pontuação na tela

​	Todas as ações são interativas e fáceis de serem implementadas, tenha calma e observe o ambiente ou assista vídeos de instrução no youtube.

- Exemplo de pontuação entre currículo e vaga de desenvolvedor:

![CVMatch](https://github.com/Daiene-Fortunato/cvmatch/blob/main/example.png?raw=true)

### Usando o Local Host (avançado)

------

​	Para fazer a aplicação rodar no seu ambiente local você terá que fazer algumas instalações e possuir conhecimentos básicos de programação, siga os passos descritos abaixo.

**Requisitos:**

- Anaconda (4.10.3)
- Python (3.9.7)
- Git (2.33.1)
- Vs Code ou PyCharm
- streamlit (0.83.0)
- pdfplumber (0.5.2)
- nltk (3.5.0)
- numpy (1.19.2)
- pandas (1.1.3)
- wordcloud (1.8.1)
- matplotlib (3.3.2)

**Conhecimento prévio:**

- Saber usar o terminal do Anaconda para instalar as bibliotecas
- Saber configurar uma IDE para a linguagem Python
- Saber implementar uma aplicação no local host através do StreamLit
- Saber fazer um fork do github e puxar ele para sua máquina local

### Instalando

------

1. Instale os requisitos
2. Faça um fork deste repositório e um pull para sua máquina local
3. Pelo terminal do Anaconda faça o StreamLit rodar o arquivo cvmatch.py
4. Uma aba deve abrir no seu navegador padrão contendo um painel interativo
5. Adicione um ou mais currículos que deseja avaliar
6. Adicione o arquivo vagas.xlsx"
7. Clique no botão "Dar Match"
8. Agora basta observar sua pontuação

## Origem do Projeto e Agradecimentos

​				A ideia de construir esse projeto surgiu durante uma aula do Curso de Imersão em Data Science da [Flai](https://www.flai.com.br/) uma empresa de consultoria e ensino que eu descobri por acaso, mas que deu uma luz nos meus estudos. Fica registrado meu agradecimento.

​				O modelo utilizado para o Google Colab é uma cópia do que foi escrito em aula para exemplificar uma das tantas possibilidades da análise de dados entre arquivos de texto, tabelas e matchs para a área de dados, já a codificação para o ambiente local foi alterada e incrementada por mim para se tornar viável como uma aplicação Web independente voltada ao setor de desenvolvimento de sistemas.

## Contribuindo

​		Teve uma ideia que pode melhorar ou acrescentar algo bacana ao projeto? Leia [CONTRIBUTING.md](https://github.com/Daiene-Fortunato/cvmatch/blob/main/CONTRIBUTING.md) para obter detalhes sobre o processo de envio de solicitações pull.

**Desafios Propostos:**

- [ ] Construir a opção "Candidato" ou "Recrutador"
- [ ] Excluir o arquivo vagas.xlsx e colocar opções de seleção dentro do ambiente
- [ ] Para o candidato: inserir gráficos e outros recursos (WCloud) como saída da análise
- [ ] Para o recrutador: inserir outros recursos de saída além da pontuação
- [ ] Colocar a saída da pontuação num formato: pts_obtidos | pts_max

Divirta-se!

## Autoras

Contribuiu com:

1.  **cvmatch.py**
2.  **colab.ipynb**
2.  VAGAS.md
3.  README.md
4.  LICENSE.md
5.  CONTRIBUTING.md
6.  example.png



:woman_student: [**Daiene Fortunato**](https://www.linkedin.com/in/daienefortunato/) - Gestora de TI e Dev Backend

:email:  daiene.fortunato@gmail.com

![Daiene Fortunato](https://media-exp1.licdn.com/dms/image/D4E03AQGBXxy-MaASgA/profile-displayphoto-shrink_200_200/0/1634165214468?e=1643241600&v=beta&t=3nP5RbaTr6Sw_K4_6v255iU3MTWK6u94AF2Cxzf60nk)



------

Contribuiu com:

1. Origem do **colab.ipynb**



:woman_student: [**Juliana Scudilho**](https://www.linkedin.com/in/julianascudilio/) da [Flai](flai.com.br) - Data Science e Inteligência Artificial

:email: juliana-scudilio@uol.com.br

![JULIANA SCUDILIO](https://media-exp1.licdn.com/dms/image/C4E03AQEepqyGWj1iww/profile-displayphoto-shrink_200_200/0/1619750599237?e=1643241600&v=beta&t=qxhlW1i4hg-C-Nndyw4z8usKS_KXcQVHBYz_GV0E_lU)



## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE.md](https://github.com/Daiene-Fortunato/wcloud/blob/main/LICENSE.md) para detalhes
