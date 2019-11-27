from flask import Flask, render_template, request, send_file, session
from werkzeug.utils import secure_filename
from pandas import read_csv
from geopy.geocoders import ArcGIS

app = Flask(__name__)
app.secret_key = 'most_secret_key_ever_made'


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/geocode", methods=['POST'])
def geocode():
    if request.method == 'POST':
        # Get CSV file from request, save and get data
        file = request.files['file']
        file.save(secure_filename("raw_" + file.filename))
        data = read_csv("raw_" + file.filename)

        # Try to save column 'Address' or 'address' to a variable
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

        # Create ArcGIS object,
        # apply methods on pandas DF - get None coordinates, if geocoding not possible
        # export processed data to CSV
        arcgis = ArcGIS()
        coords = addresses.apply(arcgis.geocode)
        data['Latitude'] = coords.apply(lambda x: x.latitude if x is not None else None)
        data['Longitude'] = coords.apply(lambda x: x.longitude if x is not None else None)
        data.to_csv("geocoded_" + file.filename)

        # Save filename in session to download
        session['filename'] = "geocoded_" + file.filename

        return render_template("geocode.html", table=data.to_html())
    return render_template("index.html", text="Something went wrong."
                                              "<br>Check your file and "
                                              "try again please.")


@app.route("/download")
def download():
    return send_file(session.get('filename'), as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
