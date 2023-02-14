import os
import openai
openai.organization = "org-s5xRdnxv3xUnpGDRaIRKDC6H"
openai.api_key = os.getenv("OPENAI_API_KEY")

#clear content from previous run
open('testresults.txt', mode='w') 

#open file containing questions.
f = open("Data\\UASI_Cities.txt", "r") 

counti = 0

for x in f:
#    print(x)
    counti += 1    

    if counti > 0 and counti < 10:
#define the prompt       
    
        prompt = "1.List fire deparments in the city of " + x + "City: Boston, MA; Boston Fire Department\ncity: "
    

#        print(prompt)

#generate a response using fine tuned model  (recommend at least 100 entries)
        response = openai.Completion.create(
          #  model="davinci:ft-personal-2023-02-01-22-49-33",
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.0,
            max_tokens=256,
            )
#    print(response.choices[0].text)
  

#extract the notes from the response
        notes = response.choices[0].text

#Add response to a .txt file
        with open('testresults.txt', mode='a') as file_object:
            print((x,"|",notes), file=file_object)

    else: 
        pass

#print the notes
#    print(notes)

print("End") 

open('testresults.txt', mode='r') 
