from database import db # Importa a instância do SQLAlchemy

class Inscritos(db.Model): # Define um modelo de dados chamado "Inscritos"
    __tablename__ = 'Inscritos' # Nome da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True) # Coluna 'id' do tipo inteiro e chave primária
    email = db.Column(db.String(120), unique=True, nullable=False)  # Coluna 'email' do tipo string, único e não nulo

    def __init__(self, email): # Método inicializador para a classe Inscritos
        self.email = email # Define o atributo 'email' ao criar uma instância do modelo