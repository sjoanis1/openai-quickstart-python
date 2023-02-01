import os

import openai
openai.api_key = os.getenv("OPENAI_API_KEY")


#define the prompt
prompt = """Find who has receive funding from the Urban Area Security Initiative UASI"""

#generate a response
response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.6,
            max_tokens=256,
#            stop = None,
        )

#extract the notes from the response
notes = response.choices[0].text

#Add response to a .txt file
with open('testresults.txt', mode='w') as file_object:
#    print(["test",notes], file=file_object)
    print((prompt,"|",notes), file=file_object)


#print the notes
print(notes)