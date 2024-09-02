from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from models import User

class RegistrationForm(FlaskForm):
    """Formulário de registro de usuário."""

    username = StringField('Nome do Usuário', validators=[DataRequired(), Length(min=2, max=150)])  # Alterado para 'Nome do Usuário'
    password = PasswordField('Senha', validators=[DataRequired()])  # Alterado para 'Senha'
    confirm_password = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password')])  # Alterado para 'Confirmar Senha'
    submit = SubmitField('Registrar')

    def validate_username(self, username):
        """Verifica se o nome de usuário já está em uso."""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Nome de usuário já está em uso.')  # Alterado para 'Nome de usuário'

class LoginForm(FlaskForm):
    """Formulário de login de usuário."""

    username = StringField('Nome do Usuário', validators=[DataRequired()])  # Alterado para 'Nome do Usuário'
    password = PasswordField('Senha', validators=[DataRequired()])  # Alterado para 'Senha'
    submit = SubmitField('Login')

class TaskForm(FlaskForm):
    """Formulário para adicionar uma nova tarefa."""

    content = StringField('Conteúdo da Tarefa', validators=[DataRequired()])  # Alterado para 'Conteúdo da Tarefa'
    submit = SubmitField('Adicionar Tarefa')