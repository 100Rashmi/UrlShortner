UrlShortner
------------------------

This is a web application developed with *Python*, *Flask* and *MySql Db*.

*SQLAlchemy* is used as the ORM.

It covers the following use-cases:-

- For every long url, return a short url, which when clicked on, should redirect to the longer url.

- This short url should be used only once.
 
- In case of multiple concurrent requests trying to access the same short url, only the first request should be redirected and the url should be expired. All the other requests should be errored out.
 
 All the rest of the requests should error out.
  
 
Build & Run Instructions
--------------------

Prerequisites:
   - Python
   - Git
   - pip
   - MySql

**Clone Repository:-**

`git clone https://github.com/100Rashmi/UrlShortner.git`

**Go into the Folder:-**

`cd UrlShortner/`

**Install Dependencies:-**

`pip install -r requirements.txt`

**Configure Mysql:-**

In  [commons/constants.py file here.](https://github.com/100Rashmi/UrlShortner/blob/master/commons/constants.py#L4) 

**Run the App:-**

`python flaskapp.py`

The application starts at http://localhost:5000/

API Documentation
---------------------------
- **1. POST /create** Create Short Url

**Request:-**

```
curl -X POST \
http://127.0.0.1:5000/create \
-d '{ "long_url" : "https://github.com/100Rashmi/UrlShortner"}'
```
**Response:-**

```
StatusCode : 201
{"short_url": "http://localhost:5000/<somecode>"}
``` 


- **2. GET:** Hit the Short Url
```
curl http://localhost:5000/<somecode>
```

**Response**

*On Success:*
```
StatusCode : 302,  
Redirecting to <Long Url>..
```

*On Expire:*
```
StatusCode : 498,
{"message": "expired"}
```

*On Wrong Short Url:*
```
StatusCode : 404
{"message": "not found"}
```

Data Model:
-----------------


- Table : `urlinfo`

| Field          | Type          | Null | Key | Default | Extra |
|----------------|---------------|------|-----|---------|-------|
| url_id         | INT           | NO   | PRI | NULL    |       |
| status         | VARCHAR(32)   |      |     | NULL    |       |
| long_url       | VARCHAR(2048) |      |     | NULL    |       |
| created_time   | DATETIME      |      |     | NULL    |       |
| updated_time   | DATETIME      |      |     | NULL    |       |
| short_url      | VARCHAR(32)   |      | UNI | NULL    |       |


