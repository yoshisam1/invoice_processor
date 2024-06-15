from dotenv import load_dotenv

load_dotenv() ## load all the environment variable from .env file

import os # To pick up env variable
from PIL import Image
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
  response = model.generate_content((input, image[0], prompt))
  return response.text

# Function that processes image file
def input_image_details(uploaded_file):
  if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()

    image_parts = [
      {
        "mime_type": uploaded_file.type,
        "data": bytes_data
      }
    ]
    return image_parts
  else: raise FileNotFoundError("No file upladed")


# Setup streamlit
st.set_page_config(page_title="Invoice Extractor")

st.header("Invoice Extractor")
input = st.text_input("Input Prompt: ", key = "input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type = ["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image, caption = "Uploaded Image.", use_column_width = True)

submit = st.button("Get Answer")

input_prompt = "You are an expert in understanding invoices. We will upload an image as an invoice and you will have to answer any questions based on the uploaded invoice image"

# If submit button is clicked
if submit:
  image_data = input_image_details(uploaded_file)
  response = get_gemini_response(input_prompt, image_data, input)
  st.subheader("The response is")
  st.write(response)