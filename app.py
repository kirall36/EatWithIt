from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from forms import *
from passlib.hash import sha256_crypt
from functools import wraps
from calculation import *
from bdservice import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'EatWithItSecretKey01'
ADMINPASSWORD = 'adminsecret'
VIPPASSWORD = 'vipsecret'


@app.route('/')
def index():
    if 'login' in session:
        ration = Ration.get(Ration.id_ration == session['ration'])
        user = User.get(User.login == session['login'])
        ration_dict = {
            'calories': ration.calories,
            'proteins': ration.proteins,
            'fats': ration.fats,
            'carbs': ration.carbs,
            'recomendation': user.calories_recomendation,
        }

        return render_template('home.html', name=user.name, ration_dict=ration_dict)
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/search_product', methods=['GET', 'POST'])
def search_product():
    form = SearchProductForm(request.form)
    if request.method == 'POST' and form.validate():
        product_name = form.name.data
        product = get_product(product_name)
        if product:
            return redirect(url_for('add_product', idproduct=product.get().idproducts, name=product.get().name, \
                                    calories=product.get().calories, proteins=product.get().proteins, \
                                    fats=product.get().fats, carbs=product.get().carbs))
            #return render_template('add_product.html', product=product_dict, form=form)
        else:
            error ='Product with name ' + product_name + ' was not found'
            return render_template('search_product.html', form=form, error=error)
    return render_template('search_product.html', form=form)


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = AddProductForm(request.form)
    product = {
        'idproduct': request.args.get('idproduct'),
        'name': request.args.get('name'),
        'calories': request.args.get('calories'),
        'proteins': float(request.args.get('proteins')),
        'fats': float(request.args.get('fats')),
        'carbs': float(request.args.get('carbs')),
    }
    if request.method == 'POST' and form.validate():
        weight = form.weight.data
        meal_type = form.meal_type.data
        add_product_in_ration(product, float(weight), meal_type, session['ration'])
        flash('Product ' + product['name'] +  ' was added', 'success')
        return redirect(url_for('index'))
    return render_template('add_product.html', form=form, product=product)


@app.route('/delete_product', methods=['GET', 'POST'])
def delete_product():
    products = get_products_in_ration(session['ration'])
    return render_template('delete_products.html', products=products)


@app.route('/delete/<idmeal>', methods=['GET', 'POST'])
def delete(idmeal):
    delete_meal(idmeal, session['ration'])
    return redirect(url_for('index'))


@app.route('/change_info', methods=['GET', 'POST'])
def change_info():
    form = ChangeForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.get(User.login == session['login'])
        password = sha256_crypt.encrypt(str(form.password.data))
        vip_password = form.vip_password.data
        hight = form.hight.data
        weight = form.weight.data
        activity_level = form.activity_level.data
        diet = form.diet.data

        if vip_password == VIPPASSWORD:
            user.role = 'Vip'
        user.password = password
        user.hight = hight
        user.weight = weight
        user.activity_level = activity_level
        user.diet = diet
        user.calories_recomendation = calculate_calories(user)
        user.save()

        flash('You have changed your info', 'success')
        return redirect(url_for('index'))

    return render_template("change_info.html", form=form)

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
                ration = get_ration(user)
                session['ration'] = ration.id_ration

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
