from flask import Flask, render_template, request, url_for, jsonify
import pickle
import numpy as np

app = Flask(__name__ , template_folder="templates")
model = pickle.load(open(r"Final2.pkl" ,"rb"))


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("Home.html")

@app.route('/AboutUs', methods=['GET', 'POST'])
def aboutus():
    return render_template('AboutUs.html')

@app.route('/ContactUs', methods=['GET', 'POST'])
def contactus():
    return render_template('ContactUs.html')

@app.route('/HealthTools', methods=['GET', 'POST'])
def healthtools():
    return render_template('HealthTools.html')

@app.route('/ExpertAdv', methods=['GET', 'POST'])
def expertadv():
    return render_template('ExpertAdv.html')

@app.route('/Diet&Exer', methods=['GET', 'POST'])
def dietandexer():
    return render_template('Diet&Exer.html')

@app.route('/Test', methods=['GET', 'POST'])
def test():
    return render_template('prac.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    # Get data from the request
    data = request.get_json().get('data')
    print(data)
    dt1 = int(data[0])
    dt2 = int(data[1])
    dt3 = int(data[2])
    dt4 = int(data[3])
    dt5 = int(data[4])
    dt6 = float(data[5])
    dt7 = float(data[6])
    dt8 = int(data[7])
    dat = (dt1, dt2, dt3, dt4, dt5, dt6, dt7, dt8)
    print(dat)
    # dt = [float(x) for x in dat]
    # print (dt)
    final = np.array([dat])
    print(final)
    prediction = model.predict(final)
    print(prediction)
    res1 = prediction[0]
    if res1 == 0:
        msg = "Worry less! You seem to be absolutely Fit & Fine"
    elif res1 == 1:
        msg = "You are prune to Diabetic Lifestyle. Please look after your habits"
    # output=' in '.join(prediction)
    # print(output)

    # Make predictions using the loaded model (replace this with your actual model logic)
    # prediction = make_prediction(data)

    # Return the prediction as JSON response
    return jsonify({'result': msg})

if __name__ ==  "__main__":
    app.run(debug=True)