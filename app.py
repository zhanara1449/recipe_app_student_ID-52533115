from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

# -------------------
# Homepage
# -------------------
@app.route("/")
def home():
    return render_template("index.html")

# -------------------
# Search recipes
# -------------------
@app.route("/search", methods=["GET", "POST"])
def search():

    conn = get_db()
    cur = conn.cursor()

    query = "SELECT * FROM recipes WHERE 1=1"
    params = []

    if request.method == "POST":

        name = request.form.get("name")
        cuisine = request.form.get("cuisine")

        if name:
            query += " AND name LIKE ?"
            params.append(f"%{name}%")

        if cuisine:
            query += " AND cuisine LIKE ?"
            params.append(f"%{cuisine}%")

    cur.execute(query, params)
    results = cur.fetchall()

    conn.close()

    return render_template("search.html", results=results)

# -------------------
# Recipe detail page
# -------------------
@app.route("/recipe/<int:id>")
def recipe_detail(id):

    conn = get_db()
    cur = conn.cursor()

    # Get recipe
    cur.execute("""
        SELECT * FROM recipes
        WHERE recipe_id = ?
    """, (id,))

    recipe = cur.fetchone()

    # Get related reviews
    cur.execute("""
        SELECT username, rating, comment
        FROM reviews
        WHERE recipe_id = ?
    """, (id,))

    reviews = cur.fetchall()

    conn.close()

    return render_template(
        "detail.html",
        recipe=recipe,
        reviews=reviews
    )

# -------------------
# Statistics page
# -------------------
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

    return render_template("stats.html", stats=stats)

# -------------------
# Run app
# -------------------
if __name__ == "__main__":
    app.run(debug=True)