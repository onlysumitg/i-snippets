import json
import json5
from os import walk
import os
from tomark import Tomark



if __name__ =="__main__":
    finalList = []
    for (dirpath, dirnames, filenames) in walk("./snippets"):
        for filename in filenames:
            if filename.endswith(".code-snippets"):
                print(dirpath,":",dirnames, filename)
                # Opening JSON file
                f = open( os.path.join(dirpath, filename))

                
                # returns JSON object as 
                # a dictionary
                data = json5.load(f)
                print("type", type(data))

                for k, v in data.items():

                    print("------", k,":::" ,v.get("description",""), "::",v.get("prefix",""))
                    trigger = v.get("prefix","")
                    if type(trigger) == list:
                        trigger = ",".join(trigger)


                    
                    finalDict = {"Scope" :v.get("scope",""),"Description":v.get("description","") , "Trigger":trigger}
                    finalList.append(finalDict)

    mdTable= Tomark.table(finalList)
    print(mdTable)