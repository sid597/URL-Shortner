## API documentation

Base_url = 127.0.0.1:5000

### Base_url/shorten/

This route is used to provide the url which needs to be shortned.
Examples:

request : { "url" : "https://www.google.com/"}
response : {"shortned_url" : "Base_url/d", error:""}

### Base_url/<some characters>

This route is used to redirect to the original path.

request: Base_url/d
response: The original url

## Persistance 

I am using the shelve module in python, this provides the following functionallities:

A dictionary of pickled Python objects identified by keys
A dictionary of pickled Python objects identified by keys that can be persisted to a file.
Provide one or more forms of popular DBM implementations. A DBM database in its primitive form is a dictionary that can be persisted to a file.

