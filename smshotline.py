# The following is code written by Gatlin Newhouse <- DO NOT REMOVE THIS
import urllib
import urllib2
class gateway:
    'Class for the SMS gateway API info'
    def __init__(self, user, password, api_id, mo, frm):
        self.user = user    # Your API Username
        self.password = password    # Your API Password
        self.api_id = api_id    # Your API ID
        self.mo = mo    # Just set this to 1
        self.frm = frm  # Number to send the texts from
    def send(self, number, msg):    # This sends the message to a given number
        url = "https://api.clickatell.com/http/sendmsg?user="+ self.user + "&password=" + self.password + "&api_id="+ self.api_id +"&mo=" + self.mo + "&from=" + self.frm + "&to=" + number + "&text=" + makemessagewebready(msg)
        urllib2.urlopen(url).read()
def makemessagewebready(msg):   # This converts the message into a webfriendly URL message
    return msg.replace(" ", "%20")
