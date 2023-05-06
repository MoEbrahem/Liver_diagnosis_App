from flask import Flask, jsonify, request
import pickle
import numpy as np
model = pickle.load(open('RandomForest-model.pkl', 'rb'))

app = Flask(__name__,)


@app.route('/')
def home():
    return "Hello World!"


@app.route('/predict', methods=['POST'])
def predict():
        Age = request.form.get('Age')
        Gender = request.form.get('Gender')
        Total_Bilirubin = request.form.get('Total_Bilirubin')
        Direct_Bilirubin = request.form.get('Direct_Bilirubin')
        Alkaline_Phosphotase = request.form.get('Alkaline_Phosphotase')
        Alamine_Aminotransferase = request.form.get('Alamine_Aminotransferase')
        Aspartate_Aminotransferase = request.form.get('Aspartate_Aminotransferase')
        Total_Protiens = request.form.get('Total_Protiens')
        Albumin = request.form.get('Albumin')
        Albumin_and_Globulin_Ratio = request.form.get('Albumin_and_Globulin_Ratio')

        input_query = np.array([[Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase,Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])

        result = model.predict(input_query)[0]

        return jsonify({'placement ': str(result)})


if __name__ == '__main__':
    app.run(debug=True)
