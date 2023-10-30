from twilio.rest import Client

account_sid = "account_sid"
auth_token = 'auth_token'
client = Client(account_sid, auth_token)
def sendSms():
    message = client.messages.create(
    from_='+15408604350',
    body='Alert Something Detected Into it',
    to='+919999091100'
    )

    print(message.sid)