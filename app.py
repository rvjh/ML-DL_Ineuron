from flask import Flask,render_template,request
from flask_cors import CORS,cross_origin
import  pickle
import sklearn

app=Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def homepage():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            LSTAT = float(request.form['LSTAT'])
            RM = float(request.form['RM'])

            filename = 'finalized_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[LSTAT,RM]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=round(prediction[0],2))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
