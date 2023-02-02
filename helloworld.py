import json
import pickle 
import numpy as np 
import pandas as pd 
import tensorflow as tf
import os
from tensorflow.keras import layers
from tensorflow.keras import models,utils
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.python.keras import utils
import streamlit as st
from streamlit_option_menu import option_menu
os.environ["TOKENIZERS_PARALLELISM"] = "true"
from PIL import Image



##################################################

#################################################

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


selected = option_menu(
    menu_title=None,
    options = ["Application"],
    icons = ["house","card-text","file-earmark-code","envelope"],
    default_index=0,
    orientation="horizontal",
    )



if selected == "Application":   
    st.title("Try out the application!")
    st.markdown("""
                #### It’s simple to kick start!
                ##### Just input your values and predict the performance. 
                ##### Our model will analyze and check the results with just ***one click***. 


        """)
    
    home_image = Image.open('Picture3.png')
    st.image(home_image, caption="")

# creating a function for Prediction 
def predict(id_student,date_submitted,weight,imd_band,age_band,sum_click,studied_credits,module_presentation,Quartile):
    prediction=classifier.predict([[id_student,date_submitted,weight,imd_band,age_band,sum_click,studied_credits,module_presentation,Quartile]])
    print(prediction)
    return prediction

def main():
    st.title("Student Performance Prediction")
    st.header('Enter the values')
    id_student = st.selectbox("id_student:",['6516', '11391', '23629', '23798', '24734' ,'2692384', '2692514','2694424','2694788','2698257'])
    date_submitted = st.number_input("date_submitted:", min_value=-6, max_value=239, value=1)
    weight= st.selectbox("weight",['0', '1','5', '8', '10', '20','30'])
    imd_band=st.number_input("imd_band", min_value=0, max_value=9, value=1)
    sum_click=st.number_input("sum_click", min_value=0, max_value=1326, value=1)
    age_band=st.selectbox("age_band",['0', '1', '2'])
    studied_credits = st.selectbox("studied_credits:",['60', '70', '75', '80', '90' ,'105', '120','130','135','150','165', '170', '180', '195', '210' ,'225', '240','270','300','325','330','345','420'])
    module_presentation=st.selectbox("module_presentaion",['240', '268', '269'])
    Quartile=st.selectbox("Quartile",['1', '2', '3', '4'])
    result=""
    if st.button("Predict Performance"):
        result=predict(id_student,date_submitted,weight,imd_band,age_band,sum_click,studied_credits,module_presentation,Quartile)
    st.success('The output is {}'.format(result))
    
if __name__=='__main__':
    main()




    st.markdown("""
            ---
            ***Credits:***
            > *The image was taken from [here](https://www.studentdoctor.net/2020/03/10/step-1-becomes-pass-fail-what-are-the-impacts/)*
           
            ---
            """)




    




