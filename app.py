import os
import openai
openai.organization = "org-s5xRdnxv3xUnpGDRaIRKDC6H"
openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.Model.list()

from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)


#define the prompt
prompt = """show 5 cities has receive funding from the Urban Area Security Initiative UASI"""

#generate a response
response = openai.Completion.create(
            model="text-davinci-003",
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
