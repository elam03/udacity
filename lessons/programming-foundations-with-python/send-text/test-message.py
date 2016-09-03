import json
import twilio
from twilio.rest import TwilioRestClient

print('twilio version: ' + twilio.__version__)

def load_twilio_credentials():
    json_data = open("twilio-account-info.json").read()
    return json.loads(json_data)

data = load_twilio_credentials()

account_sid    = data["account_sid"]
auth_token     = data["auth_token"]
twilio_number  = data["twilio_number"]
send_to_number = data["send_to_number"]

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Python again! Yet again! 34",
    to=send_to_number,    # Replace with your phone number
    from_=twilio_number)  # Replace with your Twilio number

print(message.sid)
