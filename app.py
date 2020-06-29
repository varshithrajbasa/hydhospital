from flask import Flask, request, render_template, redirect, request, url_for, session
from flask_mysqldb import MySQL 

app = Flask(__name__)
app.secret_key = "S689Gjysjms0"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'tiger'
app.config['MYSQL_DB'] = 'hospital_management_system'
mysql = MySQL(app)

@app.route("/", methods=['post', 'get'])
def login():
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

@app.route("/create_patient",methods=['post','get'])
def create_patient():
    if request.method == 'POST':
        ssn_id = int(request.form.get('ssn_id')) 
        patient_name = request.form.get('patient_name')
        patient_age=int(request.form.get('age'))
        patient_admission_date=request.form.get('admission_date')
        patient_bed=request.form.get('bed_type')
        patient_address=request.form.get('address')
        patient_state=request.form.get('state')
        patient_city=request.form.get('city')
        cur = mysql.connection.cursor()
        cur.execute('''insert into patients(patient_ssn_id,patient_name,age,date_of_admission,type_of_bed,address,city,state,status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (ssn_id,patient_name,patient_age,patient_admission_date,patient_bed,patient_address,patient_city,patient_state,patient_city,"active"))
        mysql.connection.commit()
    return render_template("create_patient.html")
