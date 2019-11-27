from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from pandas import read_csv
from geopy.geocoders import ArcGIS

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/geocode", methods=['POST'])
def geocode():
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename("raw_" + file.filename))
        data = read_csv("raw_" + file.filename)

        try:
            addresses = data.loc[:, 'Address']
        except KeyError:
            try:
                addresses = data.loc[:, 'address']
            except KeyError:
                return render_template("index.html", text="""<h2>ERROR</h2>
                                                             <h4>No column named 
                                                             <i>Address</i> or <i>address</i> 
                                                             found in your file.<br>
                                                             Please try again.</h4>""")

        arcgis = ArcGIS()
        latitude = []
        longitude = []
        for row in addresses:
            location = arcgis.geocode(row)
            latitude.append(location.latitude)
            longitude.append(location.longitude)

        data['Latitude'] = latitude
        data['Longitude'] = longitude

        data.to_csv("geocoded_" + file.filename)

        return render_template("geocode.html", table=data.to_html())
    return render_template("index.html", text="Something went wrong."
                                              "<br>Check your file and "
                                              "try again please.")


if __name__ == "__main__":
    app.run(debug=True)
