#!/usr/bin/env/python

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/home/willy/anaconda3/lib/python3.7/site-packages")
sys.path.insert(0, "/home/willy/github_willyrv/hello_world_flask")
from hello_world_flask import app as application
application.secret_key = "a;sleri302AW#I)@#iaWEAOIf9$DS"
