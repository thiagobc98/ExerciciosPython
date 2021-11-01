# -*- coding: utf-8 -*-
"""ADSTI_EX16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FVz20rFsx1iLO03QfAbe2RE7n8OKJ18q
"""

from google.colab import files
src = list (files.upload ().values ())[0]
open ("kc_house_data.csv", "wb").write (src)

import pandas as pd
dataset = pd.read_csv ("kc_house_data.csv", sep = ",")
dataset.info()

import pandas as pd
print(dataset)

"""# **Método head()**

O método "head ()" de um "DataFrame" permite que vejamos alguns de seus registros
iniciais, em geral, as 5 primeiros registros. 
O método "head ()" permite que especifiquemos como argumento o número de registros a
serem apresentados.
"""

import pandas as pd
dataset = pd.read_csv ("kc_house_data.csv", sep = ",")
dataset.head (7)

"""# **Metodo LOC[]**

Podemos filtrar registros usando o atributo "loc[]". O atributo "loc[]" recebe uma expressão
para realizar a filtragem.
"""

import pandas as pd
dataset = pd.read_csv ("kc_house_data.csv", sep = ",")
dataset.loc[dataset["bedrooms"] > 7]

"""# **UNIQUE()**

O método "unique ()" permite retornar registros únicos do "DataFrame".
"""

#Identificadores sem repetições:
import pandas as pd
dataset = pd.read_csv ("kc_house_data.csv", sep = ",")
dataset.id.unique ()

#Quartos sem repetições:
import pandas as pd
dataset = pd.read_csv ("kc_house_data.csv", sep = ",")
dataset.bedrooms.unique ()

"""# **count ()**

O método "count ()" permite que calculemos o número total de registros (número de linhas)
do "DataFrame" considerando cada coluna ou uma coluna específica.
"""

#Número total de registros do DataFrame considerando cada coluna:
import pandas as pd
dataset = pd.read_csv ("kc_house_data.csv", sep = ",")
dataset.count ()

#Número total de registros do DataFrame considerando a coluna bedrooms:
import pandas as pd
dataset = pd.read_csv ("kc_house_data.csv", sep = ",")
dataset.bedrooms.count ()

"""# **mean ()**

O método "mean ()" permite que calculemos a média aritmética dos valores de cada coluna
do "DataFrame" ou de uma coluna específica.
"""

#Média aritmética de cada coluna:
import pandas as pd
dataset = pd.read_csv ("kc_house_data.csv", sep = ",")
dataset.mean ()

#Média aritmética do número de quartos:
import pandas as pd
dataset = pd.read_csv ("kc_house_data.csv", sep = ",")
dataset.bedrooms.mean ()

"""# **Columns**

O atributo "columns" armazena o nome das colunas do "DataFrame".
"""

#Nome das colunas:
import pandas as pd
dataset = pd.read_csv ("kc_house_data.csv", sep = ",")
dataset.columns

"""# **describe()**

O método "describe ()" retorna informação estatística sobre o "DataFrame" considerando
cada coluna separadamente, como número de registros, média aritmética, desvio padrão,
valor mínimo, quartis e valor máximo. O método considera apenas as colunas com valores
núméricos. Colunas com valores não numéricos são descartadas da análise estatística.
"""

#Informação estatística sobre o DataFrame:
import pandas as pd
dataset = pd.read_csv ("kc_house_data.csv", sep = ",")
dataset.describe ()

"""# **Exercício**

# **Carregamento**
"""

from google.colab import files
src = list (files.upload ().values ())[0]
open ("brazil_covid19.csv", "wb").write (src)

"""1. Quantas colunas o "data set" possui?"""

import pandas as pd
dataset = pd.read_csv ("brazil_covid19.csv", sep = ",")
dataset.count

"""2. Quais são os nomes e tipos das colunas do "data set"?"""

import pandas as pd
dataset = pd.read_csv ("brazil_covid19.csv", sep = ",")
dataset.columns

"""3. Quantas entradas, linhas, o "data set" possui?"""

import pandas as pd
dataset = pd.read_csv ("brazil_covid19.csv", sep = ",")
dataset.count()

"""4. Qual o espaço de memória ocupado pelo "data set"?"""

import pandas as pd
dataset = pd.read_csv ("brazil_covid19.csv", sep = ",")
dataset.count()

"""5. Quais são as 10 primeiras linhas do "data set"?"""

import pandas as pd
dataset = pd.read_csv ("brazil_covid19.csv", sep = ",")
dataset.head(10)

"""6. Quantas entradas do "data set" reportam mais de 1.000 casos confirmados da COVID-19?"""

import pandas as pd
dataset = pd.read_csv ("brazil_covid19.csv", sep = ",")
dataset.loc[dataset["cases"] > 1000]

"""7. Quantas entradas do "data set" reportam mais de 2.000 mortes por COVID-19?"""

import pandas as pd
dataset = pd.read_csv("brazil_covid19.csv", sep = ",")
dataset.loc[dataset["deaths"] > 2000]

"""8. Quais são as regiões reportadas no "data set"? Apresentar cada região de forma única."""

import pandas as pd
dataset = pd.read_csv ("brazil_covid19.csv", sep = ",")
dataset.region.unique ()

"""9. Quais são os estados reportados no "data set"? Apresentar cada estado de forma única."""

import pandas as pd
dataset = pd.read_csv ("brazil_covid19.csv", sep = ",")
dataset.state.unique ()

"""10. Quais são os registros em que o estado é Minas Gerais? Quantos são esses registros?"""

import pandas as pd
dataset = pd.read_csv("brazil_covid19.csv", sep = ",")
dataset.loc[dataset["state"] == "Minas Gerais"]

"""11. Quantos são os registros em que a região é Norte?"""

import pandas as pd
dataset = pd.read_csv("brazil_covid19.csv", sep = ",")
dataset.loc[dataset["region"] == "Norte"]

"""12. Qual é o número médio de casos de infecção por COVID-19 reportados no "data set"?"""

import pandas as pd
dataset = pd.read_csv ("brazil_covid19.csv", sep = ",")
dataset.cases.mean ()

"""13. Qual é o número médio de mortes por COVID-19 reportados no "data set"?"""

import pandas as pd
dataset = pd.read_csv ("brazil_covid19.csv", sep = ",")
dataset.deaths.mean ()

"""14. Qual é o número máximo de casos de infecção por COVID-19 reportados no "data set"?"""

import pandas as pd
dataset = pd.read_csv ("brazil_covid19.csv", sep = ",")
dataset.cases.max ()

"""15. Qual é o número máximo de mortes por COVID-19 reportados no "data set"?"""

import pandas as pd
dataset = pd.read_csv ("brazil_covid19.csv", sep = ",")
dataset.deaths.max ()

"""16. A partir de qual quartil (Q1 = 25%, Q2 = 50% e Q3 = 75%) o número de casos de infecção
por COVID-19 é maior que zero?
"""

import pandas as pd
dataset = pd.read_csv ("brazil_covid19.csv", sep = ",")
dataset.cases.describe()

"""17. A partir de qual quartil (Q1 = 25%, Q2 = 50% e Q3 = 75%) o número de mortes por COVID19 é maior que zero?"""

import pandas as pd
dataset = pd.read_csv ("brazil_covid19.csv", sep = ",")
dataset.deaths.describe()