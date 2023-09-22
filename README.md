# ML_DL_projects 
This repository contains personal projects in machine learning and deep learning domain.
## PowerBI Study Project 
### HR Analytics
  
   ![HR_data_analytics](https://github.com/pooja614/ML_DL_projects/assets/69869583/58895fb3-1703-4663-8f56-4d482ac7dd9e)




## SQL 
<pre>
* IPL data analysis. 
* Here questions on the data is answered using SQL queries. 
*<a href="https://github.com/pooja614/ML_DL_projects/blob/main/SQL_IPL_Data_Analysis.ipynb">link</a>
</pre> 
## Natural Language Processing
### Medical Tweets: Topic Modelling
<pre>
* NLP based project deals with Topic Modelling of medical tweets.
* Percentage of different languages is observed and English language
tweets are used for topic modelling.
* Tweets are preprocessed based on nature of the data. Word Cloud,
frequency of words, n-grams is explored.
* LDA and BERTopic is used for topic modelling. Different visualizations are
applied.
</pre>
### Skim Literature
<pre>
* Project aims to skim the literature and classify its sections: objective,
methods, background, results and conclusion.
* Logistic Regression is used for classification.<br>
</pre> 

### Sentimental Analysis of Book Reviews with Bidirectional
LSTM
<pre>
* The project deals with sentimental binary classification of book
reviews. 
* The text data is preprocessed, lemmatization, text
vectorization, layer embedding parameters is experimented,
modelling using bidirectional LSTM, stacked bidirectional LSTM. Fine
tuning through parameter search for nodes, number of hidden layers
and dropout regularization.
* Stacked bidirectional LSTM yields 80% accuracy. 
</pre> 

### Percentage Matching of string 
<pre>
* Data is explored 
* Null values dropped. 
* Text Data preprocessing. 
* String Matching using fuzzywuzzy.
* Ratio, partial Ratio and top_sort_ratio methods are experimented.  
* Partial ratio and Token_sort_ratio has given better results. 
</pre>
## Image Classification
### Weather Recognition
<pre>
* This Deep Learning project deals with multiclass classification of weather
images using CNN.
* EDA, experimentation with sequential model as well as modelling
through transfer learning. Dataset is augmented, dropout regularization
is applied, callbacks and early stopping is employed.
* Adam optimizers' learning rate is experimented and fine- tuned.
* Sequential Model has given 86% training accuracy and 78% test
accuracy.
</pre> 

## Machine Learning
### Air Quality Classification
<pre>
* Dataset containing reading of different gases in the atmosphere is
modelled for predicting the air quality.
* Data preprocessing, exploratory data analysis, using correlation matrix,
pair plots, scatter plots, boxplots, variable transformation is done using
boxcox and log transformations. Standard scaler is used for scaling.
* Decision tree, naive_bayes_guassian, randomforest classifier, Xgb,
support vector machine etc are searched and random forest is chosen.
* Hyper parameter tuning using randomizedSearchCV is utilized to choose
optimal parameters. The model yields 84% accuracy. 
<br>
<a href = "https://github.com/pooja614/ML_DL_projects/blob/main/Statistic_Analysis_and_Classification_of_Air_Pollution.ipynb">link</a>
</pre>  

### Time Series Forecasting
<pre>
Time series Analysis of Electric Production. 
- Visualize the data
- Check for stationarity using rolling statistics and augmented dickey fuller test
- Convert non stationary to stationary data by applying tranaformation and differencing techniques.
- find p, d, q using acf, pacf plots
- Seasonal Decomposition using multiplicative model
- Find P D Q values of the seasonal components
- Modelling using SARIMAX
- Evaluation using MSE, RMSE, MAE.
- Interpret Residual Diagnostic Plots
- Interpret Summary Statistics
- Prediction with future data.
</pre>
### Buldozer Price Prediction 
<pre>
* Predict the future sale price of a bulldozer, given its characteristics and 
   previous examples of how much similar bulldozers have been sold for. 
* Preprocessing, EDA, modelling, feature importance is explored. 
</pre>
### Fraudulent Transactions. 
<pre>
 Fraud Detection Model contains following steps:
   -Import and Explore Dataset
   -Remove correlation if there is correlation between unrelated features. 
   -Apply Variable Transformation on the skewed columns. 
   -Apply onehot encoding on categorical variables
   -Preserve customer and merchant id information to form additional categorical features. 
   -Train test split with 80-20 rule. 
   -Apply sampling for class imbalance. 
   -Fit the model to RandomForestClassifier and Logistic Regression. 
   -Visualize and analyse the results. 
  </pre>
## Machine Learning Project with GUI  

### A Novel Machine learning based Hybrid Model for Webshell Detection
<pre>
This project is based on NSL-KDD dataset, we applied different algorithms to NSL-KDD data set to classify
normal and anomaly connections. Proposed method is validated by 10 fold cross validation for the
classification. The Experimental analysis shows that when compared to other classification
methods, proposed hybrid model have increased the accuracy, precision, recall and f-measure
values.
- Features are selected based on correlation, one-hot encoding, standard scaling is applied.
- Preprocessed data is experimented with different ml models (Naïve Bayes Bernoulli, KNN,
 Decision Tree, Naïve Bayes Gaussian, Logistic Regression.).
- Selected models is tuned for hyper parameters and hybrid ensemble is performed.
- GUI is implemented using HTML, CSS, bootstrap, flask. 
Publication: <a href = "https://doi.org/10.22214/ijraset.2021.35644">IJRASET</a> 
</pre>

### Car Selling Price Prediction 

 <pre> 
This is a flask application to predict car sales. 
The major sections include:
•	Data folder : It contains dataset for testing purpose. 
•	Pickle folder: It contains trained model saved in the pickle format.
•	Static folder: It contains CSS file, images and bootstrap framework. 
•	Templates folder: HTML templates (index.html and explore.html) is contained. 
•	app.py file: It is an app object, which is an instance of the Flask object. It will act as the central configuration object for the entire application. It is used to set up pieces of the application required for extended functionality.
•	model.py file: Saved model is loaded. 
•	test.py file: It contains logic for testing the dataset whose results are displayed in explore.html 
  
 <a href = "https://github.com/pooja614/CarSelling">link</a>

 </pre>


### Data Analysis and Text Analysis 
Naukri Job Listing 
<pre>
* This project aims at exploring the job listing dataset of professional job
portal naukri.com.
* The analysis has a sneak peek into the job trends and employment hub
areas as well as the frequency of job postings, insights of high paying job
roles and monthly trends. Language used, state wise job distributions, top
job posting companies are analyzed. Average salary trends, insights into
part time and freelancing sections are explored.
* Job description is analysed. 
</pre>

## Other Projects

### Help-Chat
<pre>
This is a basic chat app which provides online resources/articles based on the chats and 
thus enlighten students to deal with their problems. 
This chat room provides client to client or many client conversation thus third person or 
host is not involved. It has a reservoir of keywords and associated online link in a csv file. As the keyword is involved in the chat, the clickable link pops up. 

Tools and Platform Used:
➢ Python
➢ VS code
➢ Libraries and Packages Required:
1. GUI:Tkinter
2. Socket and threading 
</pre>
