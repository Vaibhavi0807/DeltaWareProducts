
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to DeltaWare Products Application"

@app.route("/products")
def products():
    products = [
        { "id": 1001, "name": "Tools Gears", "description": "Gear tools production specification" },
        { "id": 2001, "name": "Panels", "description": "Switch Gear Panels" },
        { "id": 2008, "name": "DocTonar", "description": "Document Solar Objects" }
    ]
    return render_template("products.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)