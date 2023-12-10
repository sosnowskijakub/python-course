acronyms = {"LOL": "laugh out loud",
            "IDK": "i don't know",
            "TBH": "to be honest"}

print(acronyms["LOL"])

#adding to empty dictionary
acronyms1 = {}

acronyms1["LOL"] = "laugh out loud"
acronyms1["IDK"] = "i don't know"
acronyms1["TBH"] = "to be honest"

print(acronyms1)

#updating value
acronyms2 = {"LOL": "laugh out loud",
            "IDK": "i don't know",
            "TBH": "to be honest"}

acronyms2["LOL"] = "lolz"

print(acronyms2)

#deleting
acronyms3 = {"LOL": "laugh out loud",
            "IDK": "i don't know",
            "TBH": "to be honest"}

del acronyms3["LOL"]

print(acronyms3)

#none definition
acronyms = {"LOL": "laugh out loud",
            "IDK": "i don't know",
            "TBH": "to be honest"}
definition = acronyms.get("BTW")

if definition:
    print(definition)
else:
    print("Key doesn't exist")

#using dictionary to translate sentence

acronyms = {"LOL": "laugh out loud",
            "IDK": "i don't know",
            "TBH": "to be honest"}

sentence = acronyms.get("IDK") + " what happend " + acronyms.get("TBH") #thanks to get method there will be no error if acronym has no translation

print(sentence)