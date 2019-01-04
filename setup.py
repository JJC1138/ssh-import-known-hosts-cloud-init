import setuptools

setuptools.setup(
    name = 'ssh-import-known-hosts-cloud-init',
    version = '1.0.0dev',
    packages = setuptools.find_packages(),
    entry_points = {'console_scripts': [
        'ssh-import-known-hosts-cloud-init = sshimportknownhostscloudinit.__main__:main',
    ]},
    install_requires = ['ruamel.yaml'],
)
