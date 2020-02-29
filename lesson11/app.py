from flask import Flask, render_template, make_response, request, url_for

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cookie')
def cookie():
    if not(request.cookies.get('foo')):
        res = make_response('setting a cookie')
        res.set_cookie('foo', 'bar', max_age=24*60*60*1000)
    else:
        res = make_response("Value of cookie foo is <b> {} </b>".format(request.cookies['foo']))
    return res

@app.route('/delete_cookie')
def delete():
    res = make_response("Cookie Removed")
    res.set_cookie('foo', 'bar', max_age=0)
    return res

@app.route('/article/', methods=['POST', 'GET'])
def article():
    if request.method == 'POST':
        print(request.form)
        res = make_response("")
        res.set_cookie("font", request.form.get('font'), 60*60*24*15)
        res.headers['location'] = url_for('article')
        return res, 302
    return render_template('article.html')
