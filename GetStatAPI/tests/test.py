import unittest

from . import GetStat

from ..endpoints import Endpoints
from ..GetStatAPI import GetStatAPI
from .. import helpers

class getStatTestCase1(unittest.TestCase):

	def setUp(self):
		self.stats = GetStatAPI(GetStat.SUBDOMAIN, GetStat.APIKEY)

	def testGetValueFunction(self):
		self.assertEqual(helpers.getValue(Endpoints, 'tags.tagList.params'), ['site_id'])


	def testGetValueFunction2(self):

		testDict = {
			'key1': 1,
			'key2': {
				'blah':1, 
				'foo' : {
					'1': 'bar',
					'blah': ['baz', 'boo']
				}
			}

		}

		self.assertEqual(helpers.getValue(testDict, 'key2.foo.blah')[0], 'baz')


	def testGetsitesAll(self):
		self.sites = self.stats.getSitesAll()

		self.assertEqual(helpers.getValue(self.sites.filterResult('Url', "enterprise.co.uk")["www.enterprise.co.uk"], 'Id'), '117')




if __name__ == '__main__':
	unittest.main()