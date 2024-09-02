from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
""" Cria uma instância da classe SQLAlchemy chamada db, 
    que será usada para definir os modelos de dados.
"""

class User(db.Model, UserMixin):
    """Representa um usuário na aplicação.
       db.Model: para ser mapeada para uma tabela do banco de dados
       UserMixin: para implementar os métodos de autenticação
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)

    def set_password(self, password):
        """Criptografa a senha do usuário."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica se a senha fornecida corresponde à senha armazenada."""
        return check_password_hash(self.password_hash, password)

class Task(db.Model):
    """Representa uma tarefa na aplicação.
       db.Model: para ser mapeada para uma tabela do banco de dados
    """
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
