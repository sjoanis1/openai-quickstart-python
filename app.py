import os
import openai
openai.organization = "org-s5xRdnxv3xUnpGDRaIRKDC6H"
openai.api_key = os.getenv("OPENAI_API_KEY")

from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))

def index():
    if request.method == "POST":
        main_question = request.form["question1"] 
        print(main_question)

        temp = float(request.form["temperature"])        
        print(temp)

        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct"
#            model="text-davinci-003",
#            model="text-curie-001",         
#            model="curie:ft-personal-2023-02-06-21-28-47",            
            prompt=generate_prompt(main_question),       
            temperature = float(temp),
            max_tokens=1500,
        )
        print(response.choices[0].text)
#        print(response.choices[0].text)
        return redirect(url_for("index", result=response.choices[0].text))      
    result = request.args.get("result")
    return render_template("index.html", result=result)
