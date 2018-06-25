from twilio.rest import Client

account = "Your_account"
token = "Your_account_token"
client = Client(account, token)
num=['any phone number','any phone number']

for i in range(0,len(num)):
    message = client.messages.create(num[i], from_="your twilo phone number",
                                 body="Hello")