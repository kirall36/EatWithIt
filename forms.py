from wtforms import Form, StringField, FloatField, PasswordField, DateField, SelectField, validators


class ChangeForm(Form):
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')
    hight = FloatField('Hight')
    weight = FloatField('Weight')
    activity_level = SelectField(u'Activity Level', choices=[('low', 'Activity beyond baseline but fewer than 150 minutes a week'),
                                                             ('medium', '150 minutes to 300 minutes a week'),
                                                             ('high', 'More than 300 minutes a week')])
    diet = SelectField(u'Diet Type', choices=[('wl', 'To loss your weight'), ('wm', 'To maintain your weight'),
                                              ('wg', 'To gain your weight')])
    vip_password = PasswordField('Enter VIP Password if you have one')


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


class SearchProductForm(Form):
    name = StringField('Enter product', [validators.DataRequired()])


class AddProductForm(Form):
    weight = FloatField('Weight in g', [validators.DataRequired()])
    meal_type = SelectField(u'Meal Type', choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'),
                                              ('dinner', 'Dinner'), ('snack', 'Snack')])

