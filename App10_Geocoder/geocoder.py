from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/geocode", methods=['POST'])
def geocode():
    if request.method == 'POST':
        file = request.files['file']
        return render_template("geocode.html")
    return render_template("index.html", 
    text="Something went wrong.<br>Check your file and try again please.")

if __name__ == "__main__":
    app.run(debug=True)
