# Permenant-Variable-Module-for-Python
Probably already a thing and not worth posting but an empty Github page is weird.
Allows you to store python variables and their values between executions to return straight back to where it left off.
It can aslo be used to share variable values between python scripts running at the same time (good luck getting syncing right though)

This module is a tool that creates, stores, and reads variables from a generated .txt file
Included functions:
.create(<filename>, <variable name> ,<variable value>)
 - creates a variable and sets a value
 - only needs to be ran once
 - it is best practice follow standard python variable naming conventions
.save(<filename>, <variable name> ,<variable value>)
 - sets a value of a variable
.delete(<filename>, <variable name>)
 - removes the variable and its value from storage
 - variable must be created again if you need it
.read(<filename>, <variable name>) - 
 - returns the value of the specified variable
.dump(<filename>)
 - returns a list of all the variables and their value from the specified file
** The filename value is to allow you to use this with multiple projects/files
It is recommended that the filename be the same name as the project and set as a constant variable to avoid clashes
