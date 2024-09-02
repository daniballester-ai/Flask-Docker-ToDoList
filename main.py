from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from models import db, User, Task
from forms import RegistrationForm, LoginForm, TaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kil12s8s9_@34'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' 

@login_manager.user_loader
def load_user(user_id):
    """Carrega o usuário do banco de dados com base no ID."""
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Rota para registrar um novo usuário."""
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Sua conta foi criada! Agora você pode fazer o log in.', 'successo')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Rota para efetuar login no sistema."""
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Falha no log in. Por favor, verifique seu nome de usuário e senha.', 'alerta')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    """Rota para deslogar o usuário."""
    logout_user()
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    """Rota para a página principal da lista de tarefas."""
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(content=form.content.data, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))

    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', tasks=tasks, form=form)

@app.route('/delete/<int:id>')
@login_required
def delete(id):
    """Rota para deletar uma tarefa."""
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        flash('Você não possui permissão para excluir esta tarefa.', 'alerta')
        return redirect(url_for('index'))

    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria o banco de dados se ainda não existir
    app.run(debug=True, host='0.0.0.0', port=5000)