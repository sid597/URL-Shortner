from api import app
from flask import request, redirect, jsonify
import string


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

base64_characters = string.ascii_letters + '0123456789'

def convert_to_base64(num):
    '''
    same concept as converting from base 10 to binary (base2)
    say we want to convert 10 in binary
    write its remainder when divided by 2 then we divide it by 2 
    num = X
    num % 2 = 0, num /= 2
    
    for 10:
    10 % 2 = 0, num = 5
    5 % 2 = 1, num = 2
    2 % 2 = 0, num = 1
    1 % 2 = 1, num =0
    
    in binary 10 is -> 1010 
    
    '''
    encoded = []
    while num > 0:
        remainder  = num % 64
        encoded.append(base64_characters[remainder])
        num /= 64
    return ''.join(encoded[::-1])


LONG_TO_ID = {} # used to check if the new url is already shortned 
ID_TO_LONG = {} # used to return the original long url in case of read

COUNTER = 0
BASE_URL = 'http://127.0.0.1:5000'

@app.route('/shorten/', methods=['GET', 'POST'])
def shorten():
    '''
    check if url received
    check if already shortned
    if not increase counter and create a new id 
    update the dicts and return
    '''

    global COUNTER
    if request.method == 'POST':
        url = request.json['url']
        if url:
            # print(url)

            # see if this url is already shortned
            if url in LONG_TO_ID:
                res = jsonify(shortned_url = BASE_URL + LONG_TO_ID[url], error = "")
                # print(res)
                return  res
        
            COUNTER += 1
            id = convert_to_base64(COUNTER)
            LONG_TO_ID[url] = id
            ID_TO_LONG[id] = url
        
            res = jsonify(shortned_url = BASE_URL + id, error = "")
            # print(res)
            return res
        else:
            return jsonify(error = "no url received")
    return ""
        

@app.route('/<id>')
def redirect_to_long_url(id):
    if id in ID_TO_LONG:
        url = ID_TO_LONG[id] 
        # print(url)
        return redirect(url)
    return "not a valid id"



#