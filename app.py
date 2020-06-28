from flask import Flask, request, render_template, redirect, request, url_for, session
from flask_mysqldb import MySQL 

app = Flask(__name__)
app.secret_key = "S689Gjysjms0"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'tiger'
app.config['MYSQL_DB'] = 'hospital_management_system'
mysql = MySQL(app)

@app.route("/")
def login():
<<<<<<< HEAD
    return render_template("create_patient.html")
=======
    if request.method == 'POST':
        username = request.form.get('username')  # access the data inside 
        password = request.form.get('password')
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM userstore WHERE login_id = %s AND password = %s', (username, password,))
        results = cur.fetchall()
        if results:
            session['username'] = username
            cur.execute('''update userstore set last_view=current_timestamp where login_id= %s''',(username,))
            mysql.connection.commit()
            return redirect(url_for('home'))
    return render_template("login.html")

@app.route("/home")
def home():
        return render_template("hms.html")
>>>>>>> aa27f32dda7658510c027088bedaf29b0edf3409
