from flask import Flask,request,url_for,render_template,redirect
from backend import articles

Articles = articles()

app = Flask(__name__, static_url_path="/static")

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


@app.route("/articles/<int:id>/")
def article(id):
    # try: 
    return render_template("article.html", id = id, article=Articles[id-1] , a = Articles)
    # except Exception:
    #     return "404" 


if __name__ == "__main__":
    app.run(debug=True)