from peewee import *

database = MySQLDatabase('eatwithit2', **{'charset': 'utf8', 'use_unicode': True, 'user': 'root', 'password': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Products(BaseModel):
    calories = IntegerField()
    carbs = FloatField()
    fats = FloatField()
    idproducts = AutoField()
    name = CharField()
    proteins = FloatField()

    class Meta:
        table_name = 'products'

class Incompatibleproducts(BaseModel):
    id_product1 = ForeignKeyField(column_name='id_product1', field='idproducts', model=Products)
    id_product2 = ForeignKeyField(backref='products_id_product2_set', column_name='id_product2', field='idproducts', model=Products)

    class Meta:
        table_name = 'incompatibleproducts'
        indexes = (
            (('id_product1', 'id_product2'), True),
        )
        primary_key = CompositeKey('id_product1', 'id_product2')

class Meal(BaseModel):
    calories = IntegerField(null=True)
    carbs = FloatField(null=True)
    fats = FloatField(null=True)
    id_meal = AutoField()
    meal_type = CharField()
    product = ForeignKeyField(column_name='product_id', field='idproducts', model=Products)
    proteins = FloatField(null=True)
    weight = FloatField()

    class Meta:
        table_name = 'meal'

class User(BaseModel):
    activity_level = CharField(column_name='activityLevel')
    birth_date = DateField()
    calories_recomendation = FloatField(column_name='caloriesRecomendation', constraints=[SQL("DEFAULT 2000")])
    diet = CharField(constraints=[SQL("DEFAULT 'wl'")])
    hight = FloatField()
    id_user = AutoField()
    login = CharField()
    name = CharField()
    password = CharField()
    role = CharField()
    sex = CharField()
    weight = FloatField()

    class Meta:
        table_name = 'user'

class Ration(BaseModel):
    calories = IntegerField(null=True)
    carbs = FloatField(null=True)
    date = DateField()
    fats = FloatField(null=True)
    id_ration = AutoField()
    proteins = FloatField(null=True)
    user = ForeignKeyField(column_name='user_id', field='id_user', model=User)

    class Meta:
        table_name = 'ration'

class MealsInRation(BaseModel):
    id_meal = ForeignKeyField(column_name='id_meal', field='id_meal', model=Meal)
    id_ration = ForeignKeyField(column_name='id_ration', field='id_ration', model=Ration)

    class Meta:
        table_name = 'meals_in_ration'
        indexes = (
            (('id_meal', 'id_ration'), True),
        )
        primary_key = CompositeKey('id_meal', 'id_ration')

