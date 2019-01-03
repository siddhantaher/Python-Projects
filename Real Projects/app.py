import json
from difflib import get_close_matches

data=json.load(open('data.json'))

def translate(w):

   w=w.lower()
   if w in data:
        return data[w]
   elif w.title() in data:
        return data[w.title()]
   elif w.upper() in data:  # in case user enters words like USA or NATO
       return data[w.upper()]
   elif len(get_close_matches(w,data.keys()))>0:
       close=get_close_matches(w, data.keys())[0]
       yn= raw_input ('Did you mean {} instead? Enter Y is yes, or N for no : ' .format(close))
       if yn=="Y":
           return data[get_close_matches(w,data.keys())[0]]
       elif yn=="N":
           return ('Word not found, try another one')
       else:
           return ("We didnt understand your entry")

   else:
        return ('Word not found, try another one')


word=raw_input('Enter words : ')

output=(translate(word))
if type(output)==list:
    for item in output:
        print item
else:
    print output