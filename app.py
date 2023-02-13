import os
import openai
openai.organization = "org-s5xRdnxv3xUnpGDRaIRKDC6H"
openai.api_key = os.getenv("OPENAI_API_KEY")

#open file containing questions.
f = open("Data\\UASI_Questions.txt", "r") 

for x in f:
    print(x)

#define the prompt
    prompt = x

#prompt =  """show 5 cities has receive funding from the Urban Area Security Initiative UASI"""



@app.route("/", methods=("GET", "POST"))

def index():
    if request.method == "POST":
        main_question = request.form["question1"] 
        print(main_question)

        temp = float(request.form["temperature"])        
        print(temp)

#generate a response using fine tuned model  (recommend at least 100 entries)
    response = openai.Completion.create(
          #  model="davinci:ft-personal-2023-02-01-22-49-33",
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.6,
            max_tokens=256,
        )
    print(response.choices[0].text)
    return redirect(url_for("index", result=response.choices[0].text))      
    result = request.args.get("result")
    return render_template("index.html", result=result)


#extract the notes from the response
    notes = response.choices[0].text
#Add response to a .txt file
    with open('testresults.txt', mode='w') as file_object:
        print((prompt,"|",notes), file=file_object)

#print the notes
    print(notes)




##extract the notes from the response
#notes = response.choices[0].text
##Add response to a .txt file
#with open('testresults.txt', mode='w') as file_object:
#    print((mainquestion,"|",test_output), file=file_object)
   


#print the notes
#print(notes)
