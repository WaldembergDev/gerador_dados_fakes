from faker import Faker
import re
import csv
import io
import pandas as pd

def dividir_endereco(endereco: str):
    lista_endereco = endereco.split('\n')
    logradouro = lista_endereco[0]
    bairro = lista_endereco[1]

    padrao_cep = re.compile(r'\d{5}-?\d{3}')
    padrao_cidade = re.compile(r'([a-zA-Z]+\s?)+')
    padrao_uf = re.compile(r'[A-Z]{2}')

    cidade = padrao_cidade.search(lista_endereco[2]).group()
    cep = padrao_cep.search(lista_endereco[2]).group()
    uf = padrao_uf.search(lista_endereco[2]).group()

    return logradouro, bairro, cep, cidade, uf

def dict_opcoes():
    fake = Faker('pt_BR')
    endereco = dividir_endereco(fake.address()) 

    opcoes = {'Nome': fake.name(),
              'Primeiro_nome': fake.first_name(),
              'Ultimo_nome': fake.last_name(),
              'Data_nascimento': fake.date_of_birth(),
              'CPF': fake.cpf(),
              'RG': fake.rg(),
              'Endereco': endereco[0],
              'cep': endereco[2],
              'Cidade': endereco[3],
              'telefone': fake.phone_number(),
              'cod_departamento': fake.random_int(1, 5),
              'Funcao': fake.profile().get('job'),
              'Salario': fake.random_int(1420, 12000)}
    
    return opcoes


def selecionar_fake(opcao: str):
    #Gerando o dicionário com todas as opções
    opcoes = dict_opcoes()
    return opcoes.get(opcao)
    

def gerar_csv(qnt_linhas: int, colunas: list):
    with open('dados_fake.csv', 'w', newline='', encoding='utf-8') as arquivo:
        arquivo_csv = csv.writer(arquivo)
        #Inserindo as colunas no arquivo
        arquivo_csv.writerow(colunas)
        #Gerando os valores fictícios
        for linha in range(qnt_linhas):
            valores = map(selecionar_fake, colunas)
            arquivo_csv.writerow(valores)

def gerar_csv_memoria(qnt_linhas: int, colunas: list):
    output = io.StringIO()
    arquivo_csv = csv.writer(output)
    # Inserindo as colunas no arquivo
    arquivo_csv.writerow(colunas)
    # Gerando os valores fictícios
    for linha in range(qnt_linhas):
        valores = map(selecionar_fake, colunas)
        arquivo_csv.writerow(valores)
    df = pd.read_csv(io.StringIO(output.getvalue()))
    return df