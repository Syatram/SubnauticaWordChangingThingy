import re
import random

f = open("English.json", "r")

# An array of endings I want to put at the end of each value.
endings = ["Nyaa!!~", "UwU", "OwO", "TvT", "TwT", ":3", ">:3",">_<", ">:("]

# Finds elements in the json \".+"*: is the key and *\".+\" is the value
matches = re.findall("\".+\"*:*\".+\"", f.read())
f.close()

for i in range(len(matches)):
    # Gets rid of the " at the end of the value
    matches[i] = matches[i][0:len(matches[i])-1]
    # Adds a random ending to the value
    matches[i] += " " + endings[random.randint(0, len(endings)-1)] + "\""


newF = open("NewEnglish.json", "w")
newF.write("{\n")
for i in range(len(matches)):
    # If i is not the last match add a comma after the value
    if not i == len(matches)-1:
        newF.write("\t" + matches[i] + ",\n")
    else: # Since i is the last match add a closing brace on the next line
        newF.write("\t" + matches[i] + "\n}")
newF.close()
