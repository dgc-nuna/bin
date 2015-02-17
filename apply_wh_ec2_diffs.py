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
  eps_to_delete = [ep['href'] for ep in eps if  ep['uri'] in set([ 'https://' + h for h in hosts_to_del]) | set([ 'http://' + h for h in hosts_to_del])]
  ahs_to_delete = [ah['href'] for ah in ahs if ah['hostname'] in hosts_to_del]
  for ep in eps_to_delete:
      tail = ep[5:] # strip "/api/"
      print "deleting %s" % tail
      r = wh.delete(tail)
  for ah in ahs_to_delete:
      tail = ah[5:] # strip "/api/"
      print "deleting %s" % tail
      r = wh.delete(tail)
      print r
  for a in hosts_to_add:
        print wh.add_allowed_host(wh_site_id,"http",a).request
        print wh.add_allowed_host(wh_site_id,"https",a).request
        print wh.add_entry_point(wh_site_id,"GET","http://" + a + "/").request
        print wh.add_entry_point(wh_site_id,"GET","https://" + a + "/").request
