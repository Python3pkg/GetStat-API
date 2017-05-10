Endpoints = {

	"projects" : {
		"ProjectList" : {
			"uri":"/projects/list",
		}
	},

	"sites": {
		# return all the sites on the account
		# @params void
		"sitesAll" : {
				"uri":"/sites/all"
				},

		# return the list of website from a specific project folder
		#
		# @params siteID
		"sitesbyProjectFolder": {
				"uri": "/site/list",
				"params": ["project_id"]
		},

		# return rank distribution of a site
		# @params id(siteID), from_date, to_date
		"RankDistribution": {
				"uri":"/sites/ranking_distributions",
				"params":['id', 'from_date', 'to_date'],
		}
	},

	# endpoint for tags category
	"tags" : {

		"tagList": {
			"uri":"/tags/list",
			"params": ["site_id"]
		},

	},

	"keywords": {
		# returns all keywords saved under the specified site.
		"allKeywords": {
			"uri":"/keywords/list" ,
			"params":["site_id"]
		}
	},

	# ranking over time for specific keyword
	#@params keyword_id, from_date, to_date
	"rankings": {
		"uri":"/rankings/list",
		"params":["keyword_id","from_date","to_date"]
	},

	# returns the archived SERP for the specified search engine and date.
	# including the type of result, eg,regular, answer etc
	"serpData": {
		"uri":"/serps/show",
		"params": ["keyword_id","engine","date"]
	}

	#allKeyword+rankings
}
