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

        temp = request.form["temperature"]
        print(temp)

        response = openai.Completion.create(
            model="text-davinci-003",
#            model="text-curie-001",         
#            model="curie:ft-personal-2023-02-06-21-28-47",            
            prompt=generate_prompt(main_question),
            temperature=generate_temp(temp),
            max_tokens=500,
        )
        print(response.choices[0].text)
        return redirect(url_for("index", result=response.choices[0].text))
        

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(main_question):
    return """
    {}   
""".format(
        main_question.capitalize()
    )


def generate_temp(temp):
    return """
    {}   
""".format(temp        
    )






##extract the notes from the response
#notes = response.choices[0].text
##Add response to a .txt file
#with open('testresults.txt', mode='w') as file_object:
#    print((mainquestion,"|",test_output), file=file_object)
   


#print the notes
#print(notes)
