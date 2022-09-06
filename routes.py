from app import app
from flask import render_template, redirect, url_for, flash, request
import forms
from db import *

edit_complete = False
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
    if request.method == "POST":
        add_new = "INSERT INTO users(id, first_name, last_name, gender, email, username, ip_address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        id = form.id.data
        first_name = form.firstname.data
        last_name = form.lastname.data        
        gender = form.gender.data
        email = form.email.data
        username = form.username.data
        ip_address = form.ipaddress.data
        value = (id, first_name, last_name, gender, email, username, ip_address)
        cursor.execute(add_new, value)
        conn.commit()
        rowcount = str(cursor.rowcount)
        add_new_result_sql = "SELECT * FROM users WHERE id =%s"
        id_new = (id,)
        cursor.execute(add_new_result_sql,id_new)
        add_result = cursor.fetchall()
        add_message = 'New User added: {}'.format(add_result)
        modified = 'Rows modified: {}'.format(rowcount)
        flash(modified) 
        flash(add_message)
        return render_template('add.html', form=form, rowcount=rowcount, add_result=add_result)
    return render_template('add.html', form = form)

#@# Update existing user
@app.route('/update', methods = ['GET', 'POST'])
def update():
    form = forms.UpdateUserForm()
    if request.method == "GET":
        if edit_complete == True:
            retrieve_id_sql = "SELECT id FROM update_table WHERE session = 1"
            cursor.execute(retrieve_id_sql)
            results = cursor.fetchall()
            for result in results:
                for savedid in result:
                    id = savedid
                    break          
            value = (id, )
            update_sql = "SELECT * FROM users WHERE id = %s"
            cursor.execute(update_sql, value)
            results = cursor.fetchall()
            for result in results:
                #for field in result:
                id = result[0]
                firstname = result[1]
                lastname = result[2]
                gender = result[3]
                email = result[4]
                username = result[5]
                ipaddress = result[6]
            return render_template('update.html', form=form, id=id, firstname=firstname, lastname=lastname, gender=gender, email=email, username=username,  ipaddress=ipaddress)
        return render_template('update.html', form = form)
    if request.method == "POST":
        # Saves ID and searches for user.
        if form.id.data != None:
            id = form.id.data        
            value = (id,)
            saveid_sql = "UPDATE update_table SET id = %s WHERE session = 1"
            cursor.execute(saveid_sql, value)
            conn.commit()         
            search_sql = "SELECT * FROM users WHERE id = %s"
            cursor.execute(search_sql, value)
            result = cursor.fetchall()

        if request.form.get("update") == "yes":
            #Get saved ID from Database
            retrieve_id_sql = "SELECT id FROM update_table WHERE session = 1"
            cursor.execute(retrieve_id_sql)
            results = cursor.fetchall()
            for result in results:
                for savedid in result:
                    id = savedid
                    break          
            value = (id, )

            update_sql = "SELECT * FROM users WHERE id = %s"
            cursor.execute(update_sql, value)
            results = cursor.fetchall()
            for result in results:
                #for field in result:
                id = result[0]
                firstname = result[1]
                lastname = result[2]
                gender = result[3]
                email = result[4]
                username = result[5]
                ipaddress = result[6]
            return render_template('update.html', form=form, id=id, firstname=firstname, lastname=lastname, gender=gender, email=email, username=username,  ipaddress=ipaddress)

        elif request.form.get("update") == "no":
            return render_template('update.html', form=form)

        return render_template('update.html',form=form, result=result)          
    return render_template('update.html', form = form)

#@# Edit user after update request.
@app.route('/edit', methods= ['GET', 'POST'])
def edit():
    form = forms.EditUserForm()
    if request.method == "POST":
        # Save field to Database received from update.html 'edit' buttons.
        if request.form.get('column'):
            column_edit = request.form.get('column')  
            value = (column_edit,)
            savecolumn_sql = "UPDATE edit_table SET column_header = %s WHERE session = 1"
            cursor.execute(savecolumn_sql, value)
            conn.commit()         
            return render_template('edit.html', form=form, column_edit=column_edit)
        #Update Field in record
        elif form.update.data:
            #Get saved field from Database         
            retrieve_column_sql = "SELECT column_header FROM edit_table WHERE session = 1"
            cursor.execute(retrieve_column_sql)
            results = cursor.fetchall()
            for result in results:
                for savedcolumn in result:
                    column = savedcolumn
                    break          
            
            #Get saved ID from Database
            retrieve_id_sql = "SELECT id FROM update_table WHERE session = 1"
            cursor.execute(retrieve_id_sql)
            results = cursor.fetchall()
            for result in results:
                for savedid in result:
                    id = savedid
                    break

            update = form.update.data
            value = (update, id)
            update_sql = "Update users SET {} = %s WHERE id=%s".format(column)
            cursor.execute(update_sql, value)
            conn.commit()
            flash('Update Successful!')
            return redirect(url_for('update'))
    return render_template('edit.html', form=form)

#@# Delete user
@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    form = forms.DeleteUserForm()    
    if request.method == "POST":
        if form.id.data != None:
            id = form.id.data        
            value = (id,)
            saveid_sql = "UPDATE delete_table SET id = %s WHERE session = 1"
            cursor.execute(saveid_sql, value)
            conn.commit()         
            search_sql = "SELECT * FROM users WHERE id = %s"
            cursor.execute(search_sql, value)
            result = cursor.fetchall()              
        if request.form.get("delete") == "yes":
            retrieve_id_sql = "SELECT id FROM delete_table WHERE session = 1"
            cursor.execute(retrieve_id_sql)
            results = cursor.fetchall()
            for result in results:
                for savedid in result:
                    id = savedid
                    break          
            value = (id, )
            delete_sql = "DELETE FROM users WHERE id = %s"
            cursor.execute(delete_sql, value)
            rowcount = str(cursor.rowcount) 
            conn.commit()
            modified = 'Rows modified: {}'.format(rowcount)
            flash(modified) 
            flash('Record has been deleted!')                 
            return render_template('delete.html', form=form, rowcount=rowcount)
        elif request.form.get("delete") == "no":
            no = "no"
            cursor.execute("ROLLBACK")
            savedid_sql = "SELECT id FROM delete_table WHERE session = 1"
            cursor.execute(savedid_sql)
            results = cursor.fetchall()
            return render_template('delete.html', form=form,no=no, results=results)
        return render_template('delete.html',form=form, result=result)          
    return render_template('delete.html', form = form)

#@# Login user
@app.route('/', methods = ['GET', 'POST'])
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = forms.LoginUserForm()
    error = None
    if request.method == 'POST':
        if form.username.data != 'admin' or \
                form.password.data != 'admin':
            error = 'Invalid credentials'
            flash('Invalid credentials')
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', form=form, error=error)

#@# Logout
@app.route('/logout')
def logout():
    flash('Logout successful. Have a great day!')
    return redirect(url_for('login'))