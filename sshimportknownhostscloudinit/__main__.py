import argparse
import sys

import ruamel.yaml

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--hostname', default=None, help="The hostname to use for the new key entries in the known_hosts file. If not given explictly then the hostname given in the config file's 'fqdn' or 'hostname' properties is used.")
    arg_parser.add_argument('config_file_name', metavar='config-file-name', help="The path to a cloud-init config file to read the SSH host keys from.")
    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = arg_parser.parse_args()
    
    with open(args.config_file_name, 'rb') as config_file:
        config = ruamel.yaml.YAML(typ='safe').load(config_file)
    
    if not args.hostname:
        args.hostname = config.get('fqdn') or config.get('hostname')
        if not args.hostname:
            raise Exception("No hostname was found in the config file and none was given explicitly using the --hostname option")
