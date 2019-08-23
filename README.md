# Desafio 2xt

Esse projeto deve ser executado com **Python 3.6+** e foi desenvolvido utilizando **Python 3.7.3**.

## Configuração

Primeiramente é necessária a instalação das dependências do projeto. Isso pode ser feito executando o comando:
``pip install -r requirements.txt``

Também é necessário a inicialização de um banco de dados **PostgreSQL** através dos comandos:
```sudo -u postgres psql ``` 
``` 
CREATE DATABASE mysite;
CREATE USER mysiteuser WITH PASSWORD 'mysite_pass';
ALTER ROLE mysiteuser SET client_encoding TO 'utf8';
ALTER ROLE mysiteuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE mysiteuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE mysite TO mysiteuser;
ALTER USER mysiteuser CREATEDB;
```

Após isso, é necessário inserir as migrações do projeto no banco de dados recém criado, para isso, na pasta raiz do projeto execute:
```
python3 manage.py migrate
```

## Execução

Para executar o projeto, na pasta raiz do mesmo, execute:
```
python3 manage.py runserver
```
Em seguida acessar a página através do endereço http://localhost:8000

## Melhorias

 - Implementação de testes unitários para melhorar a cobertura
 - Remoção de valores definidos diretamente no código (Hardcoded)
 - Alinhamento de quais dados são necessários no banco de dados do projeto ao se efetuar uma compra
 - Definição de dados a serem cacheados para melhorar o tempo de resposta
 - Adição de loading durante o carregamento/processamento da solicitações
 - Melhor forma de inserir a data de aniversário dos segurados, já que atualmente é necessário digitar o formato _(dd/mm/aaaa)_ diretamente, ou navegar pelo calendário até a data desejada
 - Melhorias gerais de interface
