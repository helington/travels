from twilio.rest import Client

account_sid = 'ACf74115ab56810599d47d50660f94b9cc'
auth_token = '3a7b67d76bc9f25957810b289271eb34'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  to='whatsapp:+559999059334'
)

print(message.sid)