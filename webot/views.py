"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from webot import app

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ["zip"]

@app.route('/')
def root():
    return redirect(url_for("page1"))

@app.route('/upload', methods=["GET","POST"])
def upload():
    #ref01 = request.args.get('ref01', default = 0, type = int)
    #if ref01 == 0: return redirect(url_for("page1"))
    print("upload>>")
    b_redir = False
    if request.method == "POST":
        print(request.files)
        if "file" in request.files:
            file = request.files["file"]
            if file.filename != "":
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    #print(file.read())
                    print(filename)
                    b_redir = True


    print("upload<<")
    if b_redir:
        print("redirect...")
        #Redirect on Ajax calls doesn't work, browser doesn't handle it.
        #return redirect(url_for("result"), code=302)
        return jsonify({"redirect": "/result"})
    else:
        return redirect(url_for("page1"))

@app.route('/page1', methods=["GET"])
def page1():
    return redirect(url_for("uploadfile3"))

@app.route('/uploadfile0', methods=["GET"])
def uploadfile0():
    """Renders the home page."""
    return render_template(
        'uploadfile0.html',
        title='Analyzer',
        year=datetime.now().year,
    )

@app.route('/uploadfile3', methods=["GET"])
def uploadfile3():
    """Renders the home page."""
    return render_template(
        'uploadfile3.html',
        title='Analyzer',
        year=datetime.now().year,
    )

@app.route('/uploadfile4', methods=["GET"])
def uploadfile4():
    """Renders the home page."""
    return render_template(
        'uploadfile4.html',
        title='Analyzer',
        year=datetime.now().year,
    )

@app.route('/result')
def result():
    """Renders the page."""
    return render_template(
        'result.html',
        title='Results',
        year=datetime.now().year,
    )

@app.route('/page2')
def page2():
    """Renders the page."""
    return render_template(
        'page2.html',
        title='Document',
        year=datetime.now().year,
    )

@app.route('/page3')
def page3():
    """Renders the page."""
    return render_template(
        'page3.html',
        title='Contact',
        year=datetime.now().year,
    )

#@app.route('/')
#@app.route('/home')
#def home():
#    """Renders the home page."""
#    return render_template(
#        'index.html',
#        title='Home Page',
#        year=datetime.now().year,
#    )

#@app.route('/contact')
#def contact():
#    """Renders the contact page."""
#    return render_template(
#        'contact.html',
#        title='Contact',
#        year=datetime.now().year,
#        message='Your contact page.'
#    )

#@app.route('/about')
#def about():
#    """Renders the about page."""
#    return render_template(
#        'about.html',
#        title='About',
#        year=datetime.now().year,
#        message='Your application description page.'
#    )
