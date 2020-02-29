from flask import Flask, request , redirect, url_for
app = Flask(__name__)

# # # http://localhost:5000/
# @app.route('/')
# def home():
#     return 'Home page'
#
# # # http://localhost:5000/about
# @app.route('/about')
# def about():
#     return 'About page'
#
# # # http://localhost:5000/user/algorithm
# @app.route('/user/<username>')
# def show_user(username):
#     # show the user profile for that user
#     return 'User {}'.format(username)
#
# # # http://localhost:5000/post/1
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post {}'.format(post_id)
#
# # # http://localhost:5000/path/blog/python
# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath {}'.format(subpath)
#
# # # http://localhost:5000/members?first_name=Algorithm&last_name=zizou
# @app.route('/members')
# def show_user_profile():
#     first_name = request.args.get('first_name')
#     last_name = request.args.get('last_name')
#     return "<h3>First Name: {} <br>Last Name: {}</h3>".format(first_name, last_name)




@app.route('/administration')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello {} as Guest'.format(guest)

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':

      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))




@app.route('/algorithm', methods = ['POST', 'GET'])
def algorithm():
    if request.method == 'POST':
        return 'you are using POST method'
    else:
        return 'you are using GET method (default http method)'




if __name__ == '__main__':
    app.run()
