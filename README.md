# Dados das Unidades Federativas do Brasil
- Este repositório contém informações básicas sobre as Unidades Federativas (UFs) do Brasil.

## Estrutura do Repositório
-> br_uf_infos_no_carac.csv: Arquivo CSV contendo os dados das UFs do Brasil.

O br_uf_infos_no_carac.csv contém os seguintes campos para cada UF:
- cod_uf: Código da Unidade Federativa
- cod_localidade: Código da localinade
- cod_municipio: Código do municópio
- uf: Unidade Federativa
- municipio: Nome do municipio
- regiao: Região do município
- porte: Porte do município
- capital: Se é capital ou não (Sim/Nao)


-> uf_br.sql: Script SQL (MySql) para criar uma tabela no banco de dados com os dados das UFs do Brasil.

-> import_csv.py: Script Python (3.9) para criar uma tabela no banco de dados MySql a partir dos dados das UFs do Brasil.

## Execução de scripts

- Python: Ajustar local do arquivo a ser importado e inserir suas configurações do banco Mysql
- Sql: Conectar ao banco MySql e executar o script
