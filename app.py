import io
from dotenv import load_dotenv

load_dotenv() ## load all the environment variable from .env file

from PIL import Image
from pdf2image import convert_from_bytes
import os # To pick up env variable
import google.generativeai as genai
import streamlit as st # Easy front-end framework for streaming

genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) # Using os method, we pass our key to GenAI server

## Load Gemini Pro Vision
model = genai.GenerativeModel('gemini-pro-vision')

# Function that calls Google API
#input --> Tells what the assistant should do/act as
#image --> the image/invoice we pass
#prompt --> the message we want it to return to us
def get_gemini_response(input, image, prompt):
    response = model.generate_content((input, image, prompt))

    # Can check candidate by calling response.candidates[index]

    return response.text

# Function that processes image file
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            # Convert the first page of the PDF into an image
            pages = convert_from_bytes(uploaded_file.getvalue())
            first_page = pages[0]
            
            # Convert the first page to bytes using io.BytesIO
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()
            image_part = {
                "mime_type": "image/jpeg",
                "data": img_byte_arr
            }
        else:
            bytes_data = uploaded_file.getvalue()
            image_part = {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        return image_part
    else:
        raise FileNotFoundError("No file uploaded")


# Setup streamlit
st.set_page_config(page_title="Invoice Extractor")

st.header("Bill/Invoice QnA bot (V1.2)") # Make into logo?

# Placeholder for the image
image_placeholder = st.empty()

# File uploader
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png", "pdf"])

# Display the uploaded image immediately
if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        pages = convert_from_bytes(uploaded_file.getvalue())
        image = pages[0]  # Display the first page of the PDF
        image_placeholder.image(image, caption="Uploaded PDF Image.", use_column_width=True)
    else:
        image = Image.open(uploaded_file)
        image_placeholder.image(image, caption="Uploaded Image.", use_column_width=True)


input = st.text_input("Your Question: ", key = "input")
submit = st.button("Get Answer")

input_prompt = """You are an expert in understanding invoices. We will upload an image as an invoice and you will have to answer any questions only based on the uploaded invoice image. 
                  Questions unrelated to the invoice should be rejected, and an error message should be raised.
                  If there are no image attached or the attached image is not an invoice, you should raise an error message as well."""

# If submit button is clicked
if submit:
    try:
        image_data = input_image_details(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, input)
        st.subheader("The response is")
        st.write(response)
    except Exception as e:
        st.error(f"Error: {e}")