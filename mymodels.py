from peewee import *

database = MySQLDatabase('eatwithit', **{'charset': 'utf8', 'use_unicode': True, 'user': 'root', 'password': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class DerivationCodeDescription(BaseModel):
    derivation_descript = CharField(column_name='Derivation_Descript', null=True)
    derivation_code = CharField(index=True, null=True)

    class Meta:
        table_name = 'derivation_code_description'
        primary_key = False

class Nutrient(BaseModel):
    derivation_code = ForeignKeyField(column_name='Derivation_Code', field='derivation_code', model=DerivationCodeDescription, null=True)
    ndb_no = CharField(column_name='NDB_No', index=True, null=True)
    nutrient_code = CharField(column_name='Nutrient_Code', index=True, null=True)
    nutrient_name = CharField(column_name='Nutrient_name', null=True)
    output_uom = CharField(column_name='Output_uom', null=True)
    output_value = CharField(column_name='Output_value', null=True)

    class Meta:
        table_name = 'nutrient'
        primary_key = False

class ServingSize(BaseModel):
    household_serving_size = CharField(column_name='Household_Serving_Size', null=True)
    household_serving_size_uom = CharField(column_name='Household_Serving_Size_UOM', null=True)
    ndb_no = CharField(column_name='NDB_No', primary_key=True)
    preparation_state = CharField(column_name='Preparation_State', null=True)
    serving_size = CharField(column_name='Serving_Size', null=True)
    serving_size_uom = CharField(column_name='Serving_Size_UOM', null=True)

    class Meta:
        table_name = 'serving_size'

class Products(BaseModel):
    ndb_number = ForeignKeyField(column_name='NDB_Number', field='ndb_no', model=ServingSize, primary_key=True)
    ingredients_english = TextField(null=True)
    long_name = CharField(null=True)
    manufacturer = CharField(null=True)

    class Meta:
        table_name = 'products'

class Incompatibleproducts(BaseModel):
    id_product1 = ForeignKeyField(column_name='id_product1', field='ndb_number', model=Products)
    id_product2 = ForeignKeyField(backref='products_id_product2_set', column_name='id_product2', field='ndb_number', model=Products)

    class Meta:
        table_name = 'incompatibleproducts'
        indexes = (
            (('id_product1', 'id_product2'), True),
        )
        primary_key = CompositeKey('id_product1', 'id_product2')

class Meal(BaseModel):
    calories = FloatField(null=True)
    carbs = FloatField(null=True)
    fats = FloatField(null=True)
    id_meal = AutoField()
    meal_type = CharField()
    product = ForeignKeyField(column_name='product_id', field='ndb_number', model=Products)
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
    carbs = IntegerField(null=True)
    date = DateField()
    fats = IntegerField(null=True)
    id_ration = AutoField()
    proteins = IntegerField(null=True)
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

