import WH
import boto.ec2
import json
import re

wh_site_id = 40466
if __name__ == '__main__':
  wh = WH.WH()
  wh.connect()
  ahs = wh.get_allowed_hosts(wh_site_id)['allowed_hosts']
  eps = wh.get_entry_points(wh_site_id)['entry_points']
  sorted_ahs = [ h for h in sorted(ahs, key=lambda a: a['hostname'],) if re.search('\d+(\.\d+){3}',h['hostname'])]
  conn = boto.ec2.connect_to_region("us-west-2")
  ec2addrs = conn.get_all_addresses()
  new = set([addr.public_ip for addr in ec2addrs if addr.public_ip])
  old = set([addr['hostname'] for addr in sorted_ahs])
  hosts_to_add = new - old
  hosts_to_del = old - new
  for addr in hosts_to_del:
      print "Del %s" % addr
  for addr in hosts_to_add:
      print "Add %s" % addr



