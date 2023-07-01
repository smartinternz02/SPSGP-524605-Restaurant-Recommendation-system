from flask import Flask, render_template, request
import pickle 
import pandas as pd

app = Flask(__name__)

# Load the pickled object from the file
loaded_model = pickle.load(open("D:\\Flask\\model.pkl", "rb"))

# Access the 'recommend' attribute from the loaded object
recommendation = loaded_model.recommend()


@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    cuisine = request.form.get('cuisine')
    location = request.form.get('location')



    recommendations = get_recommendations(cuisine, location, dataset)

    return render_template('result1.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True, port=5000)





