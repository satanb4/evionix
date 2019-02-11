from flask import Flask,request,url_for,render_template,redirect
from backend import articles

Articles = articles()

app = Flask(__name__, static_url_path="/static")

@app.route("/", methods = ["GET","POST"])
def home():
    if request.method == 'POST':
        name = request.form.get("contactName")
        mail = request.form.get("contactEmail")
        subject = request.form.get("contactEmail")
        message = request.form.get("contactMessage")
    return render_template("index.html", article=Articles)

@app.route("/form", methods = ['GET','POST'])
def contact():
    return None



if __name__ == "__main__":
    app.run(debug=True)