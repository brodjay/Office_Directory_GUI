from flask import Flask
# import pymysql

# conn = pymysql.connect(
#     host = "localhost",
#     user = "gui_app",
#     password = "admin",
#     database = "users_db"
# )

# cursor = conn.cursor()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
from routes import *

if __name__ == "__main__":
    app.run(debug=True)