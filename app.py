from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from forms import * 
from flask_mysqldb import MySQL
app = Flask(__name__)


# database configurations 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'huncho'
app.config['MYSQL_PASSWORD']= 'c11h28no3'
app.config['MYSQL_DB'] = 'tender'

mysql = MySQL(app)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Drugs"

@app.route('/supplier', methods=['GET', 'POST'])
def supplier():
    
    form = SupplierForm()
    if request.method == 'POST':
        data = request.form
        # import ipdb; ipdb.set_trace()
        suppliername = data['suppliername']
        tendertype = data["tendertype"]
        contactemail = data['contactemail']
        phonenumber = data["phonenumber"]
        technicalrequirement = data["technicalrequirement"]
        mandatoryrequirement = data["mandatoryrequirement"]

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO supplier (suppliername, tendertype, contactemail, phonenumber, technicalrequirement, mandatoryrequirement) VALUE (%s, %s, %s, %s, %s, %s)",(suppliername, tendertype, contactemail, phonenumber, technicalrequirement, mandatoryrequirement))
        mysql.connection.commit()
        cur.close()
        return 'success'
    else:
        return render_template('supplier.html', form=form)

    return render_template('supplier.html', name='supplier', form=form)

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong credentials')
        return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)