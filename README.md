UrlShortner
------------------------

This is a web application written on *Pythoh*, *Flask* and *MySql Db*.
SQLAlchemy is used as the ORM.

It covers the following use-case:-

- For every long url, return a short url, which when clicked on, should redirect to the longer url.

- This short url should be used only once.
  In case of multiple concurrent requests trying to access the same short url, only the first request should be redirected and the url should be epired. 
  All the rest of the requests should error out.
  
 
Build & Run Instructions
--------------------

Prerequisites:
   - Python, 
   - Git,
   - pip

**Clone Repository:-**

`git clone https://github.com/100Rashmi/UrlShortner.git`

**Go into the Folder:-**

`cd UrlShortner`

**Install Dependencies:-**

`pip install -r requirements.txt`

**Run the App:-**

`python flaskapp.py`
