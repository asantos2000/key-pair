import argparse
import paramiko
import os.path
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('host', action='store', help='host to connect to')
parser.add_argument('-p', '--port', action='store', dest='port', default='22', help='port to connect to')
parser.add_argument('--known_hosts', action='store', dest='known_hosts', default='~/.ssh/known_hosts', help='known_hosts file')
args = parser.parse_args()

host = args.host
port = args.port
known_hosts = os.path.expanduser(args.known_hosts)

transport = paramiko.Transport(host, port)

transport.connect()
key = transport.get_remote_server_key()
print(key.get_base64())
transport.close()

hostfile = paramiko.HostKeys(filename=known_hosts)
hostfile.add(hostname = host, key=key, keytype=key.get_name())

hostfile.save(filename=known_hosts)