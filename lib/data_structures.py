spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(foods):
    return [food["name"] for food in foods]

def get_spiciest_foods(foods):
    return [food for food in foods if food["heat_level"] > 5]

def print_spicy_foods(foods):
    for food in foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

def get_spicy_food_by_cuisine(foods, cuisine):
    for food in foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(foods):
    spiciest = get_spiciest_foods(foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(foods):
    total = sum(food["heat_level"] for food in foods)
    return total // len(foods)

def create_spicy_food(foods, new_food):
    foods.append(new_food)
    return foods


print(get_names(spicy_foods))
# ['Green Curry', 'Buffalo Wings', 'Mapo Tofu']

print(get_spiciest_foods(spicy_foods))
# [{'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9}, {'name': 'Mapo Tofu', 'cuisine': 'Sichuan', 'heat_level': 6}]

print_spicy_foods(spicy_foods)
# Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# Buffalo Wings (American) | Heat Level: 🌶🌶🌶
# Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶

print(get_spicy_food_by_cuisine(spicy_foods, "American"))
# {'name': 'Buffalo Wings', 'cuisine': 'American', 'heat_level': 3}

print_spiciest_foods(spicy_foods)
# Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶

print(get_average_heat_level(spicy_foods))
# 6

create_spicy_food(spicy_foods, {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10
})
print(spicy_foods[-1])
# {'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10}



