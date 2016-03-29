from flask import Flask, request
from smshotline import gateway
app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
   data = request.data
   reasonAboutIncomingMessage(data)
   return "OK"

if __name__ == '__main__':
   app.run()

def reasonAboutIncomingMessage(httppoststring)
    phonenumberindex = httppoststring.rfind("&from=")
    smshotlinenumberindex = httppoststring.rfind("&to=")
    messageindex = httppoststring.rfind("&text=")
    charactersetindex = httppoststring.rfind("&charset=")
    phonenumber = httppoststring[phonenumberindex:smshotlinenumberindex]
    message = httppoststring[messageindex:charactersetindex]
    subscriberlist = []
    if "SUBSCRIBE" in message:
        subscriberlist.insert(phonenumber)
    else if "UNSUBSCRIBE" in message:
        subscriberlist.remove(phonenumber)
    else if "CLAIM" in message:
        //establish proxy convo between user and claimer on seperate thread
    else:
        for s in subscriberlist:
            gw.send(phonenumber, message)
