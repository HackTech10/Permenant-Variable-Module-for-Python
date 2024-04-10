#create
def create(file_name, variable_name, variable_value):
    #creates file if not created
    varfile = open(file_name+".txt","at")
    varfile.close()
    #opens in reader mode
    varfile =  open(file_name+".txt","rt")
    cont = 1
    #looks for if variable exists
    for i in varfile:
        if variable_name+": " in i:
            print("Variable seems to already exist")
            cont = 0
    varfile.close()
    varfile = open(file_name+".txt","at")
    #if it doesnt exist, it adds it
    if cont:
        varfile.write("\n"+variable_name+": "+variable_value)
    varfile.close()
#save
def save(file_name, variable_name, variable_value): 
    #opens the file in reader mode and finds variable it wants to update
    varfile = open(file_name+".txt","rt")
    varbuffer = []
    line = ""
    for j in varfile:
        if variable_name+": " in j:
            line = variable_name+": "+variable_value
        else: line = j
        varbuffer.append(line)
    varfile.close()
    #clears txt file and updates entire thing
    varfile = open(file_name+".txt","wt")
    varfile.close()
    varfile = open(file_name+".txt","at")
    for k in varbuffer:
        if k != "\n":  varfile.write("\n"+k)
    varfile.close()
#delete
def delete(file_name, variable_name):
    varfile = open(file_name+".txt","rt")
    varbuffer = []
    for o in varfile:
        if variable_name+": " in o:
            pass
        else:
            varbuffer.append(o)
    varfile.close()
    #clears txt file and updates entire thing
    varfile = open(file_name+".txt","wt")
    varfile.close()
    varfile = open(file_name+".txt","at")
    for p in varbuffer:
        if p != "\n":  varfile.write("\n"+p)
    varfile.close()
#read
def read(file_name, variable_name): 
    varfile = open(file_name+".txt","rt")
    #finds target variable, gets entire line and removes the variable name
    for l in varfile:
        if variable_name+": " in l:
            varia = l.replace(variable_name+": ","")
            return varia
#list
def dump(file_name):
    #gets all variable values from the file and outputs them
    varfile =  open(file_name+".txt","rt")
    listo = []
    for m in varfile:
        if m != "\n": listo.append(m)
    varfile.close()
    return listo
#help
def help():
    hep = [
"",
"This module is a tool that creates, stores, and reads variables from a generated .txt file",
"Included functions:",
".create(<filename>, <variable name> ,<variable value>)",
" - creates a variable and sets a value",
" - only needs to be ran once",
" - it is best practice follow standard python variable naming conventions"
".save(<filename>, <variable name> ,<variable value>)",
" - sets a value of a variable",
".delete(<filename>, <variable name>)",
" - removes the variable and its value from storage",
" - variable must be created again if you need it",
".read(<filename>, <variable name>) - " ,
" - returns the value of the specified variable",
".dump(<filename>)",
" - returns a list of all the variables and their value from the specified file",
"** The filename value is to allow you to use this with multiple projects/files", 
"It is recommended that the filename be the same name as the project and set as a constant variable",
"",
    ]
    for n in hep:
        print(n)
