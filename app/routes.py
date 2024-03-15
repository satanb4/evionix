from app import app
from flask import Flask,request,url_for,render_template,redirect,flash
from app.backend import articles
from app.forms import LoginForm

Articles = articles()

@app.route("/")
@app.route("/home")
def home():
    return render_template("index1.html", article=Articles)

@app.route("/form1", methods = ['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get("contactName")
        mail = request.form.get("contactEmail")
        subject = request.form.get("contactSubject")
        message = request.form.get("contactMessage")
    return redirect(url_for("home"))

@app.route("/notify", methods=["POST"])
def mail():
    if request.method == "POST":
        name = request.form.get("dEmail")
    return redirect(url_for("home"))

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data,form.remember_me.data
        ))
    return render_template("login.html", form=form, place = "Login")

@app.route("/articles/<int:id>/")
def article(id):
    # try: 
    return render_template("article.html", id = id, article=Articles[id-1] , a = Articles, place="Blog")
    # except Exception:
    #     return "404" 