import WH

conn = WH.WH()
conn.connect()
r = conn.add_allowed_host(40466,"https","nunahealth.com")
print r.text
