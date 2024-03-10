from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo.mongo_client import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management and flash messaging

# MongoDB setup
uri = "mongodb+srv://admin:admin@cluster0.vgkg7px.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client['your_database_name']  # Explicitly specify your database name here
users_collection = db.users
libdata = db.bookData

@app.route('/')
def home():
    return render_template("Homepage.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        phone = request.form.get('phone')


        username = request.form.get('username')
        email = request.form.get('email')  # Assuming you want to capture this too
        password = request.form.get('password')
        if users_collection.find_one({'username': username}):
            flash('Username already exists!')
            return redirect(url_for('signup'))
        elif users_collection.find_one({'email': email}):
            flash('Email already exists!')
            return redirect(url_for('signup'))
        else:
            hashed_password = generate_password_hash(password)
            users_collection.insert_one({'username': username, 'email': email, 'password': hashed_password,'first_name':first_name,'last_name':last_name,'phone':phone})
            flash('User registered successfully!')
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = users_collection.find_one({'username': username})
        if user and check_password_hash(user['password'], password):
            flash('Logged in successfully!')
            return redirect(url_for('home'))  # Redirect to a dashboard or home page as needed
        else:
            flash('Invalid username or password!')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
