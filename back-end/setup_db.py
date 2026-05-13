import sqlite3
import csv

conn = sqlite3.connect("database.db")
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS recipes (
    recipe_id INTEGER PRIMARY KEY,
    name TEXT,
    cuisine TEXT,
    cooking_time INTEGER,
    difficulty TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS ingredients (
    ingredient_id INTEGER PRIMARY KEY,
    recipe_id INTEGER,
    ingredient_name TEXT,
    quantity REAL,
    unit TEXT,
    FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id)
)
""")


with open("recipes.csv", newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        cur.execute("""
        INSERT INTO recipes
        VALUES (?, ?, ?, ?, ?)
        """, (
            row["recipe_id"],
            row["name"],
            row["cuisine"],
            row["cooking_time"],
            row["difficulty"]
        ))


with open("ingredients.csv", newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        cur.execute("""
        INSERT INTO ingredients
        VALUES (?, ?, ?, ?, ?)
        """, (
            row["ingredient_id"],
            row["recipe_id"],
            row["ingredient_name"],
            row["quantity"],
            row["unit"]
        ))

conn.commit()
conn.close()

print("Database created successfully!")