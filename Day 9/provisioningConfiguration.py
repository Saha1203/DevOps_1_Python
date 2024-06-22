#when setting up monitoring agents on multiple servers:

import subprocess

servers = [
    "server1",
    "server2",
    "server3"
]

def configureMonitoringAgent(server):
    subprocess.run(["configureMonitoringAgent", server])

for server in servers:
    configureMonitoringAgent(server)