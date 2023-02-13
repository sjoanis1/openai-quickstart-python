import os
import openai
openai.organization = "org-s5xRdnxv3xUnpGDRaIRKDC6H"
openai.api_key = os.getenv("OPENAI_API_KEY")

#clear content from previous call
open('testresults.txt', mode='w') 

#open file containing questions.
f = open("Data\\UASI_Questions.txt", "r") 


for x in f:
#    print(x)

#define the prompt
    prompt = "1." + x + "\n2.what is the contact information of this chief" 
  #  prompt = "1.Who is the fire chief of the " + x + "fire deparment " + "\n2.what is the contact information of this chief" 
  # "\n \n format: \n danbury fire department: terence m. mccarthy \n Contact information: 203-797-4500, terence.mccarthy@danbury-ct.gov, 2 main street, danbury, ct 06810"
  #   "\n Cambridge Fire Department: Thomas F. Cahill, Contact: 617-349-4975,  , 491 Broadway, Cambridge, MA 02138"
  #  "\n Pittsburgh bureau of fire, Darryl E. Jones, 412-255-2860, , 200 Ross Street, 5th floor   200 Ross Street, 5th Floor, Pittsburgh, PA 15219"
  #  "\n philadelphia fire department, adam k. Thiel, 215-686-1300, adam.thiel@phila.gov, 240 spring garden street, philadelphia, pa 19123"
  #  "\n new york fire department, John J. Hodgens, 212-691-1211, daniel.nigro@fdny.nyc.gov, 9 metrotech center, brooklyn, ny 11201"
  #  "\n danbury fire department, terence m. mccarthy, 203-797-4500, terence.mccarthy@danbury-ct.gov, 2 main street, danbury, ct 06810"
  #  "\n Boston Fire Department, Paul F. Burke, 617-343-3550, paul.burke@boston.gov, 115 Southampton Street, Boston, MA 02118"


  #  print(prompt)

#generate a response using fine tuned model  (recommend at least 100 entries)
    response = openai.Completion.create(
          #  model="davinci:ft-personal-2023-02-01-22-49-33",
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.6,
            max_tokens=256,
        )
#    print(response.choices[0].text)
  

#extract the notes from the response
    notes = response.choices[0].text

#Add response to a .txt file
    with open('testresults.txt', mode='a') as file_object:
        print((prompt,"|",notes), file=file_object)

#print the notes
#    print(notes)

print("End") 

open('testresults.txt', mode='r') 
