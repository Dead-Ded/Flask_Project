from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from data import db_session
from data.login import LoginForm
from data.user import User
from data.register import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'JGKzpcce9ajD72k'

login_manager = LoginManager()
login_manager.init_app(app)

@app.route("/")
@app.route("/index")
def about():
    return render_template("index.html")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():  # Вход
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.login == form.login.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('signin.html', message="Неправильный логин или пароль", form=form)
    return render_template('signin.html', title='Вход', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():  # Регистрация
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.login == form.login.data).first():
            return render_template('register.html', title='Register', form=form,
                                   message="Такой пользователь уже существует")
        user = User(login=form.login.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
@login_required
def logout():  # Выход
    logout_user()
    return redirect("/")


@app.route('/users')
@login_required
def users():  # Возвращает админу список пользователей
    if current_user.login != 'admin':
        return "Доступ запрещен"
    db_sess = db_session.create_session()
    users = db_sess.query(User).order_by(User.id.asc())  # Присвоение переменной таблицы БД
    return render_template('users.html', users=users)


if __name__ == '__main__':
    db_session.global_init("db/db.db")
    app.run(port=8000, host="127.0.0.1")
