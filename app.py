# Importação das bibliotecas necessárias
from flask import Flask, render_template, request, jsonify
from validate_email_address import validate_email
from models import Inscritos
from database import db
from flask_migrate import Migrate
import dns.resolver

# Configuração inicial da aplicação Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'minha chave'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BD_SITE.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

# Função para validar o formato do e-mail
def validar_email(email):
    is_valid = validate_email(email)
    return is_valid

# Função para validar o domínio do e-mail
def validar_dominio(email):
    domain = email.split('@')[1]
    try:
        # Consulta de registros MX para o domínio
        mx_records = dns.resolver.resolve(domain, 'MX')
        return bool(mx_records)
    except dns.resolver.NoAnswer:
        return False
    except dns.resolver.NXDOMAIN:
        return False

# Rota para lidar com a inscrição por meio de requisições POST
@app.route('/inscrever', methods=['POST'])
def inscrever():
    if request.method == 'POST':
        email = request.form['email']

        # Verifica se o e-mail e o domínio são válidos
        if not validar_email(email) or not validar_dominio(email):
            return jsonify({'message': 'Endereço de e-mail inválido ou domínio não válido.'}), 400

        # Verifica se o e-mail já está registrado
        existente = Inscritos.query.filter_by(email=email).first()
        if existente:
            return jsonify({'message': 'Este e-mail já está registrado.'}), 409
        else:
            # Registra o e-mail se não estiver previamente cadastrado
            inscrito = Inscritos(email=email)
            db.session.add(inscrito)
            db.session.commit()
            return jsonify({'message': 'Inscrição realizada com sucesso!'}), 201

# Rotas para as páginas principais do site
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

# Inicializa a aplicação Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)