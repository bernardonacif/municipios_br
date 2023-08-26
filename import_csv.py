import csv
import mysql.connector
import time

# Configurações do banco de dados MySQL
config = {
    'user': 'bernardo_root_01',
    'password': 'kirbis-deNgyw-0monge',
    'host': 'db4free.net',
    'port': '3306',    
    'raise_on_warnings': True
}

arquivo_csv = './/br_uf_infos_no_carac.csv'

print("Abrindo o arquivo CSV...")
# Abre o arquivo CSV e realiza a leitura dos dados
with open(arquivo_csv, 'r', newline='', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo, delimiter=';')
    
    print("Conectando ao banco de dados...")
    # Percorre as linhas do arquivo CSV e insere os dados no banco de dados
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    query = "INSERT INTO financialdb001.br_citys_ibge_info (cod_uf, cod_localidade, cod_municipio, uf, municipio, regiao, porte, capital) " \
            "VALUES (%(cod_uf)s, %(cod_localidade)s, %(cod_municipio)s, %(uf)s, %(municipio)s, %(regiao)s, %(porte)s, %(capital)s)"
    
    batch_size = 1000  # Número de inserções por lote
    batch = []
    total_inserted = 0

    print("Inserindo dados no banco de dados...")
    start_time = time.time()
    for linha in leitor_csv:
        batch.append(linha)
        
        if len(batch) >= batch_size:
            cursor.executemany(query, batch)
            conn.commit()
            total_inserted += len(batch)
            batch = []
            print(f"Inseridos {total_inserted}...")

    if batch:
        cursor.executemany(query, batch)
        conn.commit()
        total_inserted += len(batch)
        print(f"Inseridos {total_inserted} registros ao final.")

    cursor.close()
    conn.close()

end_time = time.time()
processing_time = end_time - start_time
print(f'Processo concluído: {total_inserted} registros inseridos.')
print(f'Tempo total de processamento: {processing_time:.2f} segundos.')
