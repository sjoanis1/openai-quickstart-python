import os
import openai
openai.organization = "org-s5xRdnxv3xUnpGDRaIRKDC6H"
openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.Model.list()

#define the prompt
prompt = """show 5 cities has receive funding from the Urban Area Security Initiative UASI"""


response = openai.Completion.create(
#            model="ada",
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=256,
        )


#extract the notes from the response
notes = response.choices[0].text
#Add response to a .txt file
with open('testresults.txt', mode='w') as file_object:
    print((prompt,"|",notes), file=file_object)

#print the notes
print(notes)




