import csv
import pymongo

#definicao de 100k resultados 
limite_de_dados = 100000


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

