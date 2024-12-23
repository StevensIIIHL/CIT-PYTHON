# for file encoding/decoding of the dictionary:
import pickle

# Declaring a dictionary - empty
dictStudentColors = {}


# 1. Load stored dictionary key/values: 
eof = False

try:
  #1.1 Attempt to open the file.  
  
  input_file = open('student_colors.dat', 'rb')

  #1.2 if execution reaches here load each dictory key/value in: 
  while not eof:
    try:
        dictStudentColors = pickle.load(input_file)
        
    except EOFError:
        eof = True
  input_file.close()

except FileNotFoundError:
    #1.3 The file may not exist on first run.  If so just skip the loading of the dictionary:
        pass

#2. Show dictionary contents:
print(dictStudentColors)


#3. Ask for more input: 

sName = "x"
while sName != "":
    sName = input("Name: ")
    if sName == "": break

    # Or can write this way with NO Warning:
    if sName not in dictStudentColors:
        sColor = input(sName +" favorite color is: ")
        dictStudentColors[sName] = sColor


#4. Output File 
output_file = open('student_colors.dat', 'wb')
pickle.dump(dictStudentColors, output_file)
output_file.close()


#5. Output the dictionary contents that were written to disk:        
        
print(dictStudentColors)


for key, value in dictStudentColors.items():
    print('Key is', key, 'Value:',value)
    




    


    




