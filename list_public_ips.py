
import boto.ec2 


if __name__ == '__main__':
    conn = boto.ec2.connect_to_region("us-west-2")
    for a in conn.get_all_addresses():
        print "%s" % (a.public_ip)
