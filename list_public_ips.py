
import boto.ec2 
import WH


if __name__ == '__main__':
    wh = WH.WH()
    wh.connect()
    conn = boto.ec2.connect_to_region("us-west-2")
    for a in conn.get_all_addresses():
        print "%s" % (a.public_ip)
