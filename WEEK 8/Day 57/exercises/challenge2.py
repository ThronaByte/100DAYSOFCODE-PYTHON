from flask import Flask, render_template
import requests
app = Flask(__name__)

AGIFY_API_KEY = "28db30b6eb7e712b9dc3d9e0a5e96164"
GENDERIZE_API_KEY = "ed0af2cb5cbac9129fe2ba553b5a0859"


@app.route('/guess/<name>')
def guess(name):
    age_response = requests.get(f'https://api.agify.io?name={name}')
    age_data = age_response.json()
    age = age_data["age"]

    gender_response = requests.get(f'https://api.genderize.io?name={name}')
    gender_data = gender_response.json()
    gender = gender_data["gender"]


    return render_template('index2.html', name=name, age=age, gender=gender)

if __name__ == '__main__':
    app.run(debug=True)