# Invoice QnA bot project (V1.1)
## About 🌟
A small personal project testing Google's GenAI Gemini LLM, inpired by multiple tutorials.
Allows QnA answering Invoice related queries.
More features will be added periodically (multi-page and history next?)

## Latest Update !!
+ Invoices in PDF format is now accepted

## Pre-requisite 🛠️
+ Python version >= 3.9 && <=3.11
+ Might need additional dependencies to install packages in requirements.txt

## How To Run the App 🚀
You can access the deployed version on the following link:
<Not Yet Deployed>

But if you want to try setting up the project on your local machine is a breeze! Follow these steps:

1. **Clone the Repository**: 
Execute the following command in your terminal:
    ```bash
    git clone https://github.com/yoshisam1/invoice_processor.git
    ```

2. **Install Dependencies**:
Ensure you have the latest versions of pip and brew installed. If not, run the following commands:
    PIP
    ```bash
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    ```
    Homebrew
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    ```

3. **Install Required Tools**:
Install the necessary tools by running the following command:
    ```bash
    pip install -r requirements.txt
    ```

4. **Inserting Google GenAI API key**:
Go to https://ai.google.dev/gemini-api/docs/quickstart?lang=python and get API key for your project
Create .env file in repository
Write the following line in the file and paste in your API Key like the following:
    ```python
    GOOGLE_API_KEY = "<your key here>"
    ```

4. **View the Project**:
Finally, run streamlit on localhost using the following:
    ```
    streamlit run app.py
    ```
Now, you're all set to explore and interact with the project right on your local machine!

5. **Upload Invoice**:
You can either use the sample invoice provided in example_invoices folder or upload your own.
