import os
import openai
openai.organization = "org-s5xRdnxv3xUnpGDRaIRKDC6H"
openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.Model.list()

#define the prompt
prompt = """show 5 cities has receive funding from the Urban Area Security Initiative UASI"""

#generate a response
#response = openai.Completion.create(
#            model="text-davinci-003",
#            prompt=prompt,
#            temperature=0.6,
#            max_tokens=256,
#        )



#generate a response using fine tuned model  (recommend at least 100 entries)
response = openai.Completion.create(
            model="davinci:ft-personal-2023-02-01-22-49-33",
            prompt=prompt,
            temperature=0.6,
            max_tokens=256,
        )


#extract the notes from the response
notes = response.choices[0].text
#Add response to a .txt file
with open('testresults.txt', mode='w') as file_object:
    print((prompt,"|",notes), file=file_object)

#print the notes
print(notes)




