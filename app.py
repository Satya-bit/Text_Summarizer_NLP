# from fastapi import FastAPI
# import uvicorn
# import sys
# import os
# from fastapi.templating import Jinja2Templates
# from starlette.responses import RedirectResponse
# from fastapi.responses import Response###
from src.Text_Summarizer_NLP.pipeline.prediction_pipeline import PredictionPipeline


# text:str = "Enter your chat here"

# app = FastAPI()

# @app.get("/", tags=["authentication"])
# async def index():
#     return RedirectResponse(url="/docs")



# @app.get("/train")
# async def training():
#     try:
#         os.system("python main.py")
#         return Response("Training successful !!")

#     except Exception as e:
#         return Response(f"Error Occurred! {e}")
    



# @app.post("/predict")
# async def predict_route(text):
#     try:

#         obj = PredictionPipeline()
#         text = obj.predict(text)
#         return text
#     except Exception as e:
#         raise e
    

# if __name__=="__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8080)



from flask import Flask, redirect, url_for, render_template, request, session
app = Flask(__name__)

app.secret_key = 'x#N2j5!fHjY6*b@X9KvX^b9$zFg7@6@8'



@app.route('/', methods=['GET', 'POST'])
def home():
    result = None  # Default value for result
    text = ''  # Default empty value for text
    error=None

    if request.method == 'POST':
        if 'clear' in request.form:  # Check if the "Clear" button was clicked
            session.pop('result', None)  # Clear result from session
            session.pop('text', None)  # Clear the text from session
            text = ''  # Clear the text in the input field
        elif 'submit' in request.form:  # Check if the "Summarize" button was clicked
            text = request.form['text']  # Get the text from the form
            # print(f"Text received: {text}")  # Debug step: Check the text received
            if len(text)<100:
                error="Please enter a longer text for summarization"
            else:
                obj = PredictionPipeline()
                result = obj.predict(text)  # Get prediction result
                # print(f"Prediction result: {result}")  # Debug step: Check the prediction result
                session['result'] = result  # Store result in session
                session['text'] = text  # Store the input text in session

    elif request.method == 'GET':
        # If the page is reloaded or visited without a form submission
        result = session.get('result', None)  # Get result from session if available
        text = session.get('text', '')  # Get the text from session if available

    return render_template("home.html", result=result, text=text,error=error)

if __name__ == '__main__':
    app.run(debug=True)
