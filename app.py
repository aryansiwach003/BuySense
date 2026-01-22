import pickle
import streamlit as st
import pandas as pd

model=pickle.load(open('model.pkl','rb'))

st.title('BuySense 🛒')

age=st.number_input("Enter the Age",min_value=18,max_value=60,step=1)
salary=st.number_input("Enter the salary",min_value=15000.00,max_value=150000.00,step=1000.0)
gender=st.selectbox("Select your Gender",('Male','Female'))

if st.button('Predict'):
  data_input=pd.DataFrame(
   {
    'Age':[age],
    'EstimatedSalary':[salary],
    'Gender':[gender]
   }
  )
  result=model.predict(data_input)
  if result[0]==1:
     st.write("The Customer is likely to purchade the item")
  else:
     st.write("The Customer is unlikely to purchase the item")