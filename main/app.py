import streamlit as st
import cv2
import numpy as np
import time
from datetime import datetime
from PIL import Image
import pandas as pd
# Import your existing functions here
from aat_main import face_detection, get_embedding, predictor

st.title("Facial Recognition Attendance System")
df = pd.read_csv('sheet.csv')
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    image.save("img.jpg")


    start_time = time.time()
    st.write("Processing image...")

    # Assuming your existing functions are correctly implemented
    names = predictor('img.jpg')
    
    # For demonstration, we'll simulate the processing time
    # time.sleep(35)  # Simulate the processing time
    
    end_time = time.time()
    st.write(f"Processing completed in {end_time - start_time} seconds.")
    
    st.write("Attendance List:")
    st.write('Total students present: ' + str(len(names)))
    # Display the attendance list
    st.write(names)

    students = ['Mann','Sai','Karnel','Divina','Saarang','Santhosh','Aditya','Nitish','Karthikey','Ishaan','Shashwat','Ujwal']

    Attendance = []
    for i in students:
      if i in names:
        Attendance.append(1)
      else:
        Attendance.append(0)

    df['day_1'] = Attendance
    df.to_csv('sheet.csv', sep=',', index=False)
    # Placeholder for displaying the attendance list
    # Replace the following line with your actual attendance list
    # st.write(["John Doe", "Jane Smith", "Alice Johnson"])
