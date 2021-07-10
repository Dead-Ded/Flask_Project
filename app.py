from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import datetime

from data import db_session
from data.login import LoginForm
from data.user import User
from data.register import RegisterForm
from data.section import Section
from data.topic import Topic
from data.post import Post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'JGKzpcce9ajD72k'

login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
@app.route("/index")
def about():
    return render_template("index.html")


@login_manager.user_loader  # Логин
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
        user = User(login=form.login.data, deleted=False, status_id=3,  # Созданире строки для БД
                                    registration_date=datetime.date.today())
        user.set_password(form.password.data)
        db_sess.add(user)  # <-
        db_sess.commit()  # <-
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
    if current_user.status_id != 1:
        return "Доступ запрещен"
    db_sess = db_session.create_session()
    users = db_sess.query(User).order_by(User.id.asc())  # Присвоение переменной таблицы БД
    return render_template('users.html', users=users)


@app.route('/')
def clear():
    return render_template("clear.html")

@app.route('/sections')
def sections():  # Возвращает админу список пользователей
    db_sess = db_session.create_session()
    sections = db_sess.query(Section).order_by(Section.id.asc())  # Присвоение переменной таблицы БД
    return render_template('sections.html', sections=sections)


@app.route('/sections/<section_id>/topics')
def topics(section_id):
    db_sess = db_session.create_session()
    topics = db_sess.query(Topic).filter(Topic.section_id == section_id).order_by(Topic.id.asc())
    section = db_sess.query(Section).filter(Section.id == section_id).first().name
    return render_template('topics.html', topics=topics, section=section)


@app.route('/sections/<section_id>/topics/<topic_id>/posts', methods=['GET', 'POST'])
def posts(section_id, topic_id):
    db_sess = db_session.create_session()
    posts = db_sess.query(Post).filter(Post.topic_id == topic_id).order_by(Post.id.asc())
    topic = db_sess.query(Topic).filter(Topic.id == topic_id).first().name
    section = db_sess.query(Section).filter(Section.id == section_id).first().name
    # if current_user.is_authenticated:
    if request.method == 'POST':
        post_text = Post(message=request.form['post-message'], date=datetime.datetime.now(),
                    topic_id=topic_id, deleted=False,
                         user_id=current_user.id)
        db_sess.add(post_text)
        db_sess.commit()
    return render_template('posts.html', section_id=section_id, section=section, topic=topic,
                                                                                        posts=posts)


if __name__ == '__main__':
    db_session.global_init("db/db.db")
    app.run(port=8000, host="127.0.0.1")
