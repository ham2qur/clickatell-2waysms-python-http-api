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
# To Do:
# * Make it accept incoming messages
# * Program commands to add/remove hotline responders to/from a list
# * Forward all other messages without commands to the hotline list
# * Allow hotline responders to 'claim' a case and then establish a conversation
#   between the user and the responder who claimed them
# * Add ability to terminate this conversation
# Script plugs into Receiving API and sending API to run the program
