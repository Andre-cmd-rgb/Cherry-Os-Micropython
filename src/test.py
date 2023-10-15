from microdot import Microdot
import machine
import gc

app = Microdot()


def ram():
    gc.collect()
    return gc.mem_free() / 1024 / 1024
    

# Define a dictionary to store authorized usernames and passwords https://microdot.readthedocs.io/en/latest/intro.html#   http://192.168.178.127:5000/   

app = Microdot()

# Define a dictionary to store authorized usernames and passwords
authorized_users = {
    'andrea': 'hi'
}

# Variable to track if the user is logged in
logged_in = False

# Function to get free RAM information
def get_free_ram():
    return micropython.mem_info()[0]

# HTML form for login
login_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        .login-container {
            text-align: center;
            max-width: 300px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>
        <form method="post" action="/login">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br><br>
            <input type="submit" value="Login">
        </form>
    </div>
</body>
</html>
"""

# Home page HTML template with free RAM information
home_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h2>Welcome, Andrea!</h2>
    <p>Free RAM: {free_ram:.3f} MB</p>
    <a href="/logout">Logout</a>
</body>
</html>
"""

@app.route('/')
def index(request):
    global logged_in
    if logged_in:
        return home_page.format(free_ram=ram()), 200, {'Content-Type': 'text/html'}
    else:
        return login_form, 202, {'Content-Type': 'text/html'}

@app.route('/login', methods=['POST'])
def login(request):
    global logged_in
    data = request.form
    username = data.get('username', None)
    password = data.get('password', None)

    if username is not None and password is not None:
        if authorized_users.get(username) == password:
            logged_in = True
            return home_page.format(free_ram=ram()), 200, {'Content-Type': 'text/html'}

    return 'Login failed. Please check your credentials.', 401

@app.route('/logout')
def logout(request):
    global logged_in
    logged_in = False
    return login_form, 202, {'Content-Type': 'text/html'}

@app.errorhandler(404)
def not_found(request):
    return {'error': 'resource not found'}, 404

@app.get('/shutdown')
def shutdown(request):
    if logged_in:
        request.app.shutdown()
        return 'The server is shutting down...'
    else:
        return 'You need to log in to access this page.', 401


gc.collect()

app.run()
