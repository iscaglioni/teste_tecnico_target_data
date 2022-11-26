import csv
import pandas as pd

limite_de_dados =100000

# criando um dataframe com panda
df = pd.read_csv('empresas9.csv', sep = ';', nrows = limite_de_dados )

# transformando dataframe em dicionario
dicionario_empresas =  df.to_dict()

# print(dicionario_empresas)
# print(df)



# def dicReader():
#     with open('empresas9.csv', 'r') as f:
#         dict_reader = DictReader(f)
#         list_of_dict = list(dict_reader)
#         print(list_of_dict)