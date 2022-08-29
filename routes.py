from app import app
from flask import render_template, redirect, url_for
import forms


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/findid', methods = ['GET', 'POST'])
def findid():
    form = forms.FindIdForm()
    if form.validate_on_submit():
        return 
    return render_template('findid.html', form = form)

@app.route('/findname', methods = ['GET', 'POST'])
def findname():
    form = forms.FindNameForm()
    if form.validate_on_submit():
        return 
    return render_template('findname.html', form = form)

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = forms.AddUserForm()
    if form.validate_on_submit():
        return 
    return render_template('add.html', form = form)

@app.route('/update', methods = ['GET', 'POST'])
def update():
    form = forms.UpdateUserForm()
    if form.validate_on_submit():
        return 
    return render_template('update.html', form = form)

@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    form = forms.DeleteUserForm()
    if form.validate_on_submit():
        return 
    return render_template('delete.html', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = forms.LoginUserForm()
    if form.validate_on_submit():        
        return redirect(render_template('index'))
    return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    return render_template('logout.html')