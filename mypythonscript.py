import uuid
import requests
import threading

url = "https://api.sfelc.com/graphql"
roomId = "64a3e962b0cf6c68ec1a2165"
meetupId = "64a3e962b0cf6c68ec1a2144"
message = "We're no strangers to love, You know the rules and so do I, A full commitment's what I'm thinking of, You wouldn't get this from any other guy, I just wanna tell you how I'm feeling, Gotta make you understand, Never gonna give you up, Never gonna let you down, Never gonna run around and desert you, Never gonna make you cry, Never gonna say goodbye, Never gonna tell a lie and hurt you."
ticketOptionId = "64a3e962b0cf6c68ec1a214c"
UserAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_6_9; like Mac OS X) AppleWebKit/533.21 (KHTML, like Gecko)  Chrome/50.0.1242.176 Mobile Safari/600.8"
TOKEN1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY0YWMyYTYyZWI1MjFhMGRlNWM2NGRiMyIsImlhdCI6MTY4OTA1NjA1NX0.ap3MlveTV-XF4mz8SW15GMVD9JLEUbUh6O8bkAScALE"
TOKEN2 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY0YWNkODZiMDViNDI1OTFiYzgyZmYxYyIsImlhdCI6MTY4OTA1NjEzMn0.mrJ8J-4jXRS5C9GVbzUpyHK58rVV1RcJIbkZaQM3H8w"
TOKEN3 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY0YWNkYWM4NWVlZTkxMjNkZWEyMWYzNyIsImlhdCI6MTY4OTA0OTgwMX0.X-JzTm2f3f3WMXuygIjJllfGPtcn7yW8bVb5PdOAOt0"
TOKEN4 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY0YWNmNDFkZWI1MjFhMGRlNWM5M2U0OCIsImlhdCI6MTY4OTA1NjI4Nn0.vf-OS4zynOGX5OrMnEI5J6r8-VU4Op4FaFhrLv6Eq2s"
TOKEN5 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY0YWNmNGFmNWVlZTkxMjNkZWEyNmZhZSIsImlhdCI6MTY4OTA1Njc3M30.T7cTLuMWabJ_j8-0I93W2Gq5qLNUT49NP-3XK7KIJNU"
TOKEN6 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY0YWNmN2I3MjI1MDgwMGJiNzQyNjhlMSIsImlhdCI6MTY4OTA1NzIwOH0.ZX4QNUPwhnnAZ1qoZsp6Ty5PXj7s0lpavvx634WCeBM"
TOKEN7 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY0YWNmODI5YmFmODdjNmVkOGRkZDkzNyIsImlhdCI6MTY4OTA1NzMyMX0.pCH34GhEPimuz1ByAfsiYxRIQj7bscZI0juj5TIHzP4"
TOKEN8 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY0YWNmODkwMzlkZGQ5ZTczYWJhNzhiOSIsImlhdCI6MTY4OTA1NzQyNX0.FxsRvBD8GSgJFJA7P1OrLlDsXkPYOk1s2IkEU_Q5RqM"
TOKEN9 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY0YWNmOTBiNWVlZTkxMjNkZWEyODBjNCIsImlhdCI6MTY4OTA1NzU0OH0.gcK0cY4BNjbaew3kgASF39L5tW0HlYf3Xcsypc17JVE"
TOKEN10 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY0YWNmOThkNWVlZTkxMjNkZWEyODI0YiIsImlhdCI6MTY4OTA1NzY3N30.ERBU3rkuyZ6ebAcYKL0GOzU5_A6iS0rWQf5NwQ0aKjE"
TOKEN11 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY0YWNmOWY3MWJjYjE1MGRmN2Y5MzNjMCIsImlhdCI6MTY4OTA1Nzc4NH0.NdN0lyg2aEVaSaKD0QLXquTEMSxnXjNGHYTVsjDdDgY"
TOKEN12 = ""
TOKEN13 = ""
TOKEN14 = ""

joindata = {
  "operationName": "submitRSVP",
  "variables": {
    "id": meetupId,
    "registerFrom": "Gradual",
    "userTrafficData": {
      "referUrl": "https://events.roblox.com/home?view=explore",
      "userAgent": UserAgent
    },
    "ticketOptionId": ticketOptionId,
    "paymentInfo": {
      "provider": "stripe",
      "paymentToken": "",
      "amount": 0
    }
  },
  "query": "mutation submitRSVP($id: String!, $registerFrom: AttendeeRegisterFromInput, $preRegistrationFormAnswers: [MeetupPreRegistrationFormAnswerInput], $referralCode: String, $userTrafficData: UserTrafficDataInput, $paymentInfo: EventRegistrationPaymentInfoInput, $ticketOptionId: String) {\n  event: submitRSVP(\n    id: $id\n    registerFrom: $registerFrom\n    preRegistrationFormAnswers: $preRegistrationFormAnswers\n    referralCode: $referralCode\n    userTrafficData: $userTrafficData\n    paymentInfo: $paymentInfo\n    ticketOptionId: $ticketOptionId\n  ) {\n    id\n    name\n    startedAt\n    endedAt\n    attendee {\n      id\n      paid\n      slug\n      displayName\n      firstName\n      lastName\n      pictureUrl\n      virtualTicketUrl\n      virtualTicketNo\n      ticketOptionId\n      ...PaymentInfoFragment\n      __typename\n    }\n    openForRSVP\n    __typename\n  }\n}\n\nfragment PaymentInfoFragment on Attendee {\n  id\n  userId\n  tenantUser {\n    id\n    email\n    __typename\n  }\n  ticketOptionId\n  payment {\n    id\n    amount\n    discount\n    originalPrice\n    refundAmount\n    paymentMethod\n    ticketOption {\n      id\n      name\n      __typename\n    }\n    transactions: successTransactions {\n      ...MeetupPaymentTransaction\n      __typename\n    }\n    createdAt\n    __typename\n  }\n  __typename\n}\n\nfragment MeetupPaymentTransaction on MeetupPaymentTransaction {\n  id\n  paymentCard\n  paymentMethod\n  amount\n  transactionType\n  createdAt\n  __typename\n}\n"
}

join = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN1, 'User-Agent': UserAgent}, json=joindata)
print('Joined to event bot 1: ' + join.text)
join = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN2, 'User-Agent': UserAgent}, json=joindata)
print('Joined to event bot 2: ' + join.text)
join = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN3, 'User-Agent': UserAgent}, json=joindata)
print('Joined to event bot 3: ' + join.text)
join = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN4, 'User-Agent': UserAgent}, json=joindata)
print('Joined to event bot 4: ' + join.text)
join = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN5, 'User-Agent': UserAgent}, json=joindata)
print('Joined to event bot 5: ' + join.text)
join = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN6, 'User-Agent': UserAgent}, json=joindata)
print('Joined to event bot 6: ' + join.text)
join = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN7, 'User-Agent': UserAgent}, json=joindata)
print('Joined to event bot 7: ' + join.text)
join = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN8, 'User-Agent': UserAgent}, json=joindata)
print('Joined to event bot 8: ' + join.text)
join = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN9, 'User-Agent': UserAgent}, json=joindata)
print('Joined to event bot 9: ' + join.text)
join = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN10, 'User-Agent': UserAgent}, json=joindata)
print('Joined to event bot 10: ' + join.text)
join = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN11, 'User-Agent': UserAgent}, json=joindata)
print('Joined to event bot 11: ' + join.text)
#join = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN12, 'User-Agent': UserAgent}, json=joindata)
#print('Joined to event bot 12: ' + join.text)
#join = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN13, 'User-Agent': UserAgent}, json=joindata)
#print('Joined to event bot 13: ' + join.text)
#join = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN14, 'User-Agent': UserAgent}, json=joindata)
#print('Joined to event bot 14: ' + join.text)

def bot1():
  while True:
    uuidstr = str(uuid.uuid4())

    chatdata1 = {
  "operationName": "SubmitMessage",
  "variables": {
    "roomId": roomId,
    "messageString": message,
    "authorType": "USER",
    "clientReferenceId": uuidstr,
    "messageMetaData": {
      "meetupId": meetupId,
      "from": "live",
      "client": "live"
    }
  },
  "query": "mutation SubmitMessage($roomId: String!, $messageString: String!, $authorType: String, $clientReferenceId: String, $messageMetaData: MessageMetaDataInput) {\n  message: submitMessage(\n    roomId: $roomId\n    messageString: $messageString\n    authorType: $authorType\n    clientReferenceId: $clientReferenceId\n    messageMetaData: $messageMetaData\n  ) {\n    id\n    __typename\n  }\n}\n"
}
    chat = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN1, 'User-Agent': UserAgent}, json=chatdata1)
    print('Chat bot 1: ' + chat.text)
    
def bot2():
  while True:
    uuidstr = str(uuid.uuid4())

    chatdata1 = {
  "operationName": "SubmitMessage",
  "variables": {
    "roomId": roomId,
    "messageString": message,
    "authorType": "USER",
    "clientReferenceId": uuidstr,
    "messageMetaData": {
      "meetupId": meetupId,
      "from": "live",
      "client": "live"
    }
  },
  "query": "mutation SubmitMessage($roomId: String!, $messageString: String!, $authorType: String, $clientReferenceId: String, $messageMetaData: MessageMetaDataInput) {\n  message: submitMessage(\n    roomId: $roomId\n    messageString: $messageString\n    authorType: $authorType\n    clientReferenceId: $clientReferenceId\n    messageMetaData: $messageMetaData\n  ) {\n    id\n    __typename\n  }\n}\n"
}
    chat = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN2, 'User-Agent': UserAgent}, json=chatdata1)
    print('Chat bot 2: ' + chat.text)
    
def bot3():
  while True:
    uuidstr = str(uuid.uuid4())

    chatdata1 = {
  "operationName": "SubmitMessage",
  "variables": {
    "roomId": roomId,
    "messageString": message,
    "authorType": "USER",
    "clientReferenceId": uuidstr,
    "messageMetaData": {
      "meetupId": meetupId,
      "from": "live",
      "client": "live"
    }
  },
  "query": "mutation SubmitMessage($roomId: String!, $messageString: String!, $authorType: String, $clientReferenceId: String, $messageMetaData: MessageMetaDataInput) {\n  message: submitMessage(\n    roomId: $roomId\n    messageString: $messageString\n    authorType: $authorType\n    clientReferenceId: $clientReferenceId\n    messageMetaData: $messageMetaData\n  ) {\n    id\n    __typename\n  }\n}\n"
}
    chat = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN3, 'User-Agent': UserAgent}, json=chatdata1)
    print('Chat bot 3: ' + chat.text)
    
def bot4():
  while True:
    uuidstr = str(uuid.uuid4())

    chatdata1 = {
  "operationName": "SubmitMessage",
  "variables": {
    "roomId": roomId,
    "messageString": message,
    "authorType": "USER",
    "clientReferenceId": uuidstr,
    "messageMetaData": {
      "meetupId": meetupId,
      "from": "live",
      "client": "live"
    }
  },
  "query": "mutation SubmitMessage($roomId: String!, $messageString: String!, $authorType: String, $clientReferenceId: String, $messageMetaData: MessageMetaDataInput) {\n  message: submitMessage(\n    roomId: $roomId\n    messageString: $messageString\n    authorType: $authorType\n    clientReferenceId: $clientReferenceId\n    messageMetaData: $messageMetaData\n  ) {\n    id\n    __typename\n  }\n}\n"
}
    chat = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN4, 'User-Agent': UserAgent}, json=chatdata1)
    print('Chat bot 4: ' + chat.text)
    
def bot5():
  while True:
    uuidstr = str(uuid.uuid4())

    chatdata1 = {
  "operationName": "SubmitMessage",
  "variables": {
    "roomId": roomId,
    "messageString": message,
    "authorType": "USER",
    "clientReferenceId": uuidstr,
    "messageMetaData": {
      "meetupId": meetupId,
      "from": "live",
      "client": "live"
    }
  },
  "query": "mutation SubmitMessage($roomId: String!, $messageString: String!, $authorType: String, $clientReferenceId: String, $messageMetaData: MessageMetaDataInput) {\n  message: submitMessage(\n    roomId: $roomId\n    messageString: $messageString\n    authorType: $authorType\n    clientReferenceId: $clientReferenceId\n    messageMetaData: $messageMetaData\n  ) {\n    id\n    __typename\n  }\n}\n"
}
    chat = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN5, 'User-Agent': UserAgent}, json=chatdata1)
    print('Chat bot 5: ' + chat.text)
    
def bot6():
  while True:
    uuidstr = str(uuid.uuid4())

    chatdata1 = {
  "operationName": "SubmitMessage",
  "variables": {
    "roomId": roomId,
    "messageString": message,
    "authorType": "USER",
    "clientReferenceId": uuidstr,
    "messageMetaData": {
      "meetupId": meetupId,
      "from": "live",
      "client": "live"
    }
  },
  "query": "mutation SubmitMessage($roomId: String!, $messageString: String!, $authorType: String, $clientReferenceId: String, $messageMetaData: MessageMetaDataInput) {\n  message: submitMessage(\n    roomId: $roomId\n    messageString: $messageString\n    authorType: $authorType\n    clientReferenceId: $clientReferenceId\n    messageMetaData: $messageMetaData\n  ) {\n    id\n    __typename\n  }\n}\n"
}
    chat = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN6, 'User-Agent': UserAgent}, json=chatdata1)
    print('Chat bot 6: ' + chat.text)
    
def bot7():
  while True:
    uuidstr = str(uuid.uuid4())

    chatdata1 = {
  "operationName": "SubmitMessage",
  "variables": {
    "roomId": roomId,
    "messageString": message,
    "authorType": "USER",
    "clientReferenceId": uuidstr,
    "messageMetaData": {
      "meetupId": meetupId,
      "from": "live",
      "client": "live"
    }
  },
  "query": "mutation SubmitMessage($roomId: String!, $messageString: String!, $authorType: String, $clientReferenceId: String, $messageMetaData: MessageMetaDataInput) {\n  message: submitMessage(\n    roomId: $roomId\n    messageString: $messageString\n    authorType: $authorType\n    clientReferenceId: $clientReferenceId\n    messageMetaData: $messageMetaData\n  ) {\n    id\n    __typename\n  }\n}\n"
}
    chat = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN7, 'User-Agent': UserAgent}, json=chatdata1)
    print('Chat bot 7: ' + chat.text)
    
def bot8():
  while True:
    uuidstr = str(uuid.uuid4())

    chatdata1 = {
  "operationName": "SubmitMessage",
  "variables": {
    "roomId": roomId,
    "messageString": message,
    "authorType": "USER",
    "clientReferenceId": uuidstr,
    "messageMetaData": {
      "meetupId": meetupId,
      "from": "live",
      "client": "live"
    }
  },
  "query": "mutation SubmitMessage($roomId: String!, $messageString: String!, $authorType: String, $clientReferenceId: String, $messageMetaData: MessageMetaDataInput) {\n  message: submitMessage(\n    roomId: $roomId\n    messageString: $messageString\n    authorType: $authorType\n    clientReferenceId: $clientReferenceId\n    messageMetaData: $messageMetaData\n  ) {\n    id\n    __typename\n  }\n}\n"
}
    chat = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN8, 'User-Agent': UserAgent}, json=chatdata1)
    print('Chat bot 8: ' + chat.text)
    
def bot9():
  while True:
    uuidstr = str(uuid.uuid4())

    chatdata1 = {
  "operationName": "SubmitMessage",
  "variables": {
    "roomId": roomId,
    "messageString": message,
    "authorType": "USER",
    "clientReferenceId": uuidstr,
    "messageMetaData": {
      "meetupId": meetupId,
      "from": "live",
      "client": "live"
    }
  },
  "query": "mutation SubmitMessage($roomId: String!, $messageString: String!, $authorType: String, $clientReferenceId: String, $messageMetaData: MessageMetaDataInput) {\n  message: submitMessage(\n    roomId: $roomId\n    messageString: $messageString\n    authorType: $authorType\n    clientReferenceId: $clientReferenceId\n    messageMetaData: $messageMetaData\n  ) {\n    id\n    __typename\n  }\n}\n"
}
    chat = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN9, 'User-Agent': UserAgent}, json=chatdata1)
    print('Chat bot 9: ' + chat.text)
    
def bot10():
  while True:
    uuidstr = str(uuid.uuid4())

    chatdata1 = {
  "operationName": "SubmitMessage",
  "variables": {
    "roomId": roomId,
    "messageString": message,
    "authorType": "USER",
    "clientReferenceId": uuidstr,
    "messageMetaData": {
      "meetupId": meetupId,
      "from": "live",
      "client": "live"
    }
  },
  "query": "mutation SubmitMessage($roomId: String!, $messageString: String!, $authorType: String, $clientReferenceId: String, $messageMetaData: MessageMetaDataInput) {\n  message: submitMessage(\n    roomId: $roomId\n    messageString: $messageString\n    authorType: $authorType\n    clientReferenceId: $clientReferenceId\n    messageMetaData: $messageMetaData\n  ) {\n    id\n    __typename\n  }\n}\n"
}
    chat = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN10, 'User-Agent': UserAgent}, json=chatdata1)
    print('Chat bot 10: ' + chat.text)
    
def bot11():
  while True:
    uuidstr = str(uuid.uuid4())

    chatdata1 = {
  "operationName": "SubmitMessage",
  "variables": {
    "roomId": roomId,
    "messageString": message,
    "authorType": "USER",
    "clientReferenceId": uuidstr,
    "messageMetaData": {
      "meetupId": meetupId,
      "from": "live",
      "client": "live"
    }
  },
  "query": "mutation SubmitMessage($roomId: String!, $messageString: String!, $authorType: String, $clientReferenceId: String, $messageMetaData: MessageMetaDataInput) {\n  message: submitMessage(\n    roomId: $roomId\n    messageString: $messageString\n    authorType: $authorType\n    clientReferenceId: $clientReferenceId\n    messageMetaData: $messageMetaData\n  ) {\n    id\n    __typename\n  }\n}\n"
}
    chat = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN11, 'User-Agent': UserAgent}, json=chatdata1)
    print('Chat bot 11: ' + chat.text)
    
def bot12():
  while True:
    uuidstr = str(uuid.uuid4())

    chatdata1 = {
  "operationName": "SubmitMessage",
  "variables": {
    "roomId": roomId,
    "messageString": message,
    "authorType": "USER",
    "clientReferenceId": uuidstr,
    "messageMetaData": {
      "meetupId": meetupId,
      "from": "live",
      "client": "live"
    }
  },
  "query": "mutation SubmitMessage($roomId: String!, $messageString: String!, $authorType: String, $clientReferenceId: String, $messageMetaData: MessageMetaDataInput) {\n  message: submitMessage(\n    roomId: $roomId\n    messageString: $messageString\n    authorType: $authorType\n    clientReferenceId: $clientReferenceId\n    messageMetaData: $messageMetaData\n  ) {\n    id\n    __typename\n  }\n}\n"
}
    chat = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN12, 'User-Agent': UserAgent}, json=chatdata1)
    print('Chat bot 12: ' + chat.text)
    
def bot13():
  while True:
    uuidstr = str(uuid.uuid4())

    chatdata1 = {
  "operationName": "SubmitMessage",
  "variables": {
    "roomId": roomId,
    "messageString": message,
    "authorType": "USER",
    "clientReferenceId": uuidstr,
    "messageMetaData": {
      "meetupId": meetupId,
      "from": "live",
      "client": "live"
    }
  },
  "query": "mutation SubmitMessage($roomId: String!, $messageString: String!, $authorType: String, $clientReferenceId: String, $messageMetaData: MessageMetaDataInput) {\n  message: submitMessage(\n    roomId: $roomId\n    messageString: $messageString\n    authorType: $authorType\n    clientReferenceId: $clientReferenceId\n    messageMetaData: $messageMetaData\n  ) {\n    id\n    __typename\n  }\n}\n"
}
    chat = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN13, 'User-Agent': UserAgent}, json=chatdata1)
    print('Chat bot 13: ' + chat.text)
    
def bot14():
  while True:
    uuidstr = str(uuid.uuid4())

    chatdata1 = {
  "operationName": "SubmitMessage",
  "variables": {
    "roomId": roomId,
    "messageString": message,
    "authorType": "USER",
    "clientReferenceId": uuidstr,
    "messageMetaData": {
      "meetupId": meetupId,
      "from": "live",
      "client": "live"
    }
  },
  "query": "mutation SubmitMessage($roomId: String!, $messageString: String!, $authorType: String, $clientReferenceId: String, $messageMetaData: MessageMetaDataInput) {\n  message: submitMessage(\n    roomId: $roomId\n    messageString: $messageString\n    authorType: $authorType\n    clientReferenceId: $clientReferenceId\n    messageMetaData: $messageMetaData\n  ) {\n    id\n    __typename\n  }\n}\n"
}
    chat = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN14, 'User-Agent': UserAgent}, json=chatdata1)
    print('Chat bot 14: ' + chat.text)
    
def react1():
  while True:

    likereact = {
    "operationName": "sendEmoji",
    "variables": {
      "roomId": roomId,
      "meetupId": meetupId,
      "emoji": "thumbUp"
    },
    "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
  }

    # thinking
    thinkreact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "thinking"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    # smile
    smilereact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "smile"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    like = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN1, 'User-Agent': UserAgent}, json=likereact)
    print('Like bot 1: ' + like.text)
    think = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN1, 'User-Agent': UserAgent}, json=thinkreact)
    print('Think bot 1: ' + like.text)
    smile = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN1, 'User-Agent': UserAgent}, json=smilereact)
    print('Smile bot 1: ' + like.text)
    
def react2():
  while True:

    likereact = {
    "operationName": "sendEmoji",
    "variables": {
      "roomId": roomId,
      "meetupId": meetupId,
      "emoji": "thumbUp"
    },
    "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
  }

    # thinking
    thinkreact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "thinking"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    # smile
    smilereact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "smile"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    like = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN2, 'User-Agent': UserAgent}, json=likereact)
    print('Like bot 2: ' + like.text)
    think = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN2, 'User-Agent': UserAgent}, json=thinkreact)
    print('Think bot 2: ' + like.text)
    smile = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN2, 'User-Agent': UserAgent}, json=smilereact)
    print('Smile bot 2: ' + like.text)
    
def react3():
  while True:

    likereact = {
    "operationName": "sendEmoji",
    "variables": {
      "roomId": roomId,
      "meetupId": meetupId,
      "emoji": "thumbUp"
    },
    "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
  }

    # thinking
    thinkreact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "thinking"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    # smile
    smilereact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "smile"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    like = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN2, 'User-Agent': UserAgent}, json=likereact)
    print('Like bot 3: ' + like.text)
    think = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN2, 'User-Agent': UserAgent}, json=thinkreact)
    print('Think bot 3: ' + like.text)
    smile = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN2, 'User-Agent': UserAgent}, json=smilereact)
    print('Smile bot 3: ' + like.text)
    
def react4():
  while True:

    likereact = {
    "operationName": "sendEmoji",
    "variables": {
      "roomId": roomId,
      "meetupId": meetupId,
      "emoji": "thumbUp"
    },
    "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
  }

    # thinking
    thinkreact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "thinking"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    # smile
    smilereact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "smile"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    like = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN4, 'User-Agent': UserAgent}, json=likereact)
    print('Like bot 4: ' + like.text)
    think = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN4, 'User-Agent': UserAgent}, json=thinkreact)
    print('Think bot 4: ' + like.text)
    smile = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN4, 'User-Agent': UserAgent}, json=smilereact)
    print('Smile bot 4: ' + like.text)
    
def react5():
  while True:

    likereact = {
    "operationName": "sendEmoji",
    "variables": {
      "roomId": roomId,
      "meetupId": meetupId,
      "emoji": "thumbUp"
    },
    "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
  }

    # thinking
    thinkreact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "thinking"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    # smile
    smilereact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "smile"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    like = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN5, 'User-Agent': UserAgent}, json=likereact)
    print('Like bot 5: ' + like.text)
    think = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN5, 'User-Agent': UserAgent}, json=thinkreact)
    print('Think bot 5: ' + like.text)
    smile = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN5, 'User-Agent': UserAgent}, json=smilereact)
    print('Smile bot 5: ' + like.text)
    
def react6():
  while True:

    likereact = {
    "operationName": "sendEmoji",
    "variables": {
      "roomId": roomId,
      "meetupId": meetupId,
      "emoji": "thumbUp"
    },
    "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
  }

    # thinking
    thinkreact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "thinking"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    # smile
    smilereact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "smile"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    like = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN6, 'User-Agent': UserAgent}, json=likereact)
    print('Like bot 6: ' + like.text)
    think = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN6, 'User-Agent': UserAgent}, json=thinkreact)
    print('Think bot 6: ' + like.text)
    smile = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN6, 'User-Agent': UserAgent}, json=smilereact)
    print('Smile bot 6: ' + like.text)
    
def react7():
  while True:

    likereact = {
    "operationName": "sendEmoji",
    "variables": {
      "roomId": roomId,
      "meetupId": meetupId,
      "emoji": "thumbUp"
    },
    "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
  }

    # thinking
    thinkreact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "thinking"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    # smile
    smilereact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "smile"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    like = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN7, 'User-Agent': UserAgent}, json=likereact)
    print('Like bot 7: ' + like.text)
    think = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN7, 'User-Agent': UserAgent}, json=thinkreact)
    print('Think bot 7: ' + like.text)
    smile = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN7, 'User-Agent': UserAgent}, json=smilereact)
    print('Smile bot 7: ' + like.text)
    
def react8():
  while True:

    likereact = {
    "operationName": "sendEmoji",
    "variables": {
      "roomId": roomId,
      "meetupId": meetupId,
      "emoji": "thumbUp"
    },
    "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
  }

    # thinking
    thinkreact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "thinking"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    # smile
    smilereact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "smile"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    like = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN8, 'User-Agent': UserAgent}, json=likereact)
    print('Like bot 8: ' + like.text)
    think = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN8, 'User-Agent': UserAgent}, json=thinkreact)
    print('Think bot 8: ' + like.text)
    smile = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN8, 'User-Agent': UserAgent}, json=smilereact)
    print('Smile bot 8: ' + like.text)
    
def react9():
  while True:

    likereact = {
    "operationName": "sendEmoji",
    "variables": {
      "roomId": roomId,
      "meetupId": meetupId,
      "emoji": "thumbUp"
    },
    "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
  }

    # thinking
    thinkreact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "thinking"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    # smile
    smilereact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "smile"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    like = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN9, 'User-Agent': UserAgent}, json=likereact)
    print('Like bot 9: ' + like.text)
    think = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN9, 'User-Agent': UserAgent}, json=thinkreact)
    print('Think bot 9: ' + like.text)
    smile = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN9, 'User-Agent': UserAgent}, json=smilereact)
    print('Smile bot 9: ' + like.text)
    
def react10():
  while True:

    likereact = {
    "operationName": "sendEmoji",
    "variables": {
      "roomId": roomId,
      "meetupId": meetupId,
      "emoji": "thumbUp"
    },
    "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
  }

    # thinking
    thinkreact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "thinking"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    # smile
    smilereact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "smile"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    like = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN10, 'User-Agent': UserAgent}, json=likereact)
    print('Like bot 10: ' + like.text)
    think = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN10, 'User-Agent': UserAgent}, json=thinkreact)
    print('Think bot 10: ' + like.text)
    smile = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN10, 'User-Agent': UserAgent}, json=smilereact)
    print('Smile bot 10: ' + like.text)

def react11():
  while True:

    likereact = {
    "operationName": "sendEmoji",
    "variables": {
      "roomId": roomId,
      "meetupId": meetupId,
      "emoji": "thumbUp"
    },
    "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
  }

    # thinking
    thinkreact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "thinking"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    # smile
    smilereact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "smile"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    like = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN11, 'User-Agent': UserAgent}, json=likereact)
    print('Like bot 11: ' + like.text)
    think = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN11, 'User-Agent': UserAgent}, json=thinkreact)
    print('Think bot 11: ' + like.text)
    smile = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN11, 'User-Agent': UserAgent}, json=smilereact)
    print('Smile bot 11: ' + like.text)
    
def react12():
  while True:

    likereact = {
    "operationName": "sendEmoji",
    "variables": {
      "roomId": roomId,
      "meetupId": meetupId,
      "emoji": "thumbUp"
    },
    "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
  }

    # thinking
    thinkreact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "thinking"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    # smile
    smilereact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "smile"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    like = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN12, 'User-Agent': User-Agent}, json=likereact)
    print('Like bot 12: ' + like.text)
    think = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN12, 'User-Agent': UserAgent}, json=thinkreact)
    print('Think bot 12: ' + like.text)
    smile = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN12, 'User-Agent': UserAgent}, json=smilereact)
    print('Smile bot 12: ' + like.text)
    
def react13():
  while True:

    likereact = {
    "operationName": "sendEmoji",
    "variables": {
      "roomId": roomId,
      "meetupId": meetupId,
      "emoji": "thumbUp"
    },
    "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
  }

    # thinking
    thinkreact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "thinking"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    # smile
    smilereact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "smile"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    like = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN13, 'User-Agent': User-Agent}, json=likereact)
    print('Like bot 13: ' + like.text)
    think = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN13, 'User-Agent': User-Agent}, json=thinkreact)
    print('Think bot 13: ' + like.text)
    smile = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN13, 'User-Agent': User-Agent}, json=smilereact)
    print('Smile bot 13: ' + like.text)
    
def react14():
  while True:

    likereact = {
    "operationName": "sendEmoji",
    "variables": {
      "roomId": roomId,
      "meetupId": meetupId,
      "emoji": "thumbUp"
    },
    "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
  }

    # thinking
    thinkreact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "thinking"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    # smile
    smilereact = {
      "operationName": "sendEmoji",
      "variables": {
        "roomId": roomId,
        "meetupId": meetupId,
        "emoji": "smile"
      },
      "query": "mutation sendEmoji($roomId: String!, $meetupId: String, $emoji: String!) {\n  sendEmoji(roomId: $roomId, meetupId: $meetupId, emoji: $emoji)\n}\n"
    }

    like = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN14, 'User-Agent': User-Agent}, json=likereact)
    print('Like bot 14: ' + like.text)
    think = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN14, 'User-Agent': User-Agent}, json=thinkreact)
    print('Think bot 14: ' + like.text)
    smile = requests.post(url, headers={'Authorization': 'Bearer ' + TOKEN14, 'User-Agent': User-Agent}, json=smilereact)
    print('Smile bot 14: ' + like.text)
    
botthread1 = threading.Thread(target=bot1)
botthread2 = threading.Thread(target=bot2)
botthread3 = threading.Thread(target=bot3)
botthread4 = threading.Thread(target=bot4)
botthread5 = threading.Thread(target=bot5)
botthread6 = threading.Thread(target=bot6)
botthread7 = threading.Thread(target=bot7)
botthread8 = threading.Thread(target=bot8)
botthread9 = threading.Thread(target=bot9)
botthread10 = threading.Thread(target=bot10)
botthread11 = threading.Thread(target=bot11)
botthread12 = threading.Thread(target=bot12)
botthread13 = threading.Thread(target=bot13)
botthread14 = threading.Thread(target=bot14)
reactspam1 = threading.Thread(target=react1)
reactspam2 = threading.Thread(target=react2)
reactspam3 = threading.Thread(target=react3)
reactspam4 = threading.Thread(target=react4)
reactspam5 = threading.Thread(target=react5)
reactspam6 = threading.Thread(target=react6)
reactspam7 = threading.Thread(target=react7)
reactspam8 = threading.Thread(target=react8)
reactspam9 = threading.Thread(target=react9)
reactspam10 = threading.Thread(target=react10)
reactspam11 = threading.Thread(target=react11)
reactspam12 = threading.Thread(target=react12)
reactspam13 = threading.Thread(target=react13)
reactspam14 = threading.Thread(target=react14)
botthread1.start()
botthread2.start()
botthread3.start()
botthread4.start()
botthread5.start()
botthread6.start()
botthread7.start()
botthread8.start()
botthread9.start()
botthread10.start()
botthread11.start()
#botthread12.start()
#botthread13.start()
#botthread14.start()
reactspam1.start()
reactspam2.start()
reactspam3.start()
reactspam4.start()
reactspam5.start()
reactspam6.start()
reactspam7.start()
reactspam8.start()
reactspam9.start()
reactspam10.start()
reactspam11.start()
#reactspam12.start()
#reactspam13.start()
#reactspam14.start()
