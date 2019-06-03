from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from mymodels import *
from wtforms import Form, StringField, FloatField, PasswordField, DateField, SelectField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from calculation import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'EatWithItSecretKey01'
ADMINPASSWORD = 'adminsecret'
VIPPASSWORD = 'vipsecret'


@app.route('/')
def index():
    if 'login' in session:
        user = User.get(User.login == session['login'])
        return render_template('home.html', name=user.name)
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    login = StringField('Login', [validators.Length(min=1, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')
    admin_password = PasswordField('Admin Password')
    hight = FloatField('Hight')
    weight = FloatField('Weight')
    birth_date = DateField('Birth date in format yyyy-mm-dd', [validators.DataRequired()])
    sex = SelectField(u'Sex', choices=[('m', 'male'), ('f', 'female')])
    activity_level = SelectField(u'Activity Level', choices=[('low', 'Activity beyond baseline but fewer than 150 minutes a week'),
                                                             ('medium', '150 minutes to 300 minutes a week'),
                                                             ('high', 'More than 300 minutes a week')])
    diet = SelectField(u'Diet Type', choices=[('wl', 'To loss your weight'), ('wm', 'To maintain your weight'),
                                              ('wg', 'To gain your weight')])
    vip_password = PasswordField('Enter VIP Password if you have one')



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        if User.select().where(User.login == form.login.data):
            error = 'This login is already used'
            form.login.data = ''
            return render_template('register.html', form=form, error=error)
        else:
            name = form.name.data
            login = form.login.data
            password = sha256_crypt.encrypt(str(form.password.data))
            admin_password = form.admin_password.data
            vip_password = form.vip_password.data
            hight = form.hight.data
            weight = form.weight.data
            birth_date = form.birth_date.data
            sex = form.sex.data
            activity_level = form.activity_level.data
            diet = form.diet.data

            if admin_password == ADMINPASSWORD:
                user = User(name=name, login=login, password=password, role='Admin',
                        hight=hight, activity_level=activity_level, weight=weight, sex=sex, birth_date=birth_date,
                            diet=diet, calories_recomendation=2000)
            elif vip_password == VIPPASSWORD:
                user = User(name=name, login=login, password=password, role='Vip',
                            hight=hight, activity_level=activity_level, weight=weight, sex=sex, birth_date=birth_date,
                            diet=diet, calories_recomendation=2000)
            else:
                user = User(name=name, login=login, password=password, role='User',
                            hight=hight, activity_level=activity_level, weight=weight, sex=sex, birth_date=birth_date,
                            diet=diet, calories_recomendation=2000)
            user.calories_recomendation = calculate_calories(user)
            user.save()

            flash('You are now registered and can log in', 'success')

            return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        login = request.form['login']
        password_candidate = request.form['password']

        user = User.get(User.login == login)

        if user:
            password = user.password

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['login'] = login


                flash('You are now logged in', 'success')
                return redirect(url_for('index'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')


# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
