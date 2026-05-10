from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

# --------------------------
# Homepage
# --------------------------
@app.route("/")
def home():
    return render_template("index.html")

# --------------------------
# Search recipes
# --------------------------
@app.route("/search", methods=["GET", "POST"])
def search():

    conn = get_db()
    cur = conn.cursor()

    query = "SELECT * FROM recipes WHERE 1=1"
    params = []

    if request.method == "POST":
        name = request.form.get("name")
        cuisine = request.form.get("cuisine")
        difficulty =request.form.get("difficulty")
        max_time=request.form.get("max_time")

        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name}%")

        if cuisine:
            query += " AND cuisine LIKE ?"
            params.append(f"%{cuisine}%")
            
        if difficulty:
            query += " AND difficulty = ?"
            params.append(f"%{difficulty}%")
            
        if max_time:
            query += " AND cooking_time <= ?"
            params.append(f"%{max_time}%")
            
    query += " ORDER BY name ASC"

    cur.execute(query, params)

    results = cur.fetchall()

    conn.close()

    return render_template(
        "search.html",
        results=results
    )

# --------------------------
# Recipe details
# --------------------------
@app.route("/recipe/<int:id>")
def recipe_detail(id):

    conn = get_db()
    cur = conn.cursor()

    # Get recipe
    cur.execute("""
        SELECT *
        FROM recipes
        WHERE recipe_id = ?
    """, (id,))

    recipe = cur.fetchone()

    # Get ingredients
    cur.execute("""
        SELECT ingredient_name, quantity, unit
        FROM ingredients
        WHERE recipe_id = ?
    """, (id,))

    ingredients = cur.fetchall()

    conn.close()

    return render_template(
        "detail.html",
        recipe=recipe,
        ingredients=ingredients
    )

# --------------------------
# Statistics page
# --------------------------
@app.route("/stats")
def stats():

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT cuisine, COUNT(*)
        FROM recipes
        GROUP BY cuisine
    """)

    stats = cur.fetchall()

    conn.close()

    return render_template(
        "stats.html",
        stats=stats
    )

# --------------------------# --------------------------
# Cuisine page
# --------------------------
@app.route("/cuisine/<cuisine>")
def cuisine_page(cuisine):

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM recipes
        WHERE cuisine = ?
        ORDER BY cooking_time ASC
    """, (cuisine,))

    recipes = cur.fetchall()

    conn.close()

    return render_template(
        "cuisine.html",
        cuisine=cuisine,
        recipes=recipes
    )


# Run Flask
# --------------------------
if __name__ == "__main__":
    app.run(debug=True)