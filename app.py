from flask import Flask, render_template, request, redirect, flash, session
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
import os
import json
app = Flask(__name__)
app.secret_key = "saju_secret_key"
ADMIN_USERNAME = "a-d-m-i-n"
ADMIN_PASSWORD = "admin"
# Gmail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sajunaturalhoney@gmail.com'
app.config['MAIL_PASSWORD'] = 'djue fpdi syuo oupq'   # Replace with your Gmail App Password

# IMPORTANT FIX
app.config["UPLOAD_FOLDER"] = "static/uploads"

mail = Mail(app)

# create upload folder if not exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


# =====================
# LOAD PRODUCTS SAFE
# =====================
def load_products():
    try:
        with open("products.json", "r") as f:
            return json.load(f)
    except:
        return []


# =====================
# HOME PAGE
# =====================
@app.route("/")
def home():
    products = load_products()
    return render_template("index.html", products=products)

from flask import send_from_directory
@app.route('/robots.txt')
def robots():
    return send_from_directory('.', 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('.', 'sitemap.xml')
@app.route("/admin")
def admin_shortcut():
    return redirect("/admin/login")
# =====================
# ADMIN LOGIN
# =====================
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect("/admin/dashboard")
        else:
            flash("Invalid credentials")

    return render_template("admin_login.html")


# =====================
# LOGOUT
# =====================
@app.route("/admin/logout")
def logout():
    session.pop("admin", None)
    return redirect("/admin/login")

# =====================
# DASHBOARD
# =====================
@app.route("/admin/dashboard")
def admin_dashboard():
    if not session.get("admin"):
        return redirect("/admin/login")

    products = load_products()
    return render_template("admin_dashboard.html", products=products)


# =====================
# ADD PRODUCT
# =====================
@app.route("/admin/add-product", methods=["GET", "POST"])
def add_product():
    if not session.get("admin"):
        return redirect("/admin/login")

    if request.method == "POST":
        name = request.form["name"]
        price500 = request.form["price500"]
        price1kg = request.form["price1kg"]
        description = request.form["description"]

        image = request.files["image"]
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        products = load_products()

        new_product = {
    "id": len(products) + 1,
    "name": name,
    "description": description,
    "price500": price500,
    "price1kg": price1kg,
    "weight500": "500 g",
    "weight1kg": "1 KG",
    "image": filename
}

        products.append(new_product)

        with open("products.json", "w") as f:
            json.dump(products, f, indent=4)

        flash("Product added successfully")
        return redirect("/admin/dashboard")

    return render_template("add_product.html")

@app.route("/admin/edit/<int:index>", methods=["GET", "POST"])
def edit_product(index):
    if not session.get("admin"):
        return redirect("/admin/login")

    products = load_products()

    if index >= len(products):
        flash("Product not found")
        return redirect("/admin/dashboard")

    if request.method == "POST":
        products[index]["name"] = request.form["name"]
        products[index]["description"] = request.form["description"]
        products[index]["price500"] = request.form["price500"]
        products[index]["price1kg"] = request.form["price1kg"]

        image = request.files.get("image")

        if image and image.filename != "":
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            products[index]["image"] = filename

        with open("products.json", "w") as f:
            json.dump(products, f, indent=4)

        flash("Product updated successfully")
        return redirect("/admin/dashboard")

    return render_template(
        "edit_product.html",
        product=products[index],
        index=index
    )

@app.route("/admin/delete/<int:index>")
def delete_product(index):
    if not session.get("admin"):
        return redirect("/admin/login")

    products = load_products()

    if index < len(products):
        products.pop(index)

        with open("products.json", "w") as f:
            json.dump(products, f, indent=4)

        flash("Product deleted successfully")

    return redirect("/admin/dashboard")
# =====================
# CONTACT FORM
# =====================
@app.route("/contact", methods=["POST"])
def contact():

    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]

    msg = Message(
        subject="New Customer Enquiry",
        sender=app.config['MAIL_USERNAME'],
        recipients=[app.config['MAIL_USERNAME']]
    )

    msg.body = f"""
Name : {name}
Email : {email}
Phone : {phone}
Message : {message}
"""

    mail.send(msg)

    reply = Message(
        subject="Thank You for Contacting SAJU Natural Honey 🍯",
        sender=app.config['MAIL_USERNAME'],
        recipients=[email]
    )

    reply.body = f"""
Dear {name},

Thank you for contacting SAJU Natural Honey.

We will contact you soon.

Regards,
SAJU Natural Honey
"""

    mail.send(reply)

    flash("Message sent successfully")
    return redirect("/")   
port = int(os.environ.get("PORT", 5000)) 
app.run(host="0.0.0.0", port=port)