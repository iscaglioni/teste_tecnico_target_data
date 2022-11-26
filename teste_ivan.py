import csv
from app.extensions.database import database

#definicao de 100k resultados 
limite_de_dados = 100000

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
  

def dados_socios():
    dados = {}
    # criando variavel para acessar o arquivo csv socios]
    arquivo_socios = csv.reader(open('socios9.csv'),delimiter=';')
    # loop para percorrer o arquivo cvs
    for index, socios in enumerate(arquivo_socios):

        # condicional para extrtair somente 100k de linhas
        if index == limite_de_dados:
            break
        # armazenamento dos dados em um dicionario
        dicionario_socios = dict(
            {
                'cnpj básico': socios[0],
                'identificador de sócio': socios[1],
                'nome do sócio ou razão social': socios[2],
                'cnpj/ cpf do sócio': socios[3],
                'qualificação do sócio': socios[4],
                'data de entrada na sociedade': socios[5],
                'país': socios[6],
                'representante legal': socios[7],
                'nome do representante': socios[8],
                'qualificação do representante': socios[9],
                'faixa etária': socios[10]
            }
        )
        # print(dicionario_socios)


def dados_estabelecimentos():    
    dados = {}
    # criando variavel para poder acessar o arquivo csv
    arquivo_estabelecimentos = csv.reader(open('estabelecimentos9.csv'), delimiter=';')
    # loop para percorrer o arquivo csv
    for index, estabelecimentos in enumerate(arquivo_estabelecimentos):
        
        # condicional para extrair somente 100k de linhas 
        if index == limite_de_dados:
            break
        # armazenamento de dados em um dicionario
        dicionario_estabelecimentos = dict(
            {
                'cnpj básico':estabelecimentos[0],
                'cnpj ordem': estabelecimentos[1],
                'cnpj DV': estabelecimentos[2],
                'idenfificador matriz / filial': estabelecimentos[3],
                'nome fantasia': estabelecimentos[4],
                'situação cadastral': estabelecimentos[5],
                'data situação cadastral': estabelecimentos[6],
                'motivo situação cadastral': estabelecimentos[7],
                'nome da cidade no exterior': estabelecimentos[8],
                'país': estabelecimentos[9],
                'data de início de atividade': estabelecimentos[10],
                'CNAE fiscal principal': estabelecimentos[11],
                'CNAE fiscal secundária': estabelecimentos[12],
                'tipo de logradouro': estabelecimentos[13],
                'logradouro': estabelecimentos[14],
                'número': estabelecimentos[15],
                'complemento': estabelecimentos[16],
                'bairro': estabelecimentos[17],
                'cep': estabelecimentos[18],
                'uf': estabelecimentos[19],
                'município': estabelecimentos[20],
                'DDD1': estabelecimentos[21],
                'telefone 1': estabelecimentos[22],
                'DDD2': estabelecimentos[23],
                'telefone 2': estabelecimentos[24],
                'DDD do fax': estabelecimentos[25],
                'fax': estabelecimentos[26],
                'correio eletrônico': estabelecimentos[27],
                'situação especial': estabelecimentos[28],
                'data da situação especial': estabelecimentos[29]
            }
        )
    print(dicionario_estabelecimentos)

# puxar as 3 tabelas e depois  pegar o filtro e juntar 