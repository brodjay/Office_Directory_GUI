from app import app
from flask import render_template, redirect, url_for



@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/findid')
def findid():
    return render_template('findid.html')

@app.route('/findname')
def findname():
    return render_template('findname.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')