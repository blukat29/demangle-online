from flask import Flask
from .views import front_page

app = Flask(__name__)
app.config.from_object('demangle.settings')
app.register_blueprint(front_page)

