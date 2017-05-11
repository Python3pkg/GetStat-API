# GetStat-API
This Package provides an easy and elegant way for you to get the information from your GetStat account.

## Installation
You can install this package via pip, type the following in your command line:

```bash
pip install GetStatAPI

```

## Basic Usage

Require the package at the top of your file, you will need all the modules

```python
from GetStatAPI import main, endpoints, helpers
```

Instantiation:
replace the SUBDOMAIN and APIKEY with your own
```Python
stats = main.GetStatAPI(SUBDOMAIN, APIKEY)
```

To make an API call to fetch all the sites on your account
```python
#return an object of main class
sites = stats.getSitesAll()

#fetch the result
sites.apiResponse

#filter result
sites.filterResult('Url', 'www.example.com')

```

## endpoints file
endpoints.py is your configuration file which stores all the API endpoints and required params.
The key of the dictionary elements that contains 'url' and 'params' are your calls to different API endpoints.

Here is an example:

If you want to call the API for fetching all the keywords for a specific site:

Find the following in endpoints.py
```python
  "allKeywords": {
        "uri":"/keywords/list" ,
        "params":["site_id"]
      }
```
In your file, you would want to do:
```python
stats.getAllKeywords(site_id=176)

```

You can add more endpoints onto the endpoints.py file, following the same convention like so:
```python
"name" : { 
  "uri": "/myapi/endpoint"
  "params": ["my_params"]
```
And also make sure such API endpoint is available from GetStat.


## Filtering Result
Once you make a specific API call, you can filter out the result. You can use the dot(.) notation for fetching the dictionary key and nested keys.
```python
# If I want to find the status of a specific ranking url
keywords = stats.getAllKeywords(site_id=123)
returnResult = keywords.filterResult('keywordRankings.Google.Url', 
                                     'www.example.com/2134523/product/my-cool-product')
```
Have fun!

