import requests
import pandas

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

APIkey = input("Enter your API key: ")
print()
print("Enter the user ID of the player who's bazaar info you'd like to check: ")
userID = input("(leave blank if your own) ")

response = requests.get("https://api.torn.com/user/" + userID + "?selections=bazaar&key=" + APIkey)

resList = response.json()["bazaar"]

for i in resList:
  del i["type"]
  del i["ID"]

bazaarData = pandas.json_normalize(resList)

print(bazaarData)

'''for i in response.json()["bazaar"]:
  print(i["name"]+" - "+str(i["quantity"]))
'''