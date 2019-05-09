from flask import Flask,request,url_for,render_template,redirect
from app.backend import articles
from app.forms import LoginForm

Articles = articles()

@app.route("/")
def home():
    return render_template("index.html", article=Articles)

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

@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data,form.remember_me.data
        ))
    return render_template("login.html")

@app.route("/articles/<int:id>/")
def article(id):
    # try: 
    return render_template("article.html", id = id, article=Articles[id-1] , a = Articles)
    # except Exception:
    #     return "404" 
