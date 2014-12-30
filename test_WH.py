import WH

conn = WH.WH()
conn.connect()
r = conn.add_allowed_host(40466,"http","nunahealth.com")
print r.text
