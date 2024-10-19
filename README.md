# Attendance-Using-Face-Detection

A facial recognition-based attendance system that uses machine learning to detect and recognize students from uploaded images. This project leverages the power of face detection and facial embeddings to mark attendance based on the recognized faces.

## Features

- **Face Detection**: Uses MTCNN (Multi-task Cascaded Convolutional Networks) for detecting faces in uploaded images.
- **Facial Embedding**: Utilizes `keras_facenet` to generate embeddings for the detected faces.
- **Recognition and Attendance**: Compares facial embeddings to pre-trained models (SVM) and automatically marks attendance based on recognized faces.
- **Streamlit Integration**: Provides a user-friendly interface for uploading images and displaying attendance.

## Tech Stack

- **Python**
- **Streamlit**: For creating the web application.
- **OpenCV**: For image processing.
- **MTCNN**: For face detection.
- **Keras FaceNet**: For generating facial embeddings.
- **Scikit-learn**: For training and using the SVM model for recognition.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/Attendance-Using-Face-Detection.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Make sure the following files are present in the project directory:

    - `svm_model_160x160.pkl`: The pre-trained SVM model for face recognition.
    - `encoder.npy`: The label encoder for mapping recognized faces to names.
    - `sheet.csv`: A CSV file for tracking attendance data.

4. To run the application, use the following command:

    ```bash
    streamlit run app.py
    ```

## Usage

1. **Upload an Image**: Launch the app and upload an image containing student faces.
2. **View Attendance**: The system will automatically detect and recognize faces, updating the attendance list in the CSV file.
3. **Display Results**: The app will show the recognized names and update the attendance records.

## Code Overview

### `app.py`

This is the main script that runs the Streamlit app. It handles:

- Image upload and processing.
- Invoking the face detection and recognition functions from `aat_main.py`.
- Displaying the attendance list and updating the `sheet.csv` file.

### `aat_main.py`

This script contains:

- Functions for face detection (`face_detection`), facial embedding (`get_embedding`), and prediction (`predictor`).
- An SVM model is used to recognize the detected faces based on pre-trained embeddings.

## Sample CSV Structure

The `sheet.csv` file is used to store the attendance record for each day. A new column (`day_1`, `day_2`, etc.) is added for every session to mark students' attendance.

| Name      | day_1 |
| --------- | ----- |
| Mann      | 1     |
| Sai       | 1     | 
| Divina    | 0     |
| Saarang   | 1     |

