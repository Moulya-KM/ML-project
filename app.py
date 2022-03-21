import streamlit as st
import joblib
model=joblib.load('spam-ham(1)')
st.title('SPAM HAM CLASSSIFIER')
ip=st.text_input('enter the message')#It will tske the message from the console
op=model.predict([ip])
if st.button('Predict'):  #here it is clicking of the button
  st.title(op[0]) 
          
