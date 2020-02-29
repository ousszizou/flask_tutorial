from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    posts = ['post1','post2','post3','post4','post5']
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)

# {{% ... %}} => used to execute statements such as for-loops
# {{ ... }} => used to print the result of the expression to the template
