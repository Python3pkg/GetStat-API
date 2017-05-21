import urllib.request
import urllib.parse
import json

from collections import defaultdict

from . import endpoints, helpers

class GetStatAPI:
	##
	# Instantiation of the class 
	#
	# @params str, str
	# @return void
	#
	def __init__(self, subdomain, apiKey):
		self.apiKey = apiKey
		self.subdomain = subdomain
		self.format = 'format=json'
		self.apiResponse = None


	## 
	# get the request URL by endpoint and params
	#
	# @params string, string
	# @return string (URL)
	#
	def get_base_URL(self, endpoint):

		# validate endpoint and params
		all_endpoints = self.getEndpointList(endpoints.Endpoints)
		if endpoint not in all_endpoints:
			raise Exception('Make sure the endpoint you passed is correct')

		requestURL = 'https://' + self.subdomain + '.getstat.com/api/v2/' + self.apiKey + endpoint

		return requestURL

	##
	# Get json formated response from a request URL
	#
	# @params string, url
	# @return dict
	#
	def getResponse(self, url):
		response = urllib.request.urlopen(url).read().decode("utf-8")
		json_response = json.loads(response)
		return json_response

	# #
	# recurse through a dictionary,
	# return the all the values and nested values as list
	#
	# @params dict
	# @return list
	#
	def getEndpointList(self, parse_dict):
	    list_final = []
	    def setMergedList(parse_dict):
	        for key, value in list(parse_dict.items()):
	            if isinstance(value, dict):
	                setMergedList(value)
	            elif not isinstance(value, list):
	                list_final.append(value)
	    setMergedList(parse_dict)
	    return list_final

	##
	# get the url parameters for the API call
	#
	# @params
	# @return 
	#
	def getParams(self, parseParams):
		params = defaultdict(dict)
		for key, value in list(parseParams.items()):
			params[key] = value
		params_encoded = urllib.parse.urlencode(params)

		return params_encoded


	#
	# Get API response from endpoint, 
	# @params str, endpoint, example(/sites/all)
	# @return dict
	#
	def getResponseURL(self, endpoint, params=None):
		if not params == None:
			url = self.get_base_URL(endpoint) + '?' + params + '&' + self.format
		else: url = self.get_base_URL(endpoint) + '?' +  self.format
		return url
	
	##
	# get all the methods from the getStatAPI class
	#
	# @params
	# @return
	#
	def getAllMethods(self, endpoints):
	    methods = defaultdict(dict)
	    def setmethods(endpoints):
	        for key, value in list(endpoints.items()):
	            if 'uri' in value:
	                methods[key] = value
	            else:
	                setmethods(value)
	    setmethods(endpoints)
	    return dict(methods)
		

	##
	# Filter the returned result 
	#
	# @params string, string
	# @return apiResponse
	#
	def filterResult(self, key, parseFilter):
		if self.apiResponse == None:
			raise Exception('must have validated API response')

		filteredResult = defaultdict(dict)

		for i in self.apiResponse:
			if parseFilter in helpers.getValue(i, key):
				filteredResult[helpers.getValue(i, key)] = i
		return filteredResult

	##
	# Similar to __call() magic function in php
	# eg. getRankings(params)
	#
	# @ params str, name: the name of the specific endpoint
	# @ params endpoint query strings
	#
	def __getattr__(self, name, **kwargs):

		def call(**kwargs):
			# get all the endpoints options
			allOptions = self.getAllMethods(endpoints.Endpoints)

			#
			tmp = name.replace('get', '')
			option = tmp[0].lower() + tmp[1:]
			params = kwargs

			if not option in allOptions:
				raise Exception('call to undefined method')

			if 'params' not in allOptions[option]:
				if len(params) != 0: raise Exception('Invalid parameters passed')
				responseURL = self.getResponseURL(helpers.getValue(allOptions, option + '.uri'))
			else:
				for param in params:
					if param not in helpers.getValue(allOptions, option + '.params') or len(params) == 0:
						raise Exception('Invalid parameters passed')

				responseURL = self.getResponseURL(helpers.getValue(allOptions, option + '.uri'),
												  self.getParams(params))
			
			self.apiResponse = self.getResponse(responseURL)['Response']['Result']
			return self
		
		return call
		# getTagList(site_id=2342).filter()
		
