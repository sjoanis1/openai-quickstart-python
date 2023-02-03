
#The following lines (used in terminal) allow to fine tune the model.
#execution takes a couple of minutes.

#start with fine_tunes to prepare data in JSONL format 
     #openai tools fine_tunes.prepare_data -f C:\Users\steph\OneDrive\Documents\GitHub\RWT_AI_FILES\static\data3.txt


#choose one of the following lines to train the model 
    #openai api fine_tunes.create -t C:\Users\steph\OneDrive\Documents\GitHub\RWT_AI_FILES\static\data3_prepared.jsonl -m davinci 
    #openai api fine_tunes.create -t C:\Users\steph\OneDrive\Documents\GitHub\RWT_AI_FILES\static\data3_prepared.jsonl -m babbage

#using the new fine tuned model in python
#   openai api completions.create -m <FINE_TUNED_MODEL> -p <YOUR_PROMPT>
#   openai api completions.create -m davinci:ft-personal-2023-02-01-22-49-33 -p <YOUR_PROMPT>

