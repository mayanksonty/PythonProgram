import re


mystr ='''Todaywearegoingto learn how we can make command-line 
utility in python and the benefits and uses of making a 
command-line utility. Let us get a brief overview of the command-line utility.

What Is a Command Line Utility?
A command-line utility is a way 
of giving operating system instructions 
using lines of texts. Command-line programs operate 
mayank.verma@gmail.com
sonty@gmail.com
via command line or PowerShell. It will interact with a command-line script.
Now let us come to the why part that 
why we should
mv@gmail.com
harry@gmail.com
jitendra.nirnejak@inkoop.in
use the command-line utility 
in our program. We can call a command line program 
in python or any other language into a different language 
program easily as each program has calling support in it for 
calling the command lines program. So in cases, were are writing 
a program in some other language, but we want to perform a task in Python 
and call it in our program, then the command line can help us to do that.

Now we are going to discuss how part of this tutorial. 
For creating a Command Line Utility In Python, first import two modules i.e., argsparse and sys. argsparse helps us to get command-line arguments in our program, and the sys module helps us to import the code we wrote using argparse onto the console. For more details and descriptions about these modules, you can read the python documentation for these modules.'''



# pattern = re.findall(r'[\w\.-]+@[\w\.-]+', mystr)   #used to match the email from the list
pattern = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+",mystr)
# Writing in a file
for item in pattern:
    with open("regx.txt","a") as f:
        str1 = f"{item}\n"
        f.write(str1)

print(pattern)









