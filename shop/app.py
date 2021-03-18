from flask import Flask, render_template
from views.products import product_app
from flask_migrate import Migrate
from models.database import db


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(product_app, url_prefix="/products")


@app.route("/")
def main_page():
    return render_template("index.html")
