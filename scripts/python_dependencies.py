#!/usr/bin/env python3

"""Utility to generate DEPEND data for ebuilds
"""

import distutils.core
import sys
import re

__author__ = "Anton Bolshakov"
__license__ = "GPL-3"
__email__ = "blshkv@pentoo.ch"

#FIXME: missing deps if platform_system is specified, see:
#dev-python/libsast

#TODO: https://github.com/uiri/toml
#def read_toml
#msoffcrypto-tool-4.12.0
#or? >>> import pep517.meta
#>>> import pprint

def portage_mapping(search):
    mapping =  {
        "dev-python/androguard": "dev-util/androguard",
        "dev-python/bs4": "dev-python/beautifulsoup:4",
        "dev-python/Django": "dev-python/django",
        "dev-python/frida": "dev-python/frida-python",
        "dev-python/lief": "dev-util/lief",
        "dev-python/prompt-toolkit": "dev-python/prompt_toolkit",
        "dev-python/pycrypto": "dev-python/pycryptodome",
        "dev-python/pyOpenSSL": "dev-python/pyopenssl",
        "dev-python/pypykatz": "app-exploits/pypykatz",
        "dev-python/ruamel.yaml": "dev-python/ruamel-yaml",
        "dev-python/tls-parser": "dev-python/tls_parser",
        "dev-python/capstone": "dev-libs/capstone[python]",
        "dev-python/unicorn": "dev-util/unicorn[python]",
        "dev-python/colored_traceback": "dev-python/colored-traceback",
        "dev-python/pycryptodomedomex": "dev-python/pycryptodome",
        "dev-python/Flask": "dev-python/flask",
        "dev-python/flask-Login": "dev-python/flask-login",
        "dev-python/flask-Mail": "dev-python/flask-mail",
        "dev-python/flask-Principal": "dev-python/flask-principal",
        "dev-python/flask-WTF": "dev-python/flask-wtf",
        "dev-python/flask-BabelEx": "dev-python/flask-babelex",
        "dev-python/scapy": "net-analyzer/scapy",
        "dev-python/PyYAML": "dev-python/pyyaml",
        "dev-python/redis": "dev-python/redis-py",

        "dev-python/ropgadget": "app-exploits/ROPgadget",
        "dev-python/pysocks": "dev-python/PySocks",
    }

    for key in mapping:
        search = search.replace(key, mapping[key])
    return search

def main():
    # setup.py can be generated by flit for pyproject.toml projects as a workaround
    setup = distutils.core.run_setup("./setup.py")

    if not hasattr(setup, 'install_requires') or len(setup.install_requires)==0:
        print("RDEPEND=\"\"")
        sys.exit(1)
    #Debug:
    #print(setup.install_requires)

    print("RDEPEND=\"")

    for i in setup.install_requires:
        #match: my-na.me<5.0.0,>=4.0.0
        #and match: my-na.me
        pattern = '([-.\w]+)(>=|>|==|=<|<)?([\d.]+)?(,)?(>=|>|==|=<|<)?([\d.]+)?'
        match = re.search(pattern, i)
#        if match:
#          print("Match:", match.group(1), match.group(2), match.group(3), match.group(4), match.group(5), match.group(6))
#          print("Match0:", match.group(0) )
#        else:
#          print("pattern not found")
        if match.group(2) == ">=" or match.group(2) == "==":
          print("\t>="+portage_mapping("dev-python/"+match.group(1))+"-"+ match.group(3)+"[${PYTHON_USEDEP}]")
        elif match.group(5) == ">=" or match.group(5) == "==":
          print("\t>="+portage_mapping("dev-python/"+match.group(1))+"-"+ match.group(6)+"[${PYTHON_USEDEP}]")
        elif match.group(1):
          print("\t"+portage_mapping("dev-python/"+match.group(1)+"[${PYTHON_USEDEP}]"))
        else:
          print("Error: fail to detect dependency name")
          sys.exit(1)

    print("\"")

if __name__ == '__main__':
    main()
