# Documentação Detalhada

## Introdução

Este é um projeto que visa criar um site simples utilizando Flask, um framework web em Python. A documentação detalhada abaixo descreve cada parte do projeto em detalhes.

## Estrutura de Pastas

O projeto segue a seguinte estrutura de pastas:
```
seu_projeto/
    app.py
    database.py
    models.py
    .flaskenv
    Procfile
    templates/
        index.html
        sobre.html
        contato.html
    static/
        css/
            style.css
        js/
            script.js
        img/
            imagem.png
    README.md
```
## Pastas de Conteúdo

### Pasta `templates`

#### Arquivos HTML

A pasta `templates/` contém os arquivos HTML para cada página do site:

- `index.html`: Página inicial.
- `sobre.html`: Página "Sobre nós".
- `contato.html`: Página de contato.

### Pasta `static`

#### Arquivos Estáticos

A pasta `static/` armazena arquivos estáticos utilizados para estilização e interação das páginas:

- `css/`: Arquivos CSS para estilização.
- `js/`: Arquivos JavaScript para interatividade.
- `img/`: Imagens utilizadas no site.

## Arquivos Principais

### `app.py`

Este é o arquivo principal da aplicação, onde são definidas as rotas e a lógica principal do aplicativo. Nele, são mapeadas as URLs para funções específicas que renderizam as páginas ou processam dados. [Veja aqui](https://github.com/lukebgds/TecnologyWay_Python-Flask/blob/main/app.py)

### `database.py` e `models.py`

Esses arquivos são responsáveis pela interação com o banco de dados. [`database.py`](https://github.com/lukebgds/TecnologyWay_Python-Flask/blob/main/database.py) geralmente configura e inicializa o SQLAlchemy, enquanto [`models.py`](https://github.com/lukebgds/TecnologyWay_Python-Flask/blob/main/models.py) define a estrutura das tabelas do banco de dados usando SQLAlchemy, incluindo os modelos de dados.

### `.flaskenv`

O arquivo [`.flaskenv`](https://github.com/lukebgds/TecnologyWay_Python-Flask/blob/main/.flaskenv) é usado para configurar o ambiente do Flask. Nele, você pode definir variáveis de ambiente específicas do Flask, como a configuração da aplicação (`FLASK_APP`) e a chave secreta (`SECRET_KEY`), entre outras. 

### `Procfile`

O arquivo [`Procfile`](https://github.com/lukebgds/TecnologyWay_Python-Flask/blob/main/Procfile) é crucial para a implantação do aplicativo no Heroku. Ele especifica o processo web a ser executado usando Gunicorn para garantir a correta execução da aplicação no ambiente de hospedagem. 

## Funcionalidades Principais

### `app.py`

#### Rotas

`app.py` define as rotas, que são URLs específicas que a aplicação responde. Cada rota pode estar associada a uma função que renderiza um template HTML ou executa uma ação específica.

#### Lógica para Inscrição de Usuários

Além das rotas, `app.py` pode conter a lógica para lidar com a inscrição de usuários. Por exemplo, um método `POST` para receber e processar dados de um formulário de inscrição.

### `database.py` e `models.py`

#### `database.py`

Esse arquivo geralmente contém a configuração e inicialização do SQLAlchemy, que é uma biblioteca de ORM (Object-Relational Mapping) usada para interagir com o banco de dados.

#### `models.py`

`models.py` é onde você define a estrutura das tabelas do banco de dados utilizando SQLAlchemy, criando os modelos de dados e suas relações.

## Uso do Flask-Migrate

#### Inicialização e Criação de Migração

Para começar a utilizar o Flask-Migrate, os seguintes comandos devem ser executados para inicializar e criar a primeira migração:

```bash
flask db init  # Inicializa a estrutura de migração
flask db migrate -m "Nome da migração"  # Cria uma nova migração
flask db upgrade  # Aplica a migração ao banco de dados 
```
Esses comandos ajudam a gerenciar as migrações do banco de dados, refletindo as alterações no esquema do banco de dados de maneira controlada e organizada

## Estrutura de Diretórios Gerados

Após a inicialização e criação das migrações, o Flask-Migrate cria dois diretórios adicionais no seu projeto:

### `migrations/`

O diretório `migrations/` armazena todos os arquivos relacionados às migrações do banco de dados. Isso inclui os arquivos de migração Python, responsáveis por descrever as alterações no esquema do banco de dados.

### `instance/`

O diretório `instance/` é usado para armazenar dados sensíveis ou específicos de uma instância do aplicativo. É comum armazenar chaves secretas ou configurações específicas que não devem ser versionadas no controle de código fonte.

## Gerenciamento de Pacotes Python

### `pip freeze` e `requirements.txt`

O `pip` é uma ferramenta para instalar e gerenciar pacotes Python. O comando `pip freeze` é usado para listar todos os pacotes instalados no ambiente virtual. Essa listagem inclui os nomes e versões de todos os pacotes Python instalados.

#### Criação do `requirements.txt`

O `requirements.txt` é um arquivo de texto que contém uma lista dos pacotes Python instalados em um ambiente virtual. Ele é frequentemente utilizado para compartilhar e reproduzir um ambiente Python específico. Para criar um `requirements.txt`, basta executar o comando:

```bash
pip freeze > requirements.txt
```
## Estrutura de Arquivos do Projeto Finalizada:
```
seu_projeto/
    migrations/
    instance/
    static/
        css/
            style.css
        js/
            script.js
        img/
            imagem.png
    templates/
        index.html
        sobre.html
        contato.html        
    .flaskenv    
    app.py
    database.py
    models.py
    Procfile
    README.md
    requirements.txt
```
## Conclusão

O projeto foi desenvolvido com base no framework Flask para criação de um site simples. Ele inclui uma estrutura básica para lidar com rotas, renderização de páginas HTML, interação com um banco de dados SQLite utilizando SQLAlchemy e gerenciamento de migrações com Flask-Migrate.

Com a organização de diretórios para armazenamento de templates HTML, arquivos estáticos e a utilização do Flask-Migrate para gerenciar as migrações do banco de dados, este projeto serve como um exemplo didático para quem está iniciando no desenvolvimento web com Flask.

A utilização do `requirements.txt` para documentar os pacotes Python instalados, juntamente com uma breve explicação sobre a sua criação por meio do comando `pip freeze`, oferece uma maneira padronizada de compartilhar o ambiente de desenvolvimento e garantir a reprodução consistente do projeto em diferentes ambientes.

Agradecimentos especiais aos consultores **[Eduardo Negri e Rodin Sarmento]** por contribuirem com esse projeto.

Fique à vontade para explorar e utilizar este projeto como base para desenvolvimentos futuros!

## Autor

**Lucas Benício Gusmão da Silva**

Idealizador, criador e desenvolvedor deste projeto.

Todos os direitos reservados:

[![Licença](https://img.shields.io/badge/Licença-MIT-blue)](https://github.com/lukebgds/TecnologyWay_Python-Flask/blob/main/LICENSE)

---

#### [Voltar ao topo](#seu-projeto)