#!/usr/bin/env python3

from flask import Flask
from flask import url_for
from flask import redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/user/<username>')
def user_index(username):
    print('User-Agent:', request.headers.get('User-Agent'))
    print('time:', request.args.get('time'))
    print('q:', request.args.get('q'))
    print('Q:', request.args.getlist('Q'))
    return 'Hello {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.route('/test')
def test():
    print(url_for('index'))
    print(url_for('user_index', username='shixiaolou'))
    print(url_for('show_post', post_id=1,_external=True))
    print(url_for('show_post', post_id=2, q='python 03'))
    print(url_for('show_post', post_id=2, q='pythonok'))
    print(url_for('show_post', post_id=2, _anchor='a'))
    return 'test'

@app.route('/register', methods=['GET','POST'])
def register():
    print('method:', request.method)
    print('name:', request.form.get('name'))
    print('password:', request.form.get('password'))
    print('hobbies:', request.form.getlist('hobbies'))
    print('age:', request.form.get('age', default=18))
    return 'registered successfully!'

@app.route('/<username>')
def hello(username):
    if username == 'shixiaolou':
        return 'hello {}'.format(username)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
