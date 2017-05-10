# GetStat-API
This Package provides an easy and elegent way for you to get the information from your GetStat account.

## Installation
You can install this package via pip with:

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

To Make an API call to fetch all the sites on your account
```python
#return an object of main class
sites = stats.getSitesAll()

#fetch the result
sites.apiResponse

#filter result
sites.filterResult('Url', 'www.example.com')

```

## endpoints file
Refer to the endpoints file for different API calls, call to each endpoint, simplely add get + key name(uppercase first letter), for example, if I were to call other API endpoints:
```python
# get all the keywords
# API call requires the parameter need to be passed as an argument
stats.getAllKeywords(site_id=197)

```

You can customize the endpoints however you want, if you prefer to change the name of the keys(such as 'sitesAll', 'rankings', feel free to do so, but 'url' and 'params' cannot be changed.
when the keys are changes, you will need to change the method call using the 'get+' method.



