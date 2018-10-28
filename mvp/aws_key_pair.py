import logging
import argparse

import ssh_authorizer.commands as commands
from ssh_authorizer.helpers import parse_ssh_string

import boto3

from paramiko import DSSKey
from paramiko import RSAKey

logging.basicConfig(format='%(message)s', level=logging.INFO)

ec2 = boto3.client('ec2') #https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html

key_dispatch_table = {"dsa": DSSKey, "rsa": RSAKey}

def create(args):
    comment = ''
    key_name = args.key_pair_name[0]
    result = ec2.create_key_pair(KeyName=key_name)
    print('Fingerprint: ', result['KeyFingerprint'])
    with open(key_name, 'w') as fs:
        fs.write(result['KeyMaterial'])
    # Generate pub key
    pub = key_dispatch_table['rsa'](filename=key_name, password='')
    with open("%s.pub" % key_name, "w") as f:
        f.write("%s %s" % (pub.get_name(), pub.get_base64()))
        if comment:
            f.write(" %s" % comment)

def delete(args):
    print(ec2.delete_key_pair(KeyName=args.key_pair_name[0]))


def describe(args):
    print(ec2.describe_key_pairs())

def import_key(args):
    key_name = args.key_pair_name[0]
    with open(f'{key_name}.pub') as fs:
        material = fs.read()
    print(ec2.import_key_pair(KeyName=key_name, PublicKeyMaterial=material))


def main():
    parser = argparse.ArgumentParser(description='AWS EC2 key-pair management')
    subparsers = parser.add_subparsers(dest='cmd', help='Commands')
    # parser_help = subparsers.add_parser('help', help='')

    parser_create = subparsers.add_parser('create', help='Create key-pair')
    parser_create.add_argument('key_pair_name', nargs=1, help='Key name')
    parser_create.set_defaults(func=create)

    parser_delete = subparsers.add_parser('delete', help='Delete key-pair')
    parser_delete.add_argument('key_pair_name', nargs=1, help='Key name')
    parser_delete.set_defaults(func=delete)

    parser_delete = subparsers.add_parser('import', help='Import key-pair')
    parser_delete.add_argument('key_pair_name', nargs=1, help='Key name')
    parser_delete.set_defaults(func=import_key)    

    parser_describe = subparsers.add_parser('describe', help='Describe key-pairs')
    parser_describe.set_defaults(func=describe)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()