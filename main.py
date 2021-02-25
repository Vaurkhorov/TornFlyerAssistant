import requests
import json
import ast
import pandas

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

APIkey = "tbpgdzp1u2BoyAJg" #input("Enter your API key: ")

response = requests.get("https://api.torn.com/user/2178000?selections=bazaar&key=" + APIkey)

resList = response.json()["bazaar"]

for i in resList:
  del i["type"]
  del i["ID"]

bazaarData = pandas.json_normalize(resList)

print(bazaarData)

'''for i in response.json()["bazaar"]:
  print(i["name"]+" - "+str(i["quantity"]))
'''