import streamlit as st
import pandas as pd
import tensorflow as tf

# Load your trained model (using a relative path)
MODEL_PATH = 'my_model.h5'
model = tf.keras.models.load_model(MODEL_PATH)

# Preprocess descriptions if necessary
def preprocess_descriptions(descriptions):
    # Add your preprocessing steps here
    # For example, tokenization, padding, etc.
    processed_descriptions = descriptions  # Placeholder for actual preprocessing steps
    return processed_descriptions

# Function to make predictions
def make_predictions(data):
    # Check if 'Description' column exists
    if 'Description' not in data.columns:
        st.error("The input data must contain a 'Description' column.")
        return data

    # Preprocess the input data
    descriptions = preprocess_descriptions(data['Description'].astype(str))
    
    # Check the input data format
    st.write("Descriptions for prediction:", descriptions)
    
    # Make predictions
    predictions = model.predict(descriptions)
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
