"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from webot import app

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ["zip"]

@app.route('/')
@app.route('/page1', methods=["GET", "POST"])
def page1():
    if request.method == "POST":
        if "file" in request.files:
            file = request.files["file"]
            if file.filename != "":
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    print(file.read())
                    return render_template(
                        'result.html',
                        title='Result',
                        year=datetime.now().year,
                    )
    """Renders the home page."""
    return render_template(
        'page1.html',
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
