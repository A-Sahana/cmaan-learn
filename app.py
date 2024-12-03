from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import secrets 

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


# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        # e.g., validate user credentials
        return redirect(url_for('home'))  # Redirect to home after login
    return render_template('login.html')

# Route for the profile completion page
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # Handle profile completion logic here
        # e.g., save user profile information
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
        mysql.connection.commit()
        cursor.close()
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
        flash("User already exists. Please log in.")
        return redirect(url_for('bussiness_login'))
    
    # Hash password for security
    hashed_password = generate_password_hash(password)
    
    # Insert new user into database
    cursor.execute(
        "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
        (username, email, hashed_password)
    )
    mysql.connection.commit()
    
    flash("Registration successful. Please log in.")
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
        
        if user['is_new_user']:
            cursor.execute("UPDATE users SET is_new_user = FALSE WHERE id = %s", (user['id'],))
            mysql.connection.commit()  # Commit the transaction
            cursor.close()  # Close the cursor
            return redirect(url_for('get_started'))
        else:
            cursor.close()  # Close the cursor
            return redirect(url_for('choose'))
    else:
        flash("Invalid email or password.")
        cursor.close()  # Close the cursor
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


@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    ref_id = request.args.get('ref')  # Referral ID from the shared link
    ref_username = request.args.get('user')  # Referrer's username from the shared link

    if request.method == 'POST':
        email = request.form['email']  # Assume this is collected on the enroll form

        # Update referral record and earnings
        cursor = mysql.connection.cursor()
        
        # Check if the referral exists and update it as enrolled
        cursor.execute('''
            UPDATE referrals 
            SET referred_user_email = %s, enrolled = TRUE 
            WHERE referral_id = %s AND referrer_username = %s
        ''', (email, ref_id, ref_username))
        
        # Update referrer's earnings by ₹499
        cursor.execute('''
            INSERT INTO earnings (username, total_earnings)
            VALUES (%s, 499)
            ON DUPLICATE KEY UPDATE total_earnings = total_earnings + 499
        ''', (ref_username,))
        
        mysql.connection.commit()
        cursor.close()
        
        flash("Enrollment successful! The referrer has earned ₹499.")
        return redirect(url_for('fullstack'))  # Redirect to the earnings page
    
    return render_template('fullstack.html')  # Render the enrollment page for GET requests



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

@app.route('/fsm')
def fsm():
    return render_template('fsm.html')

@app.route('/bd', methods=['GET', 'POST'])
def bd():
    return render_template('bd.html')


if __name__ == '__main__':
    app.run(debug=True)