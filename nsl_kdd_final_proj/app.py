import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, send_file
import pickle 
import pandas as pd
from model import * 
from test import *


url=''
val = 0
cr = 0
app = Flask(__name__)


@app.route('/', methods=['GET','POST']) 

def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])

def predict():
    input_str = request.form['dump']
    arr1 = list(input_str.split(','))
    print(len(arr1))
    correlated_index = [19,14,23,24,33,33,34]
    for i in correlated_index:
        arr1.pop(i) 

    pt = arr1.pop(1)
    ser= arr1.pop(1) 
    fg  = arr1.pop(1) 


    arr_int = [int(arr1[x]) for x in range(0,19)]
    arr_24_25 = [0]*2
    arr_24_25[0]=int(arr1[24])
    arr_24_25[1] = int(arr1[25])
    arr_float_19_23 = [float(arr1[y]) for y in range(19,24)]
    arr_float = [float(arr1[z]) for z in range(26,31)] 


    protocol_array = [0]*3
    flag_array = [0]*11
    protocol_array = protocol_onehot(pt)
    flag_array = flag_onehot(fg)
    final_features = arr_int + arr_float_19_23 + arr_24_25 + arr_float + protocol_array + flag_array 
    scaled_feature = sc.transform([final_features])
    prediction = model.predict(scaled_feature)
    output = prediction[0]
    if(output=='anomaly'):
        res = 'The connection is Malicious!'
    else:
        res = 'The connection is Normal' 
    

    # return render_template('index.html', prediction_text='{}'.format(res))
    return render_template('index.html', prediction_text=res)

    

@app.route('/results',methods=['POST'])

def results():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(final_features)])
    output = prediction[0]
    return jsonify(output)

def protocol_onehot(key): 
    protocol_dict = {
        'icmp':[1,0,0],
        'tcp':[0,1,0],
        'udp':[0,0,1]
    }
    

    if key in protocol_dict.keys():
        return protocol_dict[key]



def flag_onehot(flg):
    flag_dict = {
        'OTH':[1,0,0,0,0,0,0,0,0,0,0],
        'REJ':[0,1,0,0,0,0,0,0,0,0,0],
        'RESTO':[0,0,1,0,0,0,0,0,0,0,0],
        'RSTR':[0,0,0,1,0,0,0,0,0,0,0],
        'RSTOS0':[0,0,0,0,1,0,0,0,0,0,0],
        'S0':[0,0,0,0,0,1,0,0,0,0,0],
        'S1':[0,0,0,0,0,0,1,0,0,0,0],
        'S2':[0,0,0,0,0,0,0,1,0,0,0],
        'S3':[0,0,0,0,0,0,0,0,1,0,0],
        'SF':[0,0,0,0,0,0,0,0,0,1,0],
        'SH':[0,0,0,0,0,0,0,0,0,0,1]
    }
    
    if flg in flag_dict:
        return flag_dict[flg]

@app.route('/explore', methods=['get'])
def explore():
    return render_template('explore.html')

@app.route('/back', methods=['get'])
def back():
    return render_template('index.html')

@app.route('/test', methods=['post'])
def test():
    test.score = score_test()
    return render_template('explore.html', test_result=test.score)
    
@app.route('/figure', methods=['post'])
def figure():
    val = display_confusion()
    if val==1:
        return render_template('explore.html',test_result=test.score, url='static/css/img/conf.png')   


@app.route('/report', methods=['post'])
def report():
    cr=display_report() 
    if cr==1:
        return render_template('explore.html',test_result=test.score, url='static/css/img/conf.png', test_report='static/css/img/classification_report.png')



if __name__ == "__main__":
    app.run(debug=True)