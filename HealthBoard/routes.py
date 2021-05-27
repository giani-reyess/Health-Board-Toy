from flask import url_for, render_template, make_response, request, redirect, session
from HealthBoard import app
from HealthBoard.forms import InputData  
from . import body_calculator 

@app.route('/', methods = ['GET','POST'])
def index():

    form = InputData()

    if request.method == 'POST':   


        body = body_calculator.Parameters(float(request.form['height']), 
                                          float(request.form['weight']),
                                          float(request.form['age']), 
                                          request.form.get('gender'),   
                                          float(request.form['waist']))

        LBM = body.Lean_Body_Mass()
        BMR = body.Basal_Metabolic_Rate()
        BMI = body.Body_Mass_Index()
        BFP = body.Body_Fat_Percentage()
       

            
        context = {
            'LBM' : LBM,
            'BMR' : BMR,
            'BMI' : BMI,
            'BFP' : BFP,
            'form' : form
            }

        return render_template('index.html', **context)   
          
    else: 
        return render_template('index.html', form=form)