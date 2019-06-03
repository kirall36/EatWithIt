from datetime import date


diet_type = {
    'wl': 0.8,
    'wm': 1,
    'wg': 1.2
}

activity_type = {
    'low': 1.2,
    'medium': 1.55,
    'high': 1.725
}


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def calculate_calories(user):
    if user.sex == 'm':
        calories = round((10 * user.weight + 6.25 * user.hight - 5 * calculate_age(user.birth_date) + 5) \
                         * activity_type[user.activity_level] * diet_type[user.diet])
    else:
        calories = round((10 * user.weight + 6.25 * user.hight - 5 * calculate_age(user.birth_date) - 161) \
                         * activity_type[user.activity_level] * diet_type[user.diet])
    return calories