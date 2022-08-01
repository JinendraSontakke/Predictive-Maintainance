# Predictive-Maintainance
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Problem Statement
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A jet engine is the most important part of the plane, and it helps to move the airplane forward with a great force that is produced by a tremendous thrust Maintenance of equipment is a critical activity for any business involving machines. And causes the plane to fly very fast. During operation, degradation occurs in each of the components. If the degradation level is any component exceeds a threshold the engine is said to have failed. Therefore, the jet engines are inspected before every take-off and maintenance of equipment is critical activity for any business involving machines. Predictive Maintenance is the method of scheduling maintenance based on the prediction of the failure time of any equipment. The prediction can be done by analyzing the data measurements from the equipment. Machine learning is technology by which outcomes can be predicted based on a model prepared by training it on past input data and its output behavior. The model developed can be used to predict machine failure before it happens.

# Data Analysis
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

n the Train dataset we are provided with 26 columns(Features) of data.

* ID : The Engine id — Unique for each engine.
* Cycle : Engine Cycle.
* OpSet 1-3 : Operational Setting.
* SM 6-21 : sensor measurements.

# Approach
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The main goal is to predict machine failure before it happens bases on different factors available in the dataset.

* Data Exploration : Exploring dataset using pandas,numpy,matplotlib and seaborn.
* Data visualization : Ploted graphs to get insights about dependend and independed variables.
* Feature Engineering : Removed missing values and created new features as per insights.
* Model Selection I : Tested all base models to check the base accuracy.
* Pickle File : Selected model as per best accuracy and created pickle file using pickle library.
* Webpage & deployment : Created a webform that takes all the necessary inputs from user and shows output. After that I have deployed project on Microsoft Azure.


# Technologies Used
-------------------------------------------------------------------------------------------------------------------------------------------------------------

* Visual Studio Code Is Used For Integrated Development Environment(IDE).
* For Visualization Of The Plots Matplotlib , Seaborn Are Used.
* Microsoft Azure is Used For Model Deployment.
* Front End Deployment Is Done Using HTML , CSS.
* Flask is for creating the application server and pages.
* Git Hub Is Used As A Version Control System.
* csv is used for creating .csv format file.
* numpy is for arrays computations and mathematical operations
* pandas is for Manipulation and wrangling structured data
* scikit-learn is used for machine learning tool kit
* pickle is used for saving model

# User InterFace 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* Home Page 

<p align="center">
  <img src="https://raw.githubusercontent.com/JinendraSontakke/Predictive-Maintainance/main/IMG/home%20(1).jpg" width='600px'>
</p>

* Predict Page
<p align="center">
  <img src="https://raw.githubusercontent.com/JinendraSontakke/Predictive-Maintainance/main/IMG/predict.jpg" width='600px'>
</p>


# Predictive Maintenance Project Video 
-----------------------------------------------------------------------------------------------------------------------------------------------------


<p align="center">
  <img src="https://youtu.be/4G2rwHDW2fo">
</p>


# Deployment Links
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
 
 Azure Link : https://predmain.azurewebsites.net/
 
 # Run Locally
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* Clone the project
```bash
   git clone https://github.com/JinendraSontakke/Predictive-Maintainance
```
* Go to the project directory
```bash
  cd Predictive-Maintainance
```
* Install dependencies
```bash
  pip install -r requirements.txt
```
* Run the app.py
```bash
  python app.py
```

# Conclusions
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

I developed a Remaining Useful life Predictive model with the capbility of indentifying machine failure before it happens. The Proposed Approach Accept Input Data Was Pre-Processed By Way Of Missing Values Imputation, Non-Numeric To Numeric Feature Conversion And Normalization, And Split Into Training And Test Set. The Training Set Is Passed Into A Data Balancing Module To Ensure Equal Class Distribution In Learning Model Decisions. he Predictive Models Were Validated On Test Data And Their Performances Were Evaluated. The Evaluation Of The Result Obtained Showed By Accuracy Score.

# Documentation
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[High Level Documentation]


