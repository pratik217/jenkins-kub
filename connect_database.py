from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': 'secure-connect-prat-bbl-sl-poc1.zip'
}
auth_provider = PlainTextAuthProvider('LogFMFeiXJcWxzKdoGwTmFbv', 'R2XvFPkDxwa+LGsytS2kl8Z_gQ+GbAav,rc61cwJGw9-sDSy.6TZYnBvQ3OHDO+TP4X--XsA0gT347t_-AzOZYRYOXi8nXpt-l5mTPcUzpmAN3vkPAhHvY8hOHchX_NA')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")
