#main.py
from flask import Flask #module to utilized web gui
from flask import render_template, url_for, request #subset of flask module, render_template for rendering html code, url_for is for directing the files and page and request is for recieving data from html gui
#from flaskwebgui import FlaskUI # import FlaskUI, this will transform the web gui app into desktop app
#machine learning libraries
import numpy as np #numerical analysis library of python
from tensorflow import keras #tensorflow, artificial intelligence library of python
from pyfladesk import init_gui
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

if getattr(sys, 'frozen', False):
    template_folder = resource_path('templates')
    static_folder = resource_path('static')
    model_folder = resource_path('model')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)
#ui = FlaskUI(app, width=800, height=600) # add app and parameters
#loading the neural network model
pretrained_model = keras.models.load_model('model.h5') #loading the artificial intelligence model file
#correct answer per subject
science_correct = ['a','c','b','d','d'] #corrected
math_correct = ['a','c','b','d','d'] #corrected
language_correct = ['c','c','a','b','d'] #corrected
socsci_correct = ['c','a','b','d','d'] #corrected
tech_correct = ['b','d','b','a','c'] #corrected
history_correct = ['d','b','c','a','d'] #corrected
pe_correct = ['d','a','b','c','d'] #corrected
humanities_correct = ['a','c','b','d','b'] #corrected
management_correct = ['d','c','a','c','d'] #corrected
arts_correct = ['c','a','b','a','d'] #corrected
college_list = ['College of Engineering and Information Technology','College of Education','College of Economics Management and Development Studies', 'College of Arts and Sciences', 'College of Nursing', 'College of Agriculture Forestry Environment and Natural Resources', 'College of Sports Physical Education and Recreation', 'College of Criminal Justice', 'College of Veterenary Medicine'] #output to be called
@app.route("/")
def hello():  
    return render_template('index.html') #homepage
@app.route("/result", methods=['GET','POST'])
def result():
    #set all score to 0 upon loading
    science_score = 0
    math_score = 0
    language_score = 0
    socsci_score = 0
    tech_score = 0
    history_score = 0
    pe_score = 0
    humanities_score = 0
    management_score = 0
    arts_score = 0
    if request.method == 'POST': #if the recieved method of data is post request, fetch all of its information contained
        user_science = [request.form['science_question1'],request.form['science_question2'],request.form['science_question3'],request.form['science_question4'],request.form['science_question5']]
        user_math = [request.form['math_question1'],request.form['math_question2'],request.form['math_question3'],request.form['math_question4'],request.form['math_question5']]
        user_language = [request.form['language_question1'],request.form['language_question2'],request.form['language_question3'],request.form['language_question4'],request.form['language_question5']]
        user_socsci = [request.form['socsci_question1'],request.form['socsci_question2'],request.form['socsci_question3'],request.form['socsci_question4'],request.form['socsci_question5']]
        user_tech = [request.form['tech_question1'],request.form['tech_question2'],request.form['tech_question3'],request.form['tech_question4'],request.form['tech_question5']]
        user_history = [request.form['history_question1'],request.form['history_question2'],request.form['history_question3'],request.form['history_question4'],request.form['history_question5']]
        user_pe = [request.form['pe_question1'],request.form['pe_question2'],request.form['pe_question3'],request.form['pe_question4'],request.form['pe_question5']]
        user_humanities = [request.form['humanities_question1'],request.form['humanities_question2'],request.form['humanities_question3'],request.form['humanities_question4'],request.form['humanities_question5']]
        user_management = [request.form['management_question1'],request.form['management_question2'],request.form['management_question3'],request.form['management_question4'],request.form['management_question5']]
        user_arts = [request.form['arts_question1'],request.form['arts_question2'],request.form['arts_question3'],request.form['arts_question4'],request.form['arts_question5']]
        for i in range(5): #since the questions per set is only 5 items
        #simple algorithm for distributing score by comparing the fetch data list to correct answer list
            if user_science[i] == science_correct[i]:
                science_score = science_score + 1
            if user_math[i] == math_correct[i]:
                math_score = math_score + 1
            if user_language[i] == language_correct[i]:
                language_score = language_score + 1
            if user_socsci[i] == socsci_correct[i]:
                socsci_score = socsci_score + 1
            if user_tech[i] == tech_correct[i]:
                tech_score = tech_score + 1
            if user_history[i] == history_correct[i]:
                history_score = history_score + 1
            if user_pe[i] == pe_correct[i]:
                pe_score = pe_score + 1
            if user_humanities[i] == humanities_correct[i]:
                humanities_score = humanities_score + 1
            if user_management[i] == management_correct[i]:
                management_score = management_score + 1
            if user_arts[i] == arts_correct[i]:
                arts_score = arts_score + 1
        #convert the score from integer to float so that it may be processed by neural network model
        language_percent = float(language_score)/5
        science_percent = float(science_score)/5
        math_percent = float(math_score)/5
        socsci_percent = float(socsci_score)/5
        tech_percent = float(tech_score)/5
        history_percent = float(history_score)/5
        pe_percent = float(pe_score)/5
        humanities_percent = float(humanities_score)/5
        management_percent = float(management_score)/5
        arts_percent = float(arts_score)/5
        #call the predict function of the neural network model file and perform the forward propagation algorithm in predicting the college
        predict = pretrained_model.predict(np.array([[language_percent,science_percent,math_percent,socsci_percent,tech_percent,history_percent,pe_percent,humanities_percent,management_percent,arts_percent]]))
        #convert the output from array into list
        list1 = predict.tolist()
        #get the first value of list
        answer = list1[0]
        max_value = max(answer) #find the highest value where it is the most probable college from the processed score
        max_index = answer.index(max_value) #get the index
        college = college_list[max_index] #point the index to college_list
    return render_template('results.html', science_score=science_score, math_score=math_score, language_score=language_score, socsci_score=socsci_score, tech_score=tech_score, history_score=history_score, pe_score=pe_score, humanities_score=humanities_score, management_score=management_score, arts_score=arts_score, college=college) #send the data back to html gui
if __name__ == "__main__":
    # app.run() for debug
    #ui.run()
    init_gui(app, port=5000, width=800, height=600,
             window_title="Course Recommendation System | Project in DSA by Girlie R. Turan & Ladi Kyla N. Cole", argv=None)