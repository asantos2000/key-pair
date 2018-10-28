# Key-pair

Key-pair is a command-line utility to manage public and private keys among machines in private and public clouds, even in just bare metal or VMs.

## Installing

## Help

[maintain]
copy-public-key (ssh-copy-id)
    --host <value>
    --user-name <value>
    --ssh-public-key-body <value>

create-key-pair (ssh-keygen)
    --key-name <value>

list-remote-public-key (ssh-keyscan)
    --host <value>
    --user-name <value>

remove-remote-public-key (ssh-keyscan)
    --host <value>
    --user-name <value>
    --key-name <value>

aws create-key-pair
    --key-name <value>
    [--dry-run | --no-dry-run]

aws delete-key-pair
    --key-name <value>
    [--dry-run | --no-dry-run]

aws describe-key-pairs
    [--filters <value>]
    [--key-names <value>]

aws import-key-pair
    [--dry-run | --no-dry-run]
    --key-name <value>
    --public-key-material <value>

[store]
aws-iam get-ssh-public-key
    --user-name <value>
    --ssh-public-key-id <value>
    --encoding <value>

aws-iam delete-ssh-public-key
    --user-name <value>
    --ssh-public-key-id <value>

aws-iam list-ssh-public-keys
    [--user-name <value>] - The name of the IAM user to list SSH public keys  for.  If  none  is specified,  the UserName field is determined implicitly based on the AWS access key used to sign the request.

aws-iam update-ssh-public-key
    --user-name <value>
    --ssh-public-key-id <value>
    --status <value>

aws-iam upload-ssh-public-key
    --user-name <value>
    --ssh-public-key-body <value>

aws-s3 get-ssh-public-key
    --bucket-name <value>
    --key-name <value> <value> (s3 key)
    --encoding <value>

aws-s3 delete-ssh-public-key
    --bucket-name <value>
    --key-name <value> <value> (s3 key)

aws-s3 list-ssh-public-keys
    --bucket-name <value>
    [--key-name <value> <value>] (s3 key)

aws-s3 upload-ssh-public-key
    --bucket-name <value>
    --key-name <value> <value> (s3 key)

consul-kv get-ssh-public-key
    --key-name <value>
    --encoding <value>

consul-kv delete-ssh-public-key
    --key-name <value> <value>

consul-kv list-ssh-public-keys
    [--key-name <value> <value>]

consul-kv upload-ssh-public-key
    --key-name <value> <value>
    --ssh-public-key-body <value> (value)

## MVP

```bash
python generate_private_public_keys.py --help
Usage:
generate_private_public_keys.py [-v] [-b bits] -t type [-N new_passphrase] [-f output_keyfile]

Options:
  -h, --help            show this help message and exit
  -t ktype, --type=ktype
                        Specify type of key to create (dsa or rsa)
  -b bits, --bits=bits  Number of bits in the key to create
  -N phrase, --new-passphrase=phrase
                        Provide new passphrase
  -P phrase, --old-passphrase=phrase
                        Provide old passphrase
  -f filename, --filename=filename
                        Filename of the key file
  -q, --quiet           Quiet
  -v, --verbose         Verbose
  -C comment, --comment=comment
                        Provide a new comment
```

```bash
$ python aws_key_pair.py --help
usage: aws_key_pair.py [-h] {create,delete,import,describe} ...

AWS EC2 key-pair management

positional arguments:
  {create,delete,import,describe}
                        Commands
    create              Create key-pair
    delete              Delete key-pair
    import              Import key-pair
    describe            Describe key-pairs

optional arguments:
  -h, --help            show this help message and exit
```

`$ python aws_key_pair.py describe`

```json
{
    " KeyPairs": [
        {
            " KeyFingerprint": " fd:e5: 23: 0b:a0:b4:fb: 7c: 60: 54: 5d:c8: 6b:a7: 35: 63:a8: 39:c9: 04",
            " KeyName": " eks"
        },
        {
            " KeyFingerprint": " 50:ce: 27: 29:d3: 5b: 32: 37:ec:f3: 67:f9: 30: 79:4e:9e:ea: 31: 2f:d1",
            " KeyName": " load-test"
        },
        {
            " KeyFingerprint": " 34: 66: 7b: 73:ba:f4: 49: 51:f7: 7b: 20:f3: 3b: 5f: 38: 99",
            " KeyName": " test"
        },
        {
            " KeyFingerprint": " bf:d3:a9:aa: 4a: 05:c1: 6a: 1c: 9f:a3:ec: 55:be: 0c: 21: 7a: 1d: 6a:4e",
            " KeyName": " testaws"
        }
    ],
    " ResponseMetadata": {
        " RequestId": " d88611dd-8359-42c8-be2a-94dbe50dfd00",
        " HTTPStatusCode": 200,
        " HTTPHeaders": {
            " content-type": " text/xml;charset=UTF-8",
            " content-length": " 917",
            " date": " Sat, 27 Oct 2018 23: 47: 21 GMT" , " server" : " AmazonEC2" 
        },
        " RetryAttempts": 0
    }
}
```

`$ python aws_key_pair.py delete test`

```json
{
    " ResponseMetadata": {
        " RequestId": " ecc11f84-1979-4242-b6f8-f2584e61378e",
        " HTTPStatusCode": 200,
        " HTTPHeaders": {
            " content-type": " text/xml;charset=UTF-8",
            " content-length": " 227",
            " date": " Sat, 27 Oct 2018 23:49:21 GMT",
            " server": " AmazonEC2"
        },
        " RetryAttempts": 0
    }
}
```

`$ python aws_key_pair.py import test`

```json
{
    " KeyFingerprint": " 34:66:7b:73:ba:f4:49:51:f7:7b:20:f3:3b:5f:38:99",
    " KeyName": " test",
    " ResponseMetadata": {
        " RequestId": " 593a80d4-7c72-4f2a-9006-184656b1bf78",
        " HTTPStatusCode": 200,
        " HTTPHeaders": {
            " content-type": " text/xml;charset=UTF-8",
            " content-length": " 314",
            " date": " Sat, 27 Oct 2018 23:28:33 GMT",
            " server": " AmazonEC2"
        },
        " RetryAttempts": 0
    }
}
```

### deploy_auth_keys.py

```bash
(py3) anderson@inspirion:~/dev/ssh-authorizer$ ssh-authorizer --help
usage: ssh-authorizer [-h] {help,get,add,del,test} ...

Manager for remote ~/.ssh/authorized_keys.

positional arguments:
  {help,get,add,del,test}
                        Commands
    help                Display help information
    get                 Display remote authorized_keys
    add                 Add keys to remote authorized_keys
    del                 Delete keys from remote authorized_keys
    test                Test keys exist in remote authorized_keys

optional arguments:
  -h, --help            show this help message and exit
```

```bash
$ python deploy_auth_keys.py --help

usage: deploy_auth_keys.py [-h] {get,add,del} ...

Manager for remote ~/.ssh/authorized_keys.

positional arguments:
  {get,add,del}  Commands
    get          Display remote authorized_keys
    add          Add keys to remote authorized_keys
    del          Delete keys from remote authorized_keys

optional arguments:
  -h, --help     show this help message and exit


$ python deploy_auth_keys.py get anderson@localhost
anderson@localhost:22 - getting authorized_keys
anderson@localhost:22 - found 2 keys:

1: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDU/ql6BZtBcwMr0HgJ2HF/9C7roydWp4KjuAslyn+KVvTMDyGznMO+/z0AkQvEgy4b74wGUva5iLd2Jadgqzdd3kNLb+WPvmrYgFKvkjkNqS5EymHQyLJFo8GacqxotTmjpJSatrFnWpTVcjcH4opfxVmX37RQNfVWJ2CDJan+EdPtkEboqcqavdCvxXI5BQMFVLJCtYHan+ypV8J/FSssREyABr8jcdtiHqJ8CiMstgyziukVeGjyTlK4N2rdMMiH04NitrSfLXypIuOSCTWHXX4UpQPlBm4DDz0kMbHWWn2nw1O1UQ1W8BQoUCQ0FkiKUlNrkP8d7j6p0rgRv6y++z9Y2eL2Q9Ci0ypq7sLR2O9V+leQxVFSY/r3UFU8JW3uhdIDG3wOuU/hW4dJSkXFIVsZMLsqTVS/6GtRYLAvM1jxc8e8ds1Xn1DbmrT8eABWFM01cJOJEDLujXmx/bATwPE4u1NXwsByG/y8sAb/26mOlqNxcxrcZunl3EqC9ZaVYwPg5pkAWzkgiHC5Ls3FHrbW8fEHwOHgzHA+Ypea43PI9lVqO++CIyMhVsiIHSNtaPxJGoVolvHK4WtF4JIOpQKNsZl22PkgS1uC3b/fTKg1aVElUUNg7KeHPb539zpXrXhM+QogqAiTIedQFEvmPU9czaJAQpHIQE3VRCz4dQ== anderson
2: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDqUbeX4sIqVQGpsUlQ6G7ZhabENbEXD8z2375g8Liy45YCr6M2wRbo/0wFGB9kEXqW6/gYUNS+p+U+UXy0WlJLxnoWJaDYx3jGnq4aubWmnkQq1gFjVfYwxcxmRITpEZlrJMYyOW4sDJqf56/zyauFsh6fPRurgSxbdYq/F8mwLQ== adsantos@gmail.com
```

```bash
$ python deploy_auth_keys.py add anderson@localhost testaws.pub
Loading keys: testaws.pub
anderson@localhost:22 - getting authorized_keys
anderson@localhost:22 - writing authorized_keys
```

```bash
$ python deploy_auth_keys.py get anderson@localhost
anderson@localhost:22 - getting authorized_keys
anderson@localhost:22 - found 3 keys:

1: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDU/ql6BZtBcwMr0HgJ2HF/9C7roydWp4KjuAslyn+KVvTMDyGznMO+/z0AkQvEgy4b74wGUva5iLd2Jadgqzdd3kNLb+WPvmrYgFKvkjkNqS5EymHQyLJFo8GacqxotTmjpJSatrFnWpTVcjcH4opfxVmX37RQNfVWJ2CDJan+EdPtkEboqcqavdCvxXI5BQMFVLJCtYHan+ypV8J/FSssREyABr8jcdtiHqJ8CiMstgyziukVeGjyTlK4N2rdMMiH04NitrSfLXypIuOSCTWHXX4UpQPlBm4DDz0kMbHWWn2nw1O1UQ1W8BQoUCQ0FkiKUlNrkP8d7j6p0rgRv6y++z9Y2eL2Q9Ci0ypq7sLR2O9V+leQxVFSY/r3UFU8JW3uhdIDG3wOuU/hW4dJSkXFIVsZMLsqTVS/6GtRYLAvM1jxc8e8ds1Xn1DbmrT8eABWFM01cJOJEDLujXmx/bATwPE4u1NXwsByG/y8sAb/26mOlqNxcxrcZunl3EqC9ZaVYwPg5pkAWzkgiHC5Ls3FHrbW8fEHwOHgzHA+Ypea43PI9lVqO++CIyMhVsiIHSNtaPxJGoVolvHK4WtF4JIOpQKNsZl22PkgS1uC3b/fTKg1aVElUUNg7KeHPb539zpXrXhM+QogqAiTIedQFEvmPU9czaJAQpHIQE3VRCz4dQ== anderson
2: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDqUbeX4sIqVQGpsUlQ6G7ZhabENbEXD8z2375g8Liy45YCr6M2wRbo/0wFGB9kEXqW6/gYUNS+p+U+UXy0WlJLxnoWJaDYx3jGnq4aubWmnkQq1gFjVfYwxcxmRITpEZlrJMYyOW4sDJqf56/zyauFsh6fPRurgSxbdYq/F8mwLQ== adsantos@gmail.com
3: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDrCtzHdQ9g8MHj3bXenmDwd74YLYhdGHTmHBW1O6mGyYWdhwP7+EfsWap58rH5iwlH+Pwm1+9y7xajlOC2rnTTTpg1C/7+r4QHoFtzXLxkfXZxRjkRmNJMAD+N/NZ4ttPSlIxZWh53yUltt7escxDBRPTI00MIPnQQcah4jtsnLxANbbY6WKzqkjnZPY7SyBiZoj5yc+tFRcp9FhSJOVryLwySCta+UqLdrMCzXjSHY652WN+cu70j/l2/o4RgnQ+FlzMkFLGe2FTEmzuApRijHGdE3d6l5le1FTtlKji+fvCogFdl4jVN5NfNI/kFhJ7eRUZ7zu+iK6fO17pcSio7
```

## Interface

```bash
key-pair [COMMANDS] [OPTIONS]

COMMANDS:

[aws]

create-key-pair
    --key-name <value>
    [--dry-run | --no-dry-run]

delete-key-pair
    --key-name <value>
    [--dry-run | --no-dry-run]

describe-key-pairs
    [--filters <value>]
    [--key-names <value>]
    [--dry-run | --no-dry-run]

import-key-pair
    [--dry-run | --no-dry-run]
    --key-name <value>
    --public-key-material <value>

iam get-ssh-public-key
    --user-name <value>
    --ssh-public-key-id <value>
    --encoding <value>

iam delete-ssh-public-key
    --user-name <value>
    --ssh-public-key-id <value>

iam list-ssh-public-keys
    [--user-name <value>] - The name of the IAM user to list SSH public keys  for.  If  none  is specified,  the UserName field is determined implicitly based on the AWS access key used to sign the request.

iam update-ssh-public-key
    --user-name <value>
    --ssh-public-key-id <value>
    --status <value>

iam upload-ssh-public-key
    --user-name <value>
    --ssh-public-key-body <value>

generic

[gcp]

generic

[azure]

generic

[generic]

ssh-copy-id

ssh-keygen

ssh-keyscan
ssh-keyscan -H 192.168.1.162 >> ~/.ssh/known_hosts

OPTIONs:

--dry-run
```

# References

* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html)