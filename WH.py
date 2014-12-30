import yaml
import requests
import json
import os
import sys
import urllib
class WH:
    def __init__(self):
        with open(os.path.expanduser("~") + "/.wh","r") as ymlfile:
            cfg = yaml.load(ymlfile)
            self.password = cfg["password"]
            self.username = cfg["username"]

    def connect(self):
        r = requests.post("https://sentinel.whitehatsec.com/api/user/%s/login" % urllib.quote(self.username), data={"password": self.password})
        print(r.url)
        self.cookies=r.cookies
        #sys.stderr.write(r.text + "\n")
        return r

    def add_allowed_host(self,site_id,scheme,host):
        r = requests.post("https://sentinel.whitehatsec.com/api/site/%d/allowed_hosts" % site_id, data=json.dumps({"scheme":scheme,"host":host}), cookies=self.cookies)
        return r
