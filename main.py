from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user')
def user():
    user_data = {
        'username': 'ユーザー名',
        'icon': 'icon.jpeg'
    }
    return render_template('user.html', user=user_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
