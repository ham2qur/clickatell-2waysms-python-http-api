# The following is code written by Gatlin Newhouse <- DO NOT REMOVE THIS
from flask import Flask, request
from smshotline import gateway
app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
   data = request.data
   value = reasonAboutIncomingMessage(data)
   return value

if __name__ == '__main__':
   app.run()

def reasonAboutIncomingMessage(httppoststring)
    phonenumberindex = httppoststring.rfind("&from=")
    smshotlinenumberindex = httppoststring.rfind("&to=")
    messageindex = httppoststring.rfind("&text=")
    charactersetindex = httppoststring.rfind("&charset=")
    phonenumber = httppoststring[phonenumberindex:smshotlinenumberindex]
    message = decodewebmessage(httppoststring[messageindex:charactersetindex])
    subscriberlist = []
    if "SUBSCRIBE" in message:
        subscriberlist.insert(phonenumber)
        return "OK"
    else if "UNSUBSCRIBE" in message:
        subscriberlist.remove(phonenumber)
        return "OK"
    else if "CLAIM" in message:
        //establish proxy convo between user and claimer on seperate thread
    else:
        message = message + "Their phone number is: " + formatphonenumber(phonenumber)
        for s in subscriberlist:
            gw.send(phonenumber, message)
        return "OK"
def decodewebmessage(msg):   # This converts the message from webfriendly URL message into plaintext
    return msg.replace("%20", " ")
def formatphonenumber(nmbr):
    return '({}) {}-{}'.format(phone[1:4], phone[4:7], phone[7:])
