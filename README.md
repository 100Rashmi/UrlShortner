UrlShortner
------------------------

This is a web application developed with *Python*, *Flask* and *MySql Db*.

*SQLAlchemy* is used as the ORM.

It covers the following use-cases:-

- For every long url, return a short url, which when clicked on, should redirect to the longer url.

- This short url should be used only once.
 
- In case of multiple concurrent requests trying to access the same short url, only the first request should be redirected and the url should be expired. 
 
 All the rest of the requests should error out.
  
 
Build & Run Instructions
--------------------

Prerequisites:
   - Python
   - Git
   - pip

**Clone Repository:-**

`git clone https://github.com/100Rashmi/UrlShortner.git`

**Go into the Folder:-**

`cd UrlShortner`

**Install Dependencies:-**

`pip install -r requirements.txt`

**Run the App:-**

`python flaskapp.py`

The application starts at http://localhost:5000/

API Documentation
---------------------------
- **POST** Create Short Url
**Request:-**
```
curl -X POST \
http://127.0.0.1:5000/create \
-d '{ "long_url" : 'https://github.com/100Rashmi/UrlShortner'}'
```
**Response:-**
`{"short_url": "http://localhost:5000/<somecode>"}` 


- **GET:** Hit the Short Url
```
curl http://localhost:5000/somecode
```

**Response**

*On Success:*
```
Status : 302,  Redirect to <Long Url>
```

*On Expire:*
```
Status : 498,
{"message": "expired"}
```

*On Wrong Short Url:*
```
Status : 404
{"message": "not found"}
```

