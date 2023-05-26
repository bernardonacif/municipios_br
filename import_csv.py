import csv
import mysql.connector

# Configurações do banco de dados MySQL - insira a credenciais do seu bd aqui:
config = {
    'user': '',
    'password': '',
    'host': '',
    'port': '',    
    'raise_on_warnings': True
}

# Nome do arquivo CSV a ser lido
arquivo_csv = './/br_uf_infos_no_carac.csv' # inserir o local do arquivo

# Abre o arquivo CSV e realiza a leitura dos dados
with open(arquivo_csv, 'r', newline='', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo, delimiter=';')
    
    # Ignora o cabeçalho do arquivo CSV
    next(leitor_csv)
    
    # Percorre as linhas do arquivo CSV e insere os dados no banco de dados
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    query = "INSERT INTO accu_weather.br_citys_ibge_info (cod_uf, cod_localidade, cod_municipio, uf, municipio, regiao, porte, capital) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    
    for linha in leitor_csv:
        cod_uf = linha[0]
        cod_localidade = linha[1]
        cod_municipio = linha[2]
        uf = linha[3]
        municipio = linha[4]
        regiao = linha[5]
        porte = linha[6]
        capital = linha[7]
        cursor.execute(query, (cod_uf, cod_localidade, cod_municipio, uf, municipio, regiao, porte, capital))
        
        # Chama a função para inserir os dados no banco de dados
        # inserir_dados(cod_localidade, cod_municipio, uf, municipio, regiao, porte, capital)
    conn.commit()
    cursor.close()
    conn.close()
print('Dados inseridos no banco de dados.')
