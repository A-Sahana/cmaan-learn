from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = 'Avenger*160'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'cmaan_learn'

mysql = MySQL(app)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        return redirect(url_for('home'))
    return render_template('login.html')

# Route for the profile completion page
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # Handle profile completion logic here
        return redirect(url_for('home'))
    return render_template('profile.html')

# Route for the courses page
@app.route('/courses')
def courses():
    return render_template('courses.html')

# Route for specific course pages
@app.route('/fullstack')
def fullstack():
    return render_template('fullstack.html')

@app.route('/backend')
def backend():
    return render_template('backend.html')

@app.route('/graphics')
def graphics():
    return render_template('graphics.html')

@app.route('/android')
def android():
    return render_template('android.html')

@app.route('/automation')
def automation():
    return render_template('automation.html')

@app.route('/ios')
def ios():
    return render_template('ios.html')

@app.route('/cloud')
def cloud():
    return render_template('cloud.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')

@app.route('/telecalling')
def telecalling():
    return render_template('telecalling.html')

@app.route('/hr')
def hr():
    return render_template('hr.html')

# Route for the become tutor page
@app.route('/tutor')
def tutor():
    return render_template('tutor.html')

@app.route('/bussiness')
def bussiness():
    return render_template('bussiness.html')

@app.route('/get_started')
def get_started():
    return render_template('get_started.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        phone = request.form['phone']
        username = request.form['username']
        course_interest = request.form['courseInterest']
        referral_goal = int(request.form['referralGoal'])
        comments = request.form.get('comments', '')

        # Insert form data into MySQL
        cursor = mysql.connection.cursor()
        cursor.execute('''
            INSERT INTO affiliates (first_name, last_name, email, phone, username, course_interest, referral_goal, comments)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (first_name, last_name, email, phone, username, course_interest, referral_goal, comments))
        mysql.connection.commit()
        cursor.close()
    return redirect(url_for('choose'))

@app.route('/choose')
def choose():
    return render_template('choose.html')

# Routes for business-specific course pages
@app.route('/business_fullstack')
def business_fullstack():
    return render_template('business_fullstack.html')

@app.route('/business_backend')
def business_backend():
    return render_template('business_backend.html')

@app.route('/business_graphics')
def business_graphics():
    return render_template('business_graphics.html')

@app.route('/business_android')
def business_android():
    return render_template('business_android.html')

@app.route('/business_automation')
def business_automation():
    return render_template('business_automation.html')

@app.route('/business_ios')
def business_ios():
    return render_template('business_ios.html')

@app.route('/business_cloud')
def business_cloud():
    return render_template('business_cloud.html')

@app.route('/business_sales')
def business_sales():
    return render_template('business_sales.html')

@app.route('/business_telecalling')
def business_telecalling():
    return render_template('business_telecalling.html')

@app.route('/business_hr')
def business_hr():
    return render_template('business_hr.html')

# Route for reviews page
@app.route('/review')
def review():
    return render_template('review.html')

if __name__ == '__main__':
    app.run(debug=True)
