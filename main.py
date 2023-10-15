from flask import Flask, render_template, request, url_for

app = Flask(__name__ , template_folder="templates")


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
    return render_template('test.html')

if __name__ ==  "__main__":
    app.run(debug=True)