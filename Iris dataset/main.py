from flask import Flask, render_template, request

from project_app.utils import SpeciesFlower

app = Flask(__name__)

@app.route("/") 
def hello_flask():
    print("Species Found")   
    return render_template("index.htsml")

@app.route("/predict_species", methods = ["POST", "GET"])

def species_info():
    if request.method == "GET":
        print("GET Method")

        SepalLengthCm = float(request.args.get('SepalLengthCm'))
        SepalWidthCm = float(request.args.get('SepalWidthCm'))
        PetalLengthCm = float(request.args.get('PetalLengthCm'))
        PetalWidthCm  = float(request.args.get('PetalWidthCm'))


        species = SpeciesFlower(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)

        species_pred = species.get_predicted_species()

        return render_template("index.html", prediction = species_pred)
    

print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5005, debug = False)