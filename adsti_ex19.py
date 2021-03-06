# -*- coding: utf-8 -*-
"""ADSTI_EX19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RHxlR7hTEWNN6xtUEH0wikyDLoPWBP1y

# **Carregamento**
"""

#Carregamento do dataset:
from google.colab import files
src = list (files.upload ().values ())[0]
open ("kc_house_data.csv", "wb").write (src)

"""# **Uso**"""

import pandas as pd

dataset = pd.read_csv ("kc_house_data.csv", sep = ",")
print (type (dataset))
dataset.head ()

"""# **Alteração do DATAFREME**"""

#Importar a biblioteca Pandas:
import pandas as pd
#Adicionar uma nova coluna ao DataFrame, atribuindo o valor zero aos registros dela:
dataset["tamanho"] = 0
#Imprimir o DataFrame com os valores da nova coluna criada:
print (dataset)
#Visualizar o DataFrame com os valores da nova coluna criada:
dataset

#Importar a biblioteca Pandas:
import pandas as pd
#Criar uma nova coluna e preencher os novos registros com dados resultantes de um processamento:
dataset["tamanho"] = dataset["bedrooms"] * 20
#Visualizar os dados da nova coluna:
dataset["tamanho"].head (10)

#Importar a biblioteca Pandas:
import pandas as pd
#Visualizar as colunas "bedrooms" e "tamanho":
dataset[["bedrooms", "tamanho"]]

#Importar a biblioteca Pandas:
import pandas as pd
#Gerar um novo DataFrame com as colunas "bedrooms" e "size":
novo_dataset = dataset[["bedrooms", "tamanho"]]
novo_dataset

"""# **Apply**"""

#Importar a biblioteca Pandas:
import pandas as pd
#Definição da função que será usada na geração dos valores para a novacoluna:
def categorizar (tam):
 if tam >= 70:
  return "Grande"
 elif tam >= 50:
  return "Médio"
 else:
  return "Pequeno"
#Criar uma nova coluna no "DataFrame" e aplicar função definida acima:
dataset["categoria_banheiro"] = dataset["tamanho"].apply (categorizar)
#Visualizar os valores da nova coluna:
dataset["categoria_banheiro"]

#Importar a biblioteca Pandas:
import pandas as pd
#Visualizar o "DataFrame":
dataset.head ()

#Importar a biblioteca Pandas:
import pandas as pd
#Visualizar os valores da coluna original e da nova coluna:
dataset[["tamanho", "categoria_banheiro"]]

#Importar a biblioteca Pandas:
import pandas as pd
#Visualizar a distribuição de valores da nova coluna, mostrando a quantidade de valores únicos em cada categoria criada:
dataset.categoria_banheiro.value_counts ()

"""# **Remoção**

**Remoção** **de** **Colunas**
"""

#Importar a biblioteca Pandas:
import pandas as pd
dataset.drop (["categoria_banheiro"], axis = 1, inplace = True)
dataset.drop (["tamanho"], axis = 1, inplace = True)
dataset.head ()

"""**Remoção** **de** **Linhas**"""

#Importar a biblioteca Pandas:
import pandas as pd
#Remover linhas com "bedrooms" = 0 e "bedrooms" > 30
dataset.drop (dataset[dataset.bedrooms == 0].index, inplace = True)
dataset.drop (dataset[dataset.bedrooms > 30].index, inplace = True)
dataset

#Importar a biblioteca Pandas:
import pandas as pd
#Visualizar o menor valor da coluna "bedrooms":
print ("Menor valor da coluna bedrooms:")
dataset.bedrooms.min ()

#Importar a biblioteca Pandas:
import pandas as pd
#Visualizar o maior valor da coluna "bedrooms";
print ("Maior valor da coluna bedrooms:")
dataset.bedrooms.max ()

"""# **Exercício**

# **Carregamento**
"""

#Carregamento do dataset:
from google.colab import files
src = list (files.upload ().values ())[0]
open ("datasets_549702_1268340_brazil_covid19.csv", "wb").write (src)

"""# **Uso**"""

import pandas as pd

covid19 = pd.read_csv ("datasets_549702_1268340_brazil_covid19.csv", sep = ",")
print (type (dataset))
covid19.head ()

"""1. Crie uma nova coluna no "DataFrame" com o nome "categoria_casos". Defina uma
função para categorizar o número de casos de COVID-19 no Brasil e preencher os
registros dessa nova coluna. A função deve classificar o número de casos da seguinte
forma:
 Se o número de casos for maior ou igual a 20.000: estado de emergência.
 Se o número de casos for maior ou igual a 5.000: estado de alerta.
 Caso contrário: estado de normalidade.
Apresente o "DataFrame" resultante no notebook.
"""

#Importar a biblioteca Pandas:
import pandas as pd
#Definição da função que será usada na geração dos valores para a novacoluna:
def categorizar (casos):
 if casos >= 20000:
  return "Estado de emergência"
 elif casos >= 5000:
  return "Estado de alerta"
 else:
  return "Estado de normalidade"
#Criar uma nova coluna no "DataFrame" e aplicar função definida acima:
covid19["categoria_casos"] = covid19["cases"].apply (categorizar)
#Visualizar os valores da nova coluna:
covid19[["cases", "categoria_casos"]]

"""2. Crie uma nova coluna no "DataFrame" com o nome "categoria_mortes". Defina uma
função para categorizar o número de mortes por COVID-19 no Brasil e preencher os
registros dessa nova coluna. A função deve classificar o número de mortes da
seguinte forma:
 Se o número de mortes for maior ou igual a 20.000: estado de sítio.
 Se o número de mortes for maior ou igual a 15.000: estado de calamidade pública.
 Se o número de mortes for maior ou igual a 11.000: estado de emergência.
 Se o número de mortes for maior ou igual a 5.000: estado de alerta.
 Caso contrário: estado de normalidade.
Apresente o "DataFrame" resultante no notebook.
"""

#Importar a biblioteca Pandas:
import pandas as pd
#Definição da função que será usada na geração dos valores para a novacoluna:
def categorizar (mortes):
 if mortes >= 20000:
  return "Estado de sítio"
 elif mortes >= 15000:
  return "Estado de calamidade pública"
 elif mortes >= 11000:
   return "Estado de emergência"
 elif mortes >= 5000:
   return "Estado de alerta"
 else:
  return "Estado de normalidade"
#Criar uma nova coluna no "DataFrame" e aplicar função definida acima:
covid19["categoria_mortes"] = covid19["deaths"].apply (categorizar)
#Visualizar os valores da nova coluna:
covid19[["cases", "categoria_casos", "deaths", "categoria_mortes"]]