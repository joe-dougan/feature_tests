from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for demonstration
users = [
    {"id": 1, "username": "john", "email": "john@example.com", "favourite_colour": "pink"},
    {"id": 2, "username": "jane", "email": "jane@example.com", "favourite_colour": "red"},
    {"id": 3, "username": "alice", "email": "alice@example.com", "favourite_colour": "green"}
]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and len(users) < 10:
        username = request.form['username']
        email = request.form['email']
        favourite_colour = request.form['favourite_colour']
        if username and email and favourite_colour:
            new_user = {
                'id': len(users) + 1,
                'username': username,
                'email': email,
                'favourite_colour': favourite_colour
            }
            users.append(new_user)
    return render_template('index.html', users=users)


@app.route('/users/<id>', methods=['GET'])
def user_details(id):
    user = next((user for user in users if user['id'] == int(id)), None)
    return render_template('user_details.html', user=user)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
