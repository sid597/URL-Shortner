
NOTE: Throughout this file <b>Base_url</b> means `<b>127.0.0.1:5000</b>`

## How to build the project ? 

1. Build the docker image : ` docker build -t urlshortner .`
2. Run the image in detached mode on port 5000 : `docker run -d -p 5000:5000 urlshortner` 
3. Now can serve the api's on `http://localhost:5000/<api endpoint>`

<i>NOTE: localhost is set to `127.0.0.1`</i>

## Testing the project 

1. To run test you need to have python3 installed
2. In the base directory of this project do:
    - `python3 -m venv venv`
    - `source venv/bin/activate`
3. Run the tests using `python3 tests.py`


### What does the test cover ?

1. Tests the function to convert base 10 numbers to base 64
2. Shorten the url `http://github.com/sid597/infracloud`, which would return  `http://Base_url/b`
3. Converts back the shortned url in previous point to the original one.


## API documentation

### API to shorten a long url
 
 <b>API ENDPOINT : Base_url/shorten/ </b>


This route is used to provide the url which needs to be shortned. Request accepts `JSON` with the following mentioned fields. 
Examples:

request type : `POST`
request body: `{ "url" : "https://www.google.com/"}`
response : `{"shortned_url" : "Base_url/d", error:""}`

### API to get back the original URL from a shortned one

<b> API ENDPOINT : Base_url/<shortned url> </b>

This route is used to redirect to the original path. You make a get request with the shortned url and get the original url as response.

Example :
request type : `GET`
request : Base_url/d
response: Redirects to the original url

## How is persistance handles ? 

I am using the shelve module in python, this provides the following functionallities:

A dictionary of pickled Python objects identified by keys
A dictionary of pickled Python objects identified by keys that can be persisted to a file.
Provide one or more forms of popular DBM implementations. A DBM database in its primitive form is a dictionary that can be persisted to a file.

