from flask import *
from flaskwebgui import FlaskUI
app = Flask(__name__)
ui = FlaskUI(app,app_mode=True,)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/sub', methods=['POST', 'GET'])
def nextstep():
    if "page" in request.form:
        return render_template("sex_select.html")
    elif "sex" in request.form:
        return render_template("age_select.html")
    elif "age" in request.form:
        return render_template("select_symptoms.html")
    elif "symptom" in request.form:
        #for demo puproses only
        return render_template("result.html",result="covid-19",percent="50%" , defin="Coronavirus disease 2019 (COVID-19) is an infectious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2).[8] The disease was first identified in December 2019 in Wuhan, the capital of China's Hubei province, and has since spread globally, resulting in the ongoing 2019–20 coronavirus pandemic.[9][10] Common symptoms include fever, cough and shortness of breath.[5] Other symptoms may include fatigue, muscle pain, diarrhoea, sore throat, loss of smell and abdominal pain.[5][11][12] The time from exposure to onset of symptoms is typically around five days, but may range from two to fourteen days.[5][13] While the majority of cases result in mild symptoms, some progress to viral pneumonia and multi-organ failure.[9][14] As of 12 April 2020, more than 1.77 million[7] cases have been reported in over 200 countries and territories,[15] resulting in more than 108,000 deaths.[7] More than 401,000 people have recovered.")
    else:
        return "error"






if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000)