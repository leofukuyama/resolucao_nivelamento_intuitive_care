CREATE DATABASE operadoras_ativas_ans;

USE operadoras_ativas_ans;

CREATE TABLE dados_ativos (
    Registro_ANS INT,
    CNPJ VARCHAR(14),
    Razao_Social VARCHAR(255),
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(100),
    Logradouro VARCHAR(255),
    Numero VARCHAR(10),
    Complemento VARCHAR(255),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    UF CHAR(2),
    CEP VARCHAR(8),
    DDD CHAR(2),
    Telefone VARCHAR(15),
    Fax VARCHAR(15),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(100),
    Regiao_de_comercializacao INT,
    Data_Registro_ANS DATE
);

LOAD DATA LOCAL INFILE 'C:\\DockerContainers\\Relatorio_cadop.csv'
INTO TABLE dados_ativos
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
