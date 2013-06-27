#!/usr/bin/env python
#
# Revision: 1.3 $"
# Id: DBSXMLParser.java,v 1.3 2006/10/26 18:26:04 afaq Exp $"
#
#
import sys
#from dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser
from DBSAPI.dbsApi import DbsApi

try:
  optManager  = DbsOptionParser()
  (opts,args) = optManager.getOpt()

  api = DbsApi(opts.__dict__)

  serverInfo = api.getServerInfo()
  print "Server Version : ", serverInfo['ServerVersion']
  print "Schema Version : ", serverInfo['SchemaVersion']
  print serverInfo
  
except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()      

