import sys 
import numpy as np 
import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns  
from sklearn import preprocessing
from sklearn.model_selection import train_test_split , KFold
from sklearn. preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report                              
from sklearn.metrics import confusion_matrix 
import pickle

sc = pickle.load(open('pickle/scaler.pk1', 'rb'))
model = pickle.load(open('pickle/model.pk1', 'rb'))
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn import model_selection
# import dataframe_image as dfi
from sklearn import metrics 
from IPython import display   
# from IPython.display import Image 
# from IPython.display import display  

columns=['duration' ,'protocol_type','service' ,'flag' ,'src_bytes' ,'dst_bytes' ,'land','wrong_fragment' ,'urgent' ,'hot' 
,'num_failed_logins','logged_in','num_compromised','root_shell' ,'su_attempted' ,'num_root' ,'num_file_creations' 
 ,'num_shells','num_access_files' ,'num_outbound_cmds' ,'is_host_login','is_guest_login','count','srv_count' ,'serror_rate' 
 ,'srv_serror_rate' ,'rerror_rate' ,'srv_rerror_rate' ,'same_srv_rate' ,'diff_srv_rate' ,'srv_diff_host_rate' 
,'dst_host_count' ,'dst_host_srv_count' ,'dst_host_same_srv_rate' ,'dst_host_diff_srv_rate' ,'dst_host_same_src_port_rate' 
 ,'dst_host_srv_diff_host_rate' ,'dst_host_serror_rate' ,'dst_host_srv_serror_rate' ,'dst_host_rerror_rate' 
 ,'dst_host_srv_rerror_rate' ,'label'
         ]


x_test = pd.read_csv("data/x_test3.csv")
y_test = pd.read_csv("data/y_test3.csv")
y_preds = model.predict(x_test)
def score_test():
    score = model.score(x_test, y_test)
    return score
    

def display_confusion():
    plt.figure()
    hm_cm = confusion_matrix(y_test, y_preds)      
    ax = plt.subplot()
    sns.heatmap(hm_cm, annot = True, fmt='g', ax=ax)
    ax.set_xlabel('predicted Labels')      
    ax.set_ylabel('True Labels')        
    ax.set_title('Confusion Matrix')
    ax.xaxis.set_ticklabels(['anomaly','normal'])   
    ax.yaxis.set_ticklabels(['anomaly', 'normal'])  
    plt.savefig("static/css/img/conf.png")
    return 1

def display_report():
    plt.figure()
    c_r = classification_report(y_test, y_preds,digits=4, output_dict=True)
    sns.heatmap(pd.DataFrame(c_r).iloc[:-1, :].T, annot=True, cmap = "RdBu")
    plt.savefig("static/css/img/classification_report.png")
    return 1

    
    
   


