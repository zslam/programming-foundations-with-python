from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7952c0c534ba0df26c26866d3287a678"
# Your Auth Token from twilio.com/console
auth_token  = "851a64ae882224efc18dc2bb98b3de85"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+201095355081",
    from_="+19842070677",
    body="Hello from Python twilio!")

print(message.sid)
