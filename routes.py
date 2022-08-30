from app import app
from flask import render_template, redirect, url_for, request
import forms
from db import *

#@# Main Page
@app.route('/index')
def index():
    return render_template('index.html')

#@# Search by id
@app.route('/findid', methods = ['GET', 'POST'])
def findid():
    form = forms.FindIdForm()
    if request.method == "POST":
        findid_sql = "SELECT * FROM users WHERE id = %s"
        value = (form.id.data,)
        cursor.execute(findid_sql, value)
        results = cursor.fetchall()
        return render_template('findid.html', form=form, results=results)
    return render_template('findid.html', form=form)

#@# Search by name
@app.route('/findname', methods = ['GET', 'POST'])
def findname():
    form = forms.FindNameForm()
    if request.method == "POST":
        findname_sql = "SELECT * FROM users WHERE first_name = %s or last_name = %s"
        value = (form.firstname.data, form.lastname.data)
        cursor.execute(findname_sql, value)
        results = cursor.fetchall()
        return render_template('findname.html', form=form, results=results)
    return render_template('findname.html', form = form)

#@# Add new user
@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = forms.AddUserForm()
    if form.validate_on_submit():
        return 
    return render_template('add.html', form = form)

#@# Update existing user
@app.route('/update', methods = ['GET', 'POST'])
def update():
    form = forms.UpdateUserForm()
    if form.validate_on_submit():
        return 
    return render_template('update.html', form = form)

#@# Delete user
@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    form = forms.DeleteUserForm()
    if form.validate_on_submit():
        return 
    return render_template('delete.html', form = form)

#@# Login user
@app.route('/', methods = ['GET', 'POST'])
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = forms.LoginUserForm()
    if form.validate_on_submit():        
        return redirect(render_template('index'))
    return render_template('login.html', form = form)

#@# Logout
@app.route('/logout')
def logout():
    return render_template('logout.html')