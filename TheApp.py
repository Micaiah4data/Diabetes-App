# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 05:18:53 2023

@author: Micaiah.O
"""

import numpy as np
import pickle
import streamlit as st

#loading the modl.sav
loaded_model = pickle.load(open('C:/Users/Micaiah.O/OneDrive/Desktop/My Stremliot/Diamodel.sav', 'rb'))

#creating a function for the prediction
def diabetes_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
        return 'Congratulations You Are Not Diabetic'
    else:
        return 'Unfortunately You Are Diabetic, Seek Medical Attention Soon'


def main():

    # Giving a title
    st.title('Diabetic Prediction System')

    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Level of Insulin')
    BMI = st.text_input('Body Mass Index Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('How Old Are You')

    #Code for prediction
    diagnosis = ''

    #Prediction button
    if st.button('Click here to Predict'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])

    st.success(diagnosis)




if __name__ == '__main__':
    main()