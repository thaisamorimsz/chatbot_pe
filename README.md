# chatbot_pe


Este projeto consiste na elaboração de um chatboot para a classificação do preço de residências em caras ou baratas em um determinado bairro, com o uso de Decision Tree 
Classification em Python, através da utiização de critérios e aleatoriedade dos dados de treino,  que aumentam a precisão das árvores do chatboot. A seguir vejamos o passo a passo de desenvolvimento:

## Dados de uso

Utilizamos os dados referentes ao ZipCode : 98004 da tabela [House Sales in King County, USA](https://www.kaggle.com/harlfoxem/housesalesprediction), a qual contém 21 colunas.

## Desenvolvimento

- [X] **Tratamento dos dados de entrada:**
neste passo fizemos o tratamento dos dados com a ajuda da biblioteca [pandas](https://pandas.pydata.org/docs/user_guide/index.html) e da [csv](https://docs.python.org/pt-br/3/library/csv.html) no arquivo *data_treatment.py*, basicamente consiste na leitura dos dados totais presentes no arquivo *nossas_casas.csv* e o tratamento através de alguns critérios que selecionamos, os quais estão presentes no arquivo *criterios.csv*, com isso após esse tratamento há a geração dos arquivos tratados em forma binária, entitulados como *nossas_casas_tratadas_j.csv*.

- [X] **Geração da árvore:**
o proximo passo consiste na geração das árvores e na obtenção das precisões das árvores, nesta parte fizemos o uso das bibliotecas [pandas](https://pandas.pydata.org/docs/user_guide/index.html), [csv](https://docs.python.org/pt-br/3/library/csv.html), [sklearn.tree.DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html), [sklearn.model_selection.train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

## Considerações Finais 
