from twilio.rest import Client

account = "AC6ac96158bda1b5d814035373b8b64329"
token = "f761d8b7a336aa746dbb533053a0ae74"
client = Client(account, token)
num=['+8801674206688','+8801937261969']

for i in range(0,len(num)):
    message = client.messages.create(num[i], from_="+16677716206",
                                 body="Hello")