from api import app
from flask import request, redirect, jsonify


#
# Make 2 dictionaries which contain mapping from long url to short url (called id)
# and from id to long url.
# Each long url will have a unique id, this will be acheived by using a monotonically
# increasing counter. This counter will then be converted to base64 which is made of 
# characters a-z,A-Z, 0-9. 

# Why is this necessary ? 
# Because we can write big integers in base 10 with less characters in base64
# for example, with 6 characters in base 10 we can represent a maximum of 999,999
# unique url, whereas in base64 we can represent ~5 billion integers

# To convert from long to short I will use a base10 to base64 converter 

def convert_to_base64(num):
    return ''

LONG_TO_ID = {} # used to check if the new url is already shortned 
ID_TO_LONG = {} # used to return the original long url in case of read

@app.route('/shorten/', methods=['GET', 'POST'])
def shorten():

    return ""

@app.route('/<id>')
def redirect_to_long_url(id):

    return redirect("")



