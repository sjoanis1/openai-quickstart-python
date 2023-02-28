import os
import openai
openai.organization = "org-s5xRdnxv3xUnpGDRaIRKDC6H"
openai.api_key = os.getenv("OPENAI_API_KEY")

#clear content from previous run
open('testresults.txt', mode='w') 

#open file containing questions.
f = open("Data\\Fire_Departments.txt", "r") 
lines = f.readlines()
#print(lines[1])

counti = 0
f = open("Data\\Fire_Departments.txt", "r") 

for x in f:
    if counti >= 6 and counti < 13:
#define the prompt       


    #    prompt = "I search and validate information to identify the fire chief and website of a fire rescue organization and identify the current fire chief." 
    #    prompt = prompt + "I provide the name, website, phone number and email address when they are available."
        
    #    prompt = prompt + "Q: who is the fire chief of the San Diego Fire-Rescue Headquarters?\nA: Colin Stowell; https://www.sandiego.gov/fire; tel: Not found; Not found"
    #    prompt = prompt + "Q: who is the fire chief of the San Francisco Fire Department?\nA: Robert F. Postel; https://sf-fire.org/; tel: (415) 558-3402; Not found"
    #    prompt = prompt + "Q: who is the fire chief of the San Mateo Consolidated Fire Department?\nA: Matt Turturici; https://www.smcfire.org/; tel:  (650) 522-7900; Not found"
        prompt = " Who is the fire chief of the " + x 
        print(prompt)

    #    prompt = "1.I search and validate information to identify the fire chief and website of a fire rescue organization\n2.I search through the internet to find the home address of the departmentnt.\n3.I look for the name of the leader found on web pages within the web domain\n3.I provide the name, website, phone number and email address if they are available otherwise I state that the the information is not available."
    #    prompt = "1.I am a highly intelligent robot that only tells the truth to identify the fire chief based on scrapping a web domain name\n2.I search through each page of the domain to identify the leadership team of command staff\n3.I identify the chief or leader and provide his email and phone number or answer “Not found” if it is not available on the domain."
    
    #    prompt = prompt + "Q: Who is the fire chief of the  San Diego Fire-Rescue Headquarters?\nA: Colin Stowell"

    #    prompt = prompt + "Q: Who is the fire chief of the  San Francisco Fire Department?\nA: Robert F. Postel"
        
    #    prompt = prompt + "Q: Who retired as fire chief of the  New York Department?\nA: Daniel A. Nigro"
    #    prompt = prompt + "Q: Who was a fire chief of the New York Fire Department?\nA: Daniel A. Nigro"
    #    prompt = prompt + "Q: What fire chief in San Mateo Consolidated fire department is deceased?\nA: David A. Holland"
    #    prompt = prompt + "Q: Who replaced David A. Holland as fire chief?\nA: Kent Thrasher"
    #    prompt = prompt + "Q: Who replaced daniel a. nigro as fire chief?\nA: John J. Hodgens"

    #    prompt = prompt + "Q: Who is the fire chief of the ?\nA: ; ; tel: ; "


    # ------------
    #    prompt = prompt + "Q: who is the fire chief of the San Diego Fire-Rescue Headquarters?\nA: Colin Stowell; https://www.sandiego.gov/fire; tel: Not found; Not found"
    #    prompt = prompt + "Q: who is the fire chief of the San Francisco Fire Department?\nA: Robert F. Postel; https://sf-fire.org/; tel: (415) 558-3402; Not found"
    #    prompt = prompt + "Q: who is the fire chief of the San Mateo Consolidated Fire Department?\nA: Matt Turturici; https://www.smcfire.org/; tel:  (650) 522-7900; Not found"

    #    prompt = prompt + "Q: Who is the fire chief of the  Tortellini Fire Department?\nA: ; ; tel: ;"

    #    prompt = prompt + "Q: Who is the fire chief of the Santa Cruz Fire Department?\nA: Rob Oatey; https://www.cityofsantacruz.com/government/city-departments/fire-department; tel: 831-420-5280; not found"
    #    prompt = prompt + "Q: Who is the fire chief of the City of Scottsdale - Fire Department?\nA: Tom Shannon; https://www.scottsdaleaz.gov/fire/fire-chief-message; tel: not found; not found"
    #    prompt = prompt + "Q: Who is the fire chief of the Seattle Fire Department?\nA: Harold D. Scoggins; https://www.seattle.gov/fire/about-us/about-the-department/leadership-team; tel: not found; not found"
    #    prompt = prompt + "Q: who is the fire chief of the Solano County Fire Department?\nA: ; https://www.solanocounty.com/emergencies/firepolicedept.asp; tel: Not found; Not found"
    #    prompt = prompt + "Q: Who is the fire chief of the City of Benicia Fire Department?\nA: Josh Chadwick; https://www.ci.benicia.ca.us/fire; tel: 707-746-4275; not found"
    #    prompt = prompt + "Q: who is the fire chief of the Cordelia Fire Protection District?\nA: Dave Carpenter; https://www.cordeliafire.org/; tel: Not found; Not found"
    #    prompt = prompt + "Q: Who is the fire chief of the Suisun City Fire Department?\nA: Brad Lopez; https://www.suisun.com/departments/fire-department/; tel: 707-421-7205; bllopez@suisun.com"
       
    #    prompt = prompt + "Q: who is the fire chief of the ?\nA: Not found; https://www.cityofdixon.us/fire; tel: Not found; Not found"

    #    prompt = prompt + "Q: Who is the fire chief of the Vacaville fire protection district?\nA: Howard Wood; https://www.vfpd.net/chiefs; tel: 707-447-2252; not found"
    #    prompt = prompt + "Q: Who is the fire chief of the City of Vallejo fire department?\nA: Kyle Long; https://www.ci.vallejo.ca.us/cms/one.aspx?portalid=16925451&pageid=17554309; tel: 707-648-4565; not found"
    #    prompt = prompt + "Q: Who is the fire chief of the Sonoma County fire district?\nA: Mark Heine; https://www.sonomacountyfd.org/; tel: 707-838-1170; not found"
    #    prompt = prompt + "Q: Who is the fire chief of the St. Louis Fire Department?\nA: Dennis Jenkerson; https://www.stlouis-mo.gov/government/departments/public-safety/fire/about-us-fire.cfm; tel: (314) 533-3406; jenkersond@stlouis-mo.gov"
            

    #    prompt = prompt + "Q: Who is the fire chief of the ?\nA: ; ; tel: ; "    
      
    #    prompt = prompt + "\nWho is the fire chief of the " + x 


#generate a response using fine tuned model  (recommend at least 100 entries)
        response = openai.Completion.create(
          #  model="davinci:ft-personal-2023-02-01-22-49-33",
          #  model = "davinci:ft-personal-2023-02-26-15-07-18",
            model = "davinci:ft-personal-2023-02-28-00-09-37",
            #corresponds to ft-mt5iV0aKbgHzL6Ha0zRA4jou
            
             
             
                       
          # model="text-davinci-003",
            prompt=prompt,
            temperature=0.0,
            max_tokens=256,
            )
#        print(response.choices[0].text)
  

#extract the notes from the response
        notes = response.choices[0].text

#Add response to a .txt file
        with open('testresults.txt', mode='a') as file_object:
            print((x,"|",notes), file=file_object)

    else: 
        pass
    counti += 1    
#print the notes
#    print(notes)

print("End") 

#open('testresults.txt', mode='r') 
f.close()