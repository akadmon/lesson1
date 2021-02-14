dicte = {"city":"Moscow", "temperature": "20"}
print (dicte["city"])
newtemp = int(dicte["temperature"]) - 5
dicte["temperature"] = newtemp
print (dicte)

dicte["country"] = "Russia"
dicte["date"] = "27.05.2019"
print (len(dicte)) 