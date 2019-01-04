import argparse
import os.path
import re
import sys

import ruamel.yaml

def log(message):
    print(message, file=sys.stderr)

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
            raise Exception("No hostname was found in the config file and none was given explicitly using the --hostname option.")
    
    keys = config.get('ssh_keys')
    
    if not keys:
        raise Exception("No 'ssh_keys' section was found in the config file.")
    
    public_key_type_pattern = re.compile('^(?P<key_type>.*?)_public$')
    
    with open(os.path.expanduser('~/.ssh/known_hosts'), 'at') as known_hosts_file:
        for full_key_type in keys.keys():
            match = public_key_type_pattern.match(full_key_type)
            if not match:
                continue
            
            key_type = match.group('key_type')
            
            key = keys[full_key_type]
            
            known_hosts_key_line = '%s %s' % (args.hostname, key)
            
            known_hosts_file.write(known_hosts_key_line)
            
            log("Imported %s key" % key_type)
