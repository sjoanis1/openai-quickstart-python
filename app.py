import os
import openai
openai.organization = "org-s5xRdnxv3xUnpGDRaIRKDC6H"
openai.api_key = os.getenv("OPENAI_API_KEY")

from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
#            model="text-davinci-003",
#            model="text-curie-001",         
            model="curie:ft-personal-2023-02-06-21-28-47",            
            prompt=generate_prompt(animal),
            temperature=0,
            max_tokens=350,
        )
        return redirect(url_for("index", result=response.choices[0].text))
    result = request.args.get("result")
    return render_template("index.html", result=result)

def generate_prompt(animal):
    return """
    {}   
""".format(
        animal.capitalize()
    )


##extract the notes from the response
#notes = response.choices[0].text
##Add response to a .txt file
#with open('testresults.txt', mode='w') as file_object:
#    print((prompt,"|",notes), file=file_object)

#print the notes
#print(notes)
