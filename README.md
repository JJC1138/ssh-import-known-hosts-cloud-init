# ssh-import-known-hosts-cloud-init

This tool imports public SSH host keys from a [cloud-init](https://cloud-init.io/) config file into your `~/.ssh/known_hosts` file. This allows you to connect to a cloud-init-configured instance securely with SSH without having to manually verify the host's keys.

It can be used with the companion tool [generate-cloud-init-ssh-host-keys](https://github.com/JJC1138/generate-cloud-init-ssh-host-keys) if you need to also generate the host keys and add them to the cloud-init config file first.

## Usage

Call the program with the path to your cloud-init config file:

```
ssh-import-known-hosts-cloud-init my-cloud-init.yaml
```

The keys are added to your `~/.ssh/known_hosts` file. The hostname to use for the `known_hosts` entries is taken from the [`fqdn` or `hostname`](https://cloudinit.readthedocs.io/en/latest/topics/modules.html#set-hostname) properties specified in the config file, or can be explicitly given using the `--hostname` option:

```
ssh-import-known-hosts-cloud-init --hostname ec2-foo.eu-west-2.compute.amazonaws.com my-cloud-init.yaml
```
