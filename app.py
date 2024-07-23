import streamlit as st
import pandas as pd
import tensorflow as tf  # or use keras.models if your model is a Keras model

# Load your trained model (replace 'my-model.h5' with your model file)
MODEL_PATH = "C:\Users\haneen\Desktop\my_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Function to make predictions
def make_predictions(data):
    # Preprocess the 'Description' column if necessary
    # For example, if you need to convert text descriptions to numerical data, add that logic here
    
    # Assuming your model takes the 'Description' column and outputs the 'Predicted Label'
    predictions = model.predict(data['Description'])
    data['Predicted Label'] = predictions
    return data

# Streamlit App
st.title('Model Deployment with Streamlit')

# File uploader
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    # Read the uploaded Excel file
    input_data = pd.read_excel(uploaded_file)
    
    # Display the uploaded data
    st.write("### Uploaded Data")
    st.write(input_data)
    
    # Make predictions
    output_data = make_predictions(input_data)
    
    # Display the predictions
    st.write("### Predictions")
    st.write(output_data)

    # Download the result
    st.download_button(
        label="Download predictions as CSV",
        data=output_data.to_csv(index=False),
        file_name='predictions.csv',
        mime='text/csv'
    )

