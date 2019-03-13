from twilio.rest import Client
dial_at = "+91"+input("Please enter the mobile number :- ")
print(dial_at)
reciver = Client("ACa06442b9f7309e5ddd5cba8cb16f48ce",
    "5864ff44d8836b2bc00a3f58fa8f255a")
reciver.calls.create(
    url="http://demo.twilio.com/docs/voice.xml",
    to=dial_at,
    from_="+12542800135"
)
print("Dialing " + dial_at)
