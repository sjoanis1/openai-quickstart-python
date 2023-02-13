#open the file
f = open("Data\\UASI_Questions.txt", "r") 

#print(f.readline())   # read a single line
#print(f.read())    # read the entire file

# read through each line individually.
for x in f:
    print(x)


#close the file
f.close