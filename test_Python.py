import os


i = 0

#for j in range(5):
#    i += 1
#    print(j) 
   
   
#open file containing questions.
f = open("Data\\UASI_Cities.txt", "r") 
lines = f.readlines()


i=0
f = open("Data\\UASI_Cities.txt", "r") 
for x in f:
    if i >= 0 and i < 10:
        print(lines[i])
#    print(x)
    i +=1

print(lines[6])
print("End") 
    
f.close()
