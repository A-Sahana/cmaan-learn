from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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

@app.route('/bussiness')  # Corrected typo here
def bussiness():
    return render_template('bussiness.html')

@app.route('/get_started')
def get_started():
    return render_template('get_started.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Process form data here
    # e.g., data = request.form['field_name']

    # For demonstration, simply redirect to choose
    return redirect(url_for('choose'))

@app.route('/choose')
def choose():
    return render_template('choose.html')

# Route for reviews page
@app.route('/review')
def review():
    return render_template('review.html')

if __name__ == '__main__':
    app.run(debug=True)
