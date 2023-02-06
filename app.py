import os
import openai
from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
#            model="text-davinci-003",
            model="curie:ft-personal-2023-02-06-21-28-47"
            prompt=generate_prompt(animal),
            temperature=0.6,
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

