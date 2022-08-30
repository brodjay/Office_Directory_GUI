import pymysql

conn = pymysql.connect(
    host = "localhost",
    user = "gui_app",
    password = "admin",
    database = "users_db"
)

cursor = conn.cursor()

