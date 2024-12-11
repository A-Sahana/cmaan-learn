from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import secrets 
import MySQLdb.cursors
import os


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.secret_key = "34de185b4e78f74a43b8ce44c51f3d72"
app.debug = True 

# Configure MySQL database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Avenger*160'
app.config['MYSQL_DB'] = 'cmaan_learn'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize MySQL
mysql = MySQL(app)

bcrypt = Bcrypt(app)



# Route for the home page
@app.route('/')
def home():
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])
    return render_template('home.html')

 
@app.route('/logout')
def logout():
    # Clear the session
    session.pop('loggedin', None)
    session.pop('username', None)
    session.pop('id', None)
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        action = request.form.get('action')  # Get the 'action' field from the form

        if action == 'register':
            # Handle Registration
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']

            # Hash the password
            password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

            # Insert data into the database
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO login_register (username, email, password_hash) VALUES (%s, %s, %s)',
                        (username, email, password_hash))
            mysql.connection.commit()

            # Fetch the newly created user to set up the session
            cursor.execute('SELECT * FROM login_register WHERE email = %s', [email])
            user = cursor.fetchone()
            cursor.close()

            if user:
                # Set up session
                session['loggedin'] = True
                session['id'] = user['id']
                session['username'] = user['username']
                flash('Registration successful! You are now logged in.', 'success')
                return redirect(url_for('home'))
            else:
                flash('Registration failed. Please try again.', 'danger')
                return redirect(url_for('login'))

        elif action == 'login':
            # Handle Login
            email = request.form['email']
            password = request.form['password']

            # Verify user credentials
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM login_register WHERE email = %s', [email])
            user = cursor.fetchone()
            cursor.close()

            if user and bcrypt.check_password_hash(user['password_hash'], password):
                session['loggedin'] = True
                session['id'] = user['id']
                session['username'] = user['username']
                return redirect(url_for('home'))
            else:
                flash('Invalid email or password. Please try again.', 'danger')
                return redirect(url_for('login'))

    return render_template('login.html')



@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'loggedin' not in session:
        return redirect(url_for('login'))  # Ensure user is logged in
    
    if request.method == 'POST':
        user_id = session['id']
        about = request.form['about']
        job_role = request.form['job_role']
        university = request.form['university']
        cgpa = request.form['cgpa']
        linkedin = request.form['linkedin']
        location = request.form['location']
        
        # Handle file upload for CV
        cv = request.files['cv']
        if cv:
            cv_filename = secure_filename(cv.filename)
            cv.save(os.path.join('static/uploads/cv', cv_filename))
        else:
            cv_filename = None  # Or set to a default value
        
        # Insert or update profile information into the database
        cursor = mysql.connection.cursor()
        
        cursor.execute("""
            INSERT INTO profiles (user_id, about, job_role, university, cgpa, linkedin, location, cv_filename)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                about = %s, job_role = %s, university = %s, cgpa = %s, linkedin = %s, location = %s, cv_filename = %s
        """, (user_id, about, job_role, university, cgpa, linkedin, location, cv_filename, 
              about, job_role, university, cgpa, linkedin, location, cv_filename))
        
        mysql.connection.commit()
        cursor.close()

        flash('Profile completed successfully!', 'success')
        return redirect(url_for('courses'))  # Redirect to the courses page

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

@app.route('/teach')
def teach():
    return render_template('teach.html')

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
        
        # Update user's `has_filled_get_started` status
        cursor.execute("UPDATE users SET has_filled_get_started = TRUE WHERE email = %s", (email,))
        mysql.connection.commit()
        cursor.close()
        
        # Ensure session remains active after get_started
        session['username'] = username
        session['email'] = email
        
    return redirect(url_for('choose'))


@app.route('/bussiness_register', methods=['POST'])
def bussiness_register():
    cursor = mysql.connection.cursor()
    username = request.form['name']
    email = request.form['email']
    password = request.form['password']
    
    # Check if user already exists
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        return redirect(url_for('bussiness'))
    
    # Hash password for security
    hashed_password = generate_password_hash(password)
    
    # Insert new user into database
    cursor.execute(
        "INSERT INTO users (username, email, password, has_filled_get_started) VALUES (%s, %s, %s, %s)",
        (username, email, hashed_password, False)
    )
    mysql.connection.commit()
    
    # Set session after registration
    session['username'] = username
    session['email'] = email
        
    # Redirect to get_started
    cursor.close()
    return redirect(url_for('get_started'))


@app.route('/bussiness_login', methods=['POST'])
def bussiness_login():
    cursor = mysql.connection.cursor()
    email = request.form['email']
    password = request.form['password']
    
    # Find user by email
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    
    if user and check_password_hash(user['password'], password):
        session['username'] = user['username']  # Save username in session
        session['user_id'] = user['id']  # Optionally, save user ID
        
        if not user['has_filled_get_started']:  # Check if user has filled the form
            return redirect(url_for('get_started'))
        else:
            return redirect(url_for('choose'))
    else:
        flash("Invalid email or password.")
        cursor.close()
        return redirect(url_for('bussiness')) 



@app.route('/generate_referral_link', methods=['GET'])
def generate_referral_link():
    if 'username' in session:
        username = session['username']
        course = request.args.get('course', 'default-course')  # Get course name from query params
        referral_id = secrets.token_hex(8)  # Generate a unique referral ID
        referral_link = f"http://127.0.0.1:5000/{course}?ref={referral_id}&user={username}"
        return {'referralLink': referral_link}, 200
    return {'error': 'User not logged in'}, 401






@app.route('/earnings')
def earnings():
    username = session.get('username')  
    
    if not username:
        flash("Please log in to view your earnings.")
        return redirect(url_for('login'))
    
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT total_earnings FROM earnings WHERE username = %s', (username,))
    earnings_data = cursor.fetchone()
    cursor.close()
    
    total_earnings = earnings_data['total_earnings'] if earnings_data else 0
    return render_template('earnings.html', total_earnings=total_earnings)



@app.route('/choose')
def choose():
    return render_template('choose.html')

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

@app.route('/fsc', methods=['GET', 'POST'])
def fsc():
    return render_template('fsc.html')


@app.route('/bd', methods=['GET', 'POST'])
def bd():
    return render_template('bd.html')

@app.route('/paymentf')
def paymentf():
    return render_template('paymentf.html')


@app.route('/paymentb')
def paymentb():
    return render_template('paymentb.html')


@app.route('/fsm1')
def fsm1():
    return render_template('fsm1.html')

@app.route('/fsm2')
def fsm2():
    return render_template('fsm2.html')

@app.route('/fsm3')
def fsm3():
    return render_template('fsm3.html')

@app.route('/fsm4')
def fsm4():
    return render_template('fsm4.html')

@app.route('/fsm5')
def fsm5():
    return render_template('fsm5.html')

@app.route('/fsm6')
def fsm6():
    return render_template('fsm6.html')

@app.route('/fsm7')
def fsm7():
    return render_template('fsm7.html')

@app.route('/fsm8')
def fsm8():
    return render_template('fsm8.html')



if __name__ == '__main__':
    app.run(debug=True)