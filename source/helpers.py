from functools import reduce
import operator


##
# Returns the value of specific item in config files, eg, endpoints
#
# @params dict, str, eg. endpoints, 'sites.sitesAll.uri'
# @return mix eg. endpoints['sites']['sitesAll']['uri']
#
def getValue(dictionary, config_path):
    pathList = config_path.split(".")

    return_val = reduce(operator.getitem, pathList, dictionary)
    return return_val
