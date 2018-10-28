import logging
import argparse

import ssh_authorizer.commands as commands
from ssh_authorizer.helpers import parse_ssh_string


logging.basicConfig(format='%(message)s', level=logging.INFO)


def get(args):
    user, host, port = parse_ssh_string(args.ssh_string[0])
    commands.get(user, host, port, args.raw)


def add(args):
    user, host, port = parse_ssh_string(args.ssh_string[0])
    commands.add(user, host, port, args.keys)


def delete(args):
    user, host, port = parse_ssh_string(args.ssh_string[0])
    commands.delete(user, host, port, args.keys)


def main():
    parser = argparse.ArgumentParser(description='Manager for remote ~/.ssh/authorized_keys.')
    subparsers = parser.add_subparsers(dest='cmd', help='Commands')
    # parser_help = subparsers.add_parser('help', help='')

    parser_get = subparsers.add_parser('get', help='Display remote authorized_keys')
    parser_get.add_argument('--raw', action='store_true', help='Display as is.')
    parser_get.add_argument('ssh_string', nargs=1, help='Remote host')
    parser_get.set_defaults(func=get)

    parser_add = subparsers.add_parser('add', help='Add keys to remote authorized_keys')
    parser_add.add_argument('ssh_string', nargs=1, help='Remote host')
    parser_add.add_argument('keys', nargs='*', help='Keys for add')
    parser_add.set_defaults(func=add)

    parser_del = subparsers.add_parser('del', help='Delete keys from remote authorized_keys')
    parser_del.add_argument('ssh_string', nargs=1, help='Remote host')
    parser_del.add_argument('keys', nargs='+', help='Keys indexes for remote')
    parser_del.set_defaults(func=delete)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()