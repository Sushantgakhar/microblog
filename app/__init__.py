from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

# Make sure this happens after declaring app to avoid circular import error


from app import views
