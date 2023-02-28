
#The following lines (used in terminal) allow to fine tune the model.
#execution takes a couple of minutes.

#start with fine_tunes to prepare data in JSONL format 
     #openai tools fine_tunes.prepare_data -f C:\Users\steph\OneDrive\Documents\GitHub\RWT_AI_FILES\static\data3.txt


#choose one of the following lines to train the model 
    #openai api fine_tunes.create -t C:\Users\steph\OneDrive\Documents\GitHub\RWT_AI_FILES\static\data\3_prepared.jsonl -m davinci 
    #openai api fine_tunes.create -t C:\Users\steph\OneDrive\Documents\GitHub\RWT_AI_FILES\static\data3_prepared.jsonl -m babbage

#using the new fine tuned model in python
#   openai api completions.create -m <FINE_TUNED_MODEL> -p <YOUR_PROMPT>
#   openai api completions.create -m davinci:ft-personal-2023-02-01-22-49-33 -p <YOUR_PROMPT>

# JSONL file =  C:\Users\steph\OneDrive\Documents\GitHub\RWT_AI_FILES\data\prompts_model.jsonl

#Check that input file containing model is in JSONL format and correct:
#         openai tools fine_tunes.prepare_data -f C:\Users\steph\OneDrive\Documents\GitHub\RWT_AI_FILES\data\prompts_model.jsonl
	
#Create new model
#	openai api fine_tunes.create -t C:\Users\steph\OneDrive\Documents\GitHub\RWT_AI_FILES\data\prompts_model.jsonl -m davinci
	
#	Response:
#  	  [2023-02-26 09:56:20] Created fine-tune: ft-BI68wNS3U0PxTCgdAPTnYmEd
	
#  	  Stream interrupted (client disconnected).
#	  To resume the stream, run:
	
#To Check progress when model is in a Queue
#	  openai api fine_tunes.follow -i ft-BI68wNS3U0PxTCgdAPTnYmEd
	
#New model created
#	davinci:ft-personal-2023-02-26-15-07-18

#To cancel a job
#        openai api fine_tunes.cancel -i <YOUR_FINE_TUNE_JOB_ID>
	
#To list models
#        openai api fine_tunes.list

#To try the new model
#	openai api completions.create -m <YOUR_MODEL> -p <YOUR_PROMPT>  

#	openai api completions.create -m davinci:ft-personal-2023-02-26-15-07-18 -p " who is the fire chief of the Pittsburgh fire department?" -t 0
        # -T = temperature = 0

#help
#     Openai api completions.create -h  

	

To delete a model
openai api models.delete -i <FINE_TUNED_MODEL>