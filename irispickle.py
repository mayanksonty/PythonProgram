# Use of Pickle Module

import requests
import pickle

# requesting data from uci machine learning dataset
r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

# Writing a Respose in text file
with open("iris.txt","a") as f:
    f.write(r.text)

# reading the text file and by using split creating list 
with open("iris.txt","r") as ob:
    r = ob.read()

# List created
rsplitted = r.split("\n")

# Start of pickling process making a pkl file
file = "iris.pkl"
fileobj = open(file, 'wb')
pickle.dump(rsplitted, fileobj)
fileobj.close()

# retriving a pkl file and accesing the list
file = "iris.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(rsplitted)
print(type(mycar))
