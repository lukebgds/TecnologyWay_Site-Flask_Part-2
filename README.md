# Site_Flask - Guia Prático(Part-2): Implementação do Framework Flask, com Deploy(Heroku)

## Introdução

Bem-vindo ao guia prático para a criação de um site simples com Flask, um poderoso framework web em Python. Este projeto foi elaborado para proporcionar uma visão detalhada de cada etapa do desenvolvimento, desde a configuração inicial de um site básico com deploy, passando pela implementação do Framework, até finalizar com o deploy na plataforma Heroku.

***Nesta segunda parte do projeto*** ``"Site_Flask - Mini Tutorial"``, mergulharemos na criação de um website básico, utilizando as poderosas ferramentas disponíveis no framework Flask. Este tutorial oferece um roteiro passo a passo para compreender a estrutura fundamental do Flask e suas capacidades.

Ao seguir as instruções detalhadas abaixo, você terá a oportunidade não apenas de explorar a estrutura do Flask, mas também de aprender como criar rotas, integrar templates HTML, interagir com um banco de dados e, por fim, realizar o deploy na nuvem através da plataforma Heroku.

Este repositório foi desenvolvido para fornecer os recursos e orientações necessárias para compreender e aplicar os recursos robustos oferecidos pelo Flask no desenvolvimento de um website. Prepare-se para mergulhar na criação de um site dinâmico e funcional com Flask, culminando com seu lançamento na nuvem através do Heroku.

### Recomendação da IDE: PyCharm

Durante o desenvolvimento do projeto, recomendo o uso do PyCharm como a IDE (Integrated Development Environment) para trabalhar com o Flask e Python de forma eficiente e produtiva.

## Estrutura de Pastas

O projeto segue a seguinte estrutura de pastas:
```
seu_projeto/
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

[`app.py`](https://github.com/lukebgds/TecnologyWay_Site-Flask_Part-2/blob/main/app.py) é o arquivo principal da aplicação, onde são definidas as rotas e a lógica principal do aplicativo. Nele, são mapeadas as URLs para funções específicas que renderizam as páginas ou processam dados. 

### `database.py` e `models.py`

Esses arquivos são responsáveis pela interação com o banco de dados. [`database.py`](https://github.com/lukebgds/TecnologyWay_Python-Flask/blob/main/database.py) geralmente configura e inicializa o SQLAlchemy, enquanto [`models.py`](https://github.com/lukebgds/TecnologyWay_Python-Flask/blob/main/models.py) define a estrutura das tabelas do banco de dados usando SQLAlchemy, incluindo os modelos de dados.

### `.flaskenv`

O arquivo [`.flaskenv`](https://github.com/lukebgds/TecnologyWay_Python-Flask/blob/main/.flaskenv) é usado para configurar o ambiente do Flask. Nele, você pode definir variáveis de ambiente específicas do Flask, como a configuração da aplicação (`FLASK_APP`) e a chave secreta (`SECRET_KEY`), entre outras. 

### `Procfile`

O arquivo [`Procfile`](https://github.com/lukebgds/TecnologyWay_Python-Flask/blob/main/Procfile) é crucial para a implantação do aplicativo em sites de hospedagem. Ele especifica o processo web a ser executado usando Gunicorn para garantir a correta execução da aplicação no ambiente de hospedagem. 

## Funcionalidades Principais

### `app.py`

#### Rotas

O arquivo `app.py` é crucial para a definição das rotas da aplicação. Essas rotas são URLs específicas que a aplicação Flask responde. Em cada rota, é possível associar uma função que renderiza um template HTML correspondente ou executa uma ação específica, como processar dados de um formulário ou interagir com o banco de dados.

#### Lógica para Inscrição de Usuários

Além de mapear as rotas, `app.py` pode conter a lógica para lidar com a inscrição de usuários. Isso geralmente inclui a implementação de um método `POST` que recebe dados de um formulário de inscrição HTML. Esses dados são processados, validados e, se válidos, são armazenados no banco de dados. 

No código fornecido, a lógica para inscrição de usuários inclui:

- Validação do formato do e-mail usando a função `validate_email()` de uma biblioteca externa.
- Verificação do domínio do e-mail para garantir que seja válido, consultando registros MX usando a biblioteca `dns.resolver`.
- Interatividade com o banco de dados através do SQLAlchemy (`db`), verificando se o e-mail já está cadastrado e adicionando-o se não estiver.

Esses pontos demonstram como o `app.py` pode ser usado não apenas para definir rotas, mas também para implementar ações específicas com base nas requisições dos usuários, como a inscrição no exemplo fornecido.

### `database.py` e `models.py`

#### `database.py`

O arquivo `database.py` geralmente abriga a configuração inicial do SQLAlchemy. Essa configuração pode incluir a criação de uma instância do SQLAlchemy (`db`) e a definição de parâmetros cruciais, como a conexão com o banco de dados, configurações do pool de conexões, entre outros. O SQLAlchemy é uma biblioteca ORM poderosa que simplifica a interação com bancos de dados relacionais por meio de objetos Python.

#### `models.py`

No arquivo `models.py`, você define os modelos de dados para sua aplicação. Esses modelos são representações das tabelas do banco de dados como classes em Python, onde cada atributo da classe corresponde a uma coluna na tabela. Além disso, é nesse arquivo que você estabelece os relacionamentos entre diferentes tabelas, como chaves estrangeiras e associações.

Por exemplo, você pode ter classes representando entidades específicas, como `Usuário`, `Produto` ou `Pedido`, e definir seus atributos correspondentes, como nome, ID ou descrição. Além disso, é onde você pode usar as funcionalidades do SQLAlchemy para criar relações entre essas entidades, como um `Pedido` que está associado a um `Usuário` ou que contém vários `Produtos`.

Os arquivos `database.py` e `models.py` trabalham em conjunto para permitir a criação de estruturas de dados flexíveis e bem organizadas, que são refletidas no banco de dados através do SQLAlchemy.

## Uso do Flask-Migrate

### Migrações em Bancos de Dados

Em desenvolvimento de software, especialmente quando lidamos com bancos de dados, migrações são alterações na estrutura ou no esquema do banco de dados ao longo do tempo. Essas alterações podem incluir a adição de novas tabelas, a modificação de colunas existentes, a exclusão de tabelas ou até mesmo a criação de relacionamentos entre tabelas.

Quando um aplicativo está em desenvolvimento contínuo, as alterações na estrutura do banco de dados são inevitáveis. Gerenciar essas mudanças de forma eficiente e controlada é fundamental para manter a integridade dos dados e evitar problemas durante o processo de atualização ou implantação.

### Flask-Migrate e Gerenciamento de Migrações

O Flask-Migrate é uma extensão do Flask que simplifica e automatiza o processo de criação, aplicação e gerenciamento de migrações em um banco de dados SQLAlchemy. Ele oferece um conjunto de comandos que permitem criar migrações a partir de alterações no modelo de dados, aplicar essas migrações ao banco de dados e reverter migrações, se necessário.

Ao usar o Flask-Migrate, as migrações são representadas como arquivos Python que descrevem as alterações a serem aplicadas no banco de dados. Isso proporciona um método estruturado para versionar as mudanças no esquema do banco de dados, facilitando o controle e a aplicação consistente dessas alterações em diferentes ambientes.

### Inicialização e Criação de Migração
Agora que entendemos o conceito de migrações em bancos de dados e sua importância, vamos explorar como o Flask-Migrate simplifica o gerenciamento dessas migrações em um projeto Flask

Para começar a utilizar o Flask-Migrate, os seguintes comandos devem ser executados para inicializar e criar a primeira migração:

Inicialização, cria a pasta `migrations/`:
```bash
flask db init # Só é preciso uma vez, para criar a pasta
```
Criação de migrações, Cria o Banco de Dados ou o altera:
```bash
flask db migrate -m "Nome da migração"
```
Aplica a migração(modificações) ao banco de dados:
 ```bash
flask db upgrade
```

Esses comandos ajudam a gerenciar as migrações do banco de dados, refletindo as alterações no esquema do banco de dados de maneira controlada e organizada

## Estruturas Geradas

Após a inicialização e criação das migrações, o Flask-Migrate cria estruturas adicionais no seu projeto:

### `migrations/`

O diretório [`migrations/`](https://github.com/lukebgds/TecnologyWay_Site-Flask_Part-2/tree/main/migrations) armazena os arquivos relacionados às migrações do banco de dados. Esses arquivos descrevem as alterações no esquema do banco de dados.

- **`versions/`**: Contém os arquivos de migração Python gerados pelo Flask-Migrate. Cada arquivo descreve uma migração específica, incluindo operações como criação de tabelas, adição ou remoção de colunas, entre outras.

Outros arquivos e pastas importantes dentro de `migrations/` incluem:

- `README`: Instruções ou informações adicionais sobre as migrações.
- `alembic.ini`: Arquivo de configuração para o Alembic, usado pelo Flask-Migrate.
- `env.py`: Arquivo Python para a configuração do ambiente de migração.
- `script.py.mako`: Modelo de script usado para gerar os arquivos de migração.
- `pycache/`: Pasta que pode conter arquivos temporários gerados pelo Python.

### `O próprio Banco de Dados`

O banco de dados em si é criado ou alterado conforme as migrações são aplicadas. Dependendo do banco de dados e das configurações, o Flask-Migrate aplica as migrações ao banco de dados especificado, refletindo as alterações descritas nos arquivos de migração no esquema real do banco de dados.

## Gerenciamento de Pacotes Python

### `pip freeze` e `requirements.txt`

O `pip` é uma ferramenta para instalar e gerenciar pacotes Python. O comando `pip freeze` é usado para listar todos os pacotes instalados no ambiente virtual. Essa listagem inclui os nomes e versões de todos os pacotes Python instalados.

#### Criação do `requirements.txt`

O  [`requirements.txt`](https://github.com/lukebgds/TecnologyWay_Site-Flask_Part-2/blob/main/requirements.txt) é um arquivo de texto que contém uma lista dos pacotes Python instalados em um ambiente virtual. Ele é frequentemente utilizado para compartilhar e reproduzir um ambiente Python específico. Para criar um `requirements.txt`, basta executar o comando:

```bash
pip freeze > requirements.txt
```
Conteudo:
```bash
﻿alembic==1.12.1
blinker==1.7.0
click==8.1.7
colorama==0.4.6
dnspython==2.4.2
Flask==3.0.0
Flask-DotEnv==0.1.2
Flask-Migrate==4.0.5
Flask-Script==2.0.6
Flask-SQLAlchemy==3.1.1
greenlet==3.0.1
gunicorn==21.2.0
itsdangerous==2.1.2
Jinja2==3.1.2
Mako==1.3.0
MarkupSafe==2.1.3
packaging==23.2
python-dotenv==1.0.0
SQLAlchemy==2.0.23
typing_extensions==4.8.0
validate-email-address==1
Werkzeug==3.0.1
```
## Estrutura de Arquivos do Projeto Finalizada:
```
seu_projeto/
    migrations/
    BD_SITE.sqlite
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

``Todos os Direitos Reservados``

---

#### [Voltar ao topo](#site_flask---guia-pr%C3%A1ticopart-2-implementa%C3%A7%C3%A3o-do-framework-flask-com-deployheroku)
