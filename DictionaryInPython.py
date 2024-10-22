
monthConversations = {
    "JAN" : "January",
    "FEB": "February",
    "MAR": "MARCH",
    "APR": "APRIL",
    "MAY": "MAY",
    "JUN": "JUNE",
    "JUL": "JULY",
    "AUG": "August",
    "SEP": "September",
    "OCT": "October",
    "NOV": "November",
    "DEC": "December",
}

print(monthConversations["NOV"])

# OR Dictionary.get("key")
print(monthConversations.get("JUL"))
print(monthConversations.get("LUV")) #return None
print(monthConversations.get("LUV", "NOT A VALID KEY")) #return Not a valid key

#print(monthConversations.get("LUV", "NOT A VALID KEY", "NOV"))
#TypeError: get expected at most 2 arguments, got 3


newMonthConversation = {
    1 : "January",
    2 : "February",
    3 : "MARCH",
    4 : "APRIL",
    5 : "MAY",
    6 : "JUNE",
    7 : "JULY",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December",
}

print(newMonthConversation[1])
print(newMonthConversation[12])
print(newMonthConversation[10])
print(newMonthConversation.get(4))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(thisdict["brand"])