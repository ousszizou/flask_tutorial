from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    title = 'Jinja2 tutorial by algorithm'
    tutorials = ['flask tutorial', 'Jinja2 tutorial', 'python tutorial', 'django tutorial']

    return render_template('index.html', title=title, tutos=tutorials)

if __name__ == '__main__':
    app.run(debug=True)
