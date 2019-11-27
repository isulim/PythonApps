from flask import Flask, render_template, request, send_file, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from send_mail import send_email
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://wpivnlbekaexqe:172ff3baa24fb18b87267dc7f325d3fd65ca6e97e57009f45fce1ad3408eb472@ec2-54-235-104-136.compute-1.amazonaws.com:5432/devdqpo99sbden?sslmode=require'
sess = Session()
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Float)

    def __init__(self, email, height):
        self.email = email
        self.height = height


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        file = request.files["file"]
        file.save(secure_filename("uploaded_" + file.filename))
        session['filename'] = "uploaded_" + file.filename
        with open("uploaded_" + file.filename, "a") as f:
            f.write("This is added.")
        return render_template("index.html", btn="download.html")


@app.route("/download", methods=['GET'])
def download():
    return send_file(session['filename'], attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == '__main__':
    app.secret_key = "secretkey"
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)

    app.run(debug=True)
