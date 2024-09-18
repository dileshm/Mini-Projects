from twilio.rest import client

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

message = client.messages.create(
    from =""
    body="SENT IN PYTHON"
    to=""
)

print(message.sid)
