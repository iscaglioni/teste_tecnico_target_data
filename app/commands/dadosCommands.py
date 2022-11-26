
import csv
import click
from extensions.database import database
from flask import Blueprint

empresasCommands = Blueprint('empresas', __name__)

limite_de_dados = 7


@empresasCommands.cli.command('import')
@click.argument()
def dados_empresas(): 
    # instanciando conexao do pymongo 
    db = database()
    # criando collection empresas
    db_empresas = db['empresas']   
    lista_empresas = []
     # criando variavel para poder acessar o arquivo csv
    arquivo_empresas = csv.reader(open('empresas9.csv'),delimiter=';')
    
    # loop para percorrer o arquivo csv 
    for index, empresas in enumerate(arquivo_empresas):        
        # condicional para extrair somente 100k de linhas
        if index == limite_de_dados:
            break
        # armazenando dados em um dicionario pelo valor do cnpj
        lista_empresas.append(
            {   
                'cnpj básico': empresas[0],       
                'razão social': empresas[1],
                'natureza jurídica': empresas[2],
                'qualificação do responsável': empresas[3],
                'capital social': empresas[4],
                'porte da empresa': empresas[5],
                'ente federativo': empresas[6]
            }
        )          
    # inserindo lista_empresas no banco de dicionario_empresas
    db_empresas.insert_many(lista_empresas)        
    # print(lista_empresas)     




# @dadosCommands.cli.command('import')
# @click.argument('csvfile')
# def import_csv(csvfile):
#     collection = database.dados
#     data = pd.read_csv(csvfile)
#     jsondata = json.load(data.to_json(orient='records'))
#     collection.insert(jsondata)
#     return collection.count