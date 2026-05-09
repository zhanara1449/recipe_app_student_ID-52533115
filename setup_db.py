import sqlite3
import csv

conn = sqlite3.connect("database.db")
cur = conn.cursor()

# -----------------------------
# Create recipes table
# -----------------------------
cur.execute("""
CREATE TABLE IF NOT EXISTS recipes (
    recipe_id INTEGER PRIMARY KEY,
    name TEXT,
    cuisine TEXT,
    ingredients TEXT,
    instructions TEXT
)
""")

# -----------------------------
# Create reviews table
# -----------------------------
cur.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    review_id INTEGER PRIMARY KEY,
    recipe_id INTEGER,
    username TEXT,
    rating INTEGER,
    comment TEXT,
    FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id)
)
""")

# -----------------------------
# Insert recipes CSV
# -----------------------------
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
            row["ingredients"],
            row["instructions"]
        ))

# -----------------------------
# Insert reviews CSV
# -----------------------------
with open("reviews.csv", newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        cur.execute("""
        INSERT INTO reviews
        VALUES (?, ?, ?, ?, ?)
        """, (
            row["review_id"],
            row["recipe_id"],
            row["username"],
            row["rating"],
            row["comment"]
        ))

conn.commit()
conn.close()

print("Database created successfully!")