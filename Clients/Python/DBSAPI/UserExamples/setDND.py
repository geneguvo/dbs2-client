#!/usr/bin/env python
#
# Revision: $"
# $Id: setDND.py,v 1.1 2009/06/01 16:00:38 afaq Exp $ 
#
import sys
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *
from DBSAPI.dbsOptions import DbsOptionParser

optManager  = DbsOptionParser()
(opts,args) = optManager.getOpt()
api = DbsApi(opts.__dict__)

try:
	if len(sys.argv) < 2:
		print "Missing dataset path"
		print "USAGE: "+sys.argv[0]+" /specify/dataset/path"
		sys.exit(1)
	path = sys.argv[1]
	api.updateProcDSStatus(path, "DONOTDISPLAY")

except DbsApiException, ex:
  print "Caught API Exception %s: %s "  % (ex.getClassName(), ex.getErrorMessage() )
  if ex.getErrorCode() not in (None, ""):
    print "DBS Exception Error Code: ", ex.getErrorCode()

print "Done"

