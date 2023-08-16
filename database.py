import sqlite3

con = sqlite3.connect("nutricional.db")

cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS food
            (food_id INTEGER PRIMARY KEY AUTOINCREMENT,
            food_name, category, calories, protein, 
            carbohydrates, fat, fiber, vitamins, minerals)""")

food_data = [
    ('Apple', 'Fruits', 95, 0.5, 25, 0.3, 4.4, 'Vitamin A, Vitamin C', 'Potassium, Calcium'),
    ('Chicken Breast', 'Meat and Poultry', 165, 31, 0, 3.6, 0, 'Vitamin B6, Niacin', 'Iron, Phosphorus'),
    ('Spinach', 'Vegetables', 7, 0.9, 1.1, 0.1, 2.2, 'Vitamin K, Vitamin A', 'Iron, Magnesium'),
    ('Rice', 'Grains', 205, 4.3, 45, 0.4, 0.6, '-', 'Iron, Phosphorus'),
    ('Salmon', 'Fish and Seafood', 206, 22, 0, 13, 0, 'Vitamin D, Vitamin B12', 'Omega-3 Fatty Acids'),
    ('Yogurt', 'Dairy', 150, 10, 12, 5, 0, 'Calcium, Vitamin D', 'Probiotics'),
    ('Banana', 'Fruits', 105, 1.3, 27, 0.4, 3.1, 'Vitamin B6, Vitamin C', 'Potassium, Magnesium'),
    ('Broccoli', 'Vegetables', 31, 2.5, 6.6, 0.3, 2.4, 'Vitamin K, Vitamin C', 'Folate, Potassium'),
    ('Bread', 'Grains', 79, 2.7, 14, 1, 1.6, '-', 'Iron, Magnesium'),
    ('Egg', 'Dairy', 68, 5.5, 0.6, 4.8, 0, 'Vitamin D, Vitamin B12', 'Choline, Selenium')
]

cur.executemany("INSERT INTO food(food_name, category, calories, protein, carbohydrates, fat, fiber, vitamins, minerals) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?)", food_data)

con.commit() # save changes

res = cur.execute("SELECT food_name FROM food")
print(res.fetchall())













con.close()