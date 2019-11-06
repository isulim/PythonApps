from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/collector'
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
        email_ = request.form.get("email")
        height_ = request.form.get("height")
        if db.session.query(Data).filter(Data.email == email_).count() == 0:
            data = Data(email_, height_)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
        else:
            return render_template("index.html", message="Seems like you already submitted a form.")


if __name__ == '__main__':
    app.run(debug=True)
