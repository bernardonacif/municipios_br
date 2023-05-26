USE ;--inserir seu banco de dados

CREATE TABLE IF NOT EXISTS br_citys_ibge_info (
cod_uf VARCHAR(2),
cod_localidade VARCHAR(6),
cod_municipio VARCHAR(7),
uf VARCHAR(2),
municipio VARCHAR(50),
regiao VARCHAR(20),
porte VARCHAR(20),
capital VARCHAR(3)
);
