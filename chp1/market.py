from chp1 import app


@app.route("/")
def hello_world():
 return '<h1>Hello world</h1>'


@app.route('/about/<username>')
def about_page(username):
 return f'<h1>This is the about page of {username}'