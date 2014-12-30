
import boto.ec2 
import WH


site_id=40466
if __name__ == '__main__':
    wh = WH.WH()
    wh.connect()
    conn = boto.ec2.connect_to_region("us-west-2")
    for a in conn.get_all_addresses():
        print "%s" % (a.public_ip)
        print wh.add_allowed_host(site_id,"http",a.public_ip).request
        print wh.add_allowed_host(site_id,"https",a.public_ip).request
        print wh.add_entry_point(site_id,"GET","http://" + a.public_ip + "/").request
        print wh.add_entry_point(site_id,"GET","https://" + a.public_ip + "/").request
