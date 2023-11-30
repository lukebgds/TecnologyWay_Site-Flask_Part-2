# Importação das bibliotecas necessárias
from flask import Flask, render_template, request, jsonify  # Importa classes e métodos do Flask
from validate_email_address import validate_email  # Importa função de validação de e-mail
from models import Inscritos  # Importa o modelo de dados Inscritos
from database import db  # Importa a instância do SQLAlchemy
from flask_migrate import Migrate  # Importa a extensão Flask-Migrate para migrações de banco de dados
import dns.resolver  # Importa a biblioteca para resolução de DNS
import os  # Importa a biblioteca para manipulação de sistema de arquivos

# Configuração inicial da aplicação Flask
app = Flask(__name__)  # Inicializa a aplicação Flask

# Define a URI do banco de dados SQLite baseada no diretório raiz da aplicação e o nome do banco de dados
conexao = 'sqlite:///' + os.path.join(app.root_path, 'BD_SITE.sqlite')
app.config['SECRET_KEY'] = 'minha chave'  # Define a chave secreta para segurança
app.config['SQLALCHEMY_DATABASE_URI'] = conexao  # Configura a URI do banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desabilita o rastreamento de modificações no SQLAlchemy
db.init_app(app) # Inicializa a aplicação Flask com o SQLAlchemy
migrate = Migrate(app, db)  # Configura a extensão Flask-Migrate para gerenciar migrações

# Função para validar o formato do e-mail
def validar_email(email):
    is_valid = validate_email(email)  # Valida o formato do e-mail usando a função importada
    return is_valid

# Função para validar o domínio do e-mail
def validar_dominio(email):
    domain = email.split('@')[1]  # Obtém o domínio do e-mail
    try:
        # Consulta de registros MX para o domínio
        mx_records = dns.resolver.resolve(domain, 'MX')
        return bool(mx_records)  # Retorna True se houver registros MX para o domínio
    except dns.resolver.NoAnswer:
        return False  # Retorna False se não houver resposta
    except dns.resolver.NXDOMAIN:
        return False  # Retorna False se o domínio não existir

# Rota para lidar com a inscrição por meio de requisições POST
@app.route('/inscrever', methods=['POST'])
def inscrever():
    if request.method == 'POST':  # Verifica se é uma requisição POST
        email = request.form['email']  # Obtém o e-mail do formulário

        # Verifica se o e-mail e o domínio são válidos usando as funções de validação
        if not validar_email(email) or not validar_dominio(email):
            return jsonify({'message': 'Endereço de e-mail inválido ou domínio não válido.'}), 400  # Retorna erro 400 se o e-mail não for válido

        # Verifica se o e-mail já está registrado no banco de dados
        existente = Inscritos.query.filter_by(email=email).first()
        if existente:
            return jsonify({'message': 'Este e-mail já está registrado.'}), 409  # Retorna erro 409 se o e-mail já estiver registrado
        else:
            # Registra o e-mail se não estiver previamente cadastrado
            inscrito = Inscritos(email=email)
            db.session.add(inscrito)  # Adiciona o e-mail à sessão do banco de dados
            db.session.commit()  # Confirma a adição no banco de dados
            return jsonify({'message': 'Inscrição realizada com sucesso!'}), 201  # Retorna mensagem de sucesso

# Rotas para as páginas principais do site
@app.route('/')
def index():
    return render_template('index.html')  # Renderiza o template da página inicial

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')  # Renderiza o template da página "Sobre nós"

@app.route('/contato')
def contato():
    return render_template('contato.html')  # Renderiza o template da página de contato

# Inicializa a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)  # Executa o aplicativo Flask em modo de depuração