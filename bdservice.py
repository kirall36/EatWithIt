from mymodels import *
from datetime import date


def get_ration(user):
    if Ration.select().where(Ration.user == user.id_user):
        ration = Ration.get(Ration.user == user.id_user)
    else:
        ration = Ration(calories=0, carbs=0, date=date.today(), fats=0, proteins=0, user=user)
        ration.save()
    return ration


def get_product(product_name):
    product = Products.select().where(Products.name == product_name)
    return product


def add_product_in_ration(product, weight, meal_type, ration):
    meal = Meal(calories=float(product['calories'])*weight/100, proteins=product['proteins']*weight/100, \
                fats=product['fats']*weight/100, carbs=product['carbs']*weight/100, product=product['idproduct'], \
                weight=weight, meal_type=meal_type)
    meal.save()
    mealinrat = MealsInRation.raw('INSERT INTO eatwithit2.meals_in_ration (id_meal, id_ration) VALUES \
                                    (%s, %s)', meal.id_meal, ration)
    mealinrat.execute()
    ration = Ration.get(Ration.id_ration == ration)
    ration.calories += float(product['calories'])*weight/100
    ration.proteins += product['proteins']*weight/100
    ration.fats += product['fats']*weight/100
    ration.carbs += product['carbs']*weight/100
    ration.save()

def get_products_in_ration(rationid):
    meals = Meal.select().join(MealsInRation).where(MealsInRation.id_ration == rationid).join(Ration).objects()
    products = list(dict())
    for m in meals:
        products.append({'idmeal': m.id_meal, 'product': Products.get(Products.idproducts == m.product).name})
    return products


def delete_meal(idmeal, idration):
    mealinr = MealsInRation.get(MealsInRation.id_meal == idmeal)
    mealinr.delete_instance()
    meal = Meal.get(Meal.id_meal == idmeal)
    ration = Ration.get(Ration.id_ration == idration)
    ration.calories -= meal.calories
    ration.proteins -= meal.proteins
    ration.fats -= meal.fats
    ration.carbs -= meal.carbs
    ration.save()
    meal.delete_instance()
