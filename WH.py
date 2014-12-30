import yaml
import requests
import json
import os
import sys
import urllib
import pprint
api_root="https://sentinel.whitehatsec.com/api"
class WH:
    def __init__(self):
        with open(os.path.expanduser("~") + "/.wh","r") as ymlfile:
            cfg = yaml.load(ymlfile)
            self.password = cfg["password"]
            self.username = cfg["username"]

    def connect(self):
        self.session = requests.session()
        r = self.session.post(
            "%s/user/%s/login" % (api_root,urllib.quote(self.username)), 
            data={"password": self.password})
        #sys.stderr.write(r.text + "\n")
        return r

    def add_allowed_host(self,site_id,scheme,host):
        r = self.session.post(
            "%s/site/%d/allowed_hosts" % (api_root,site_id), 
            data=json.dumps(
                {
                    "scheme":scheme,
                    "hostname":host
                }),
            headers={"Content-Type":"application/json"}
            )
        print r.status_code
        print r.text
        return r

    def add_entry_point(self,site_id,method,url):
        r = self.session.post(
            "%s/site/%d/entry_points" % (api_root,site_id),
            data=json.dumps(
                [{
                    "method": method,
                    "uri"   : url
                }]
                ),
            headers={"Content-Type":"application/json"}
            )
        print r.status_code
        print r.text
        return r

