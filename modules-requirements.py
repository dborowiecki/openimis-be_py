import os
import json
import sys
import argparse

parser = argparse.ArgumentParser(description='Generate requirements from openIMIS json config.')
parser.add_argument('filename', metavar='N', type=str, nargs='?',
                    help='Relative directory of openimis.json')
parser.add_argument('-s', '--save', action='store_true', help='Save output to a file')

args = parser.parse_args()

sys.path.insert(0, './openIMIS/openIMIS')
from openimisconf import load_openimis_conf

conf_file_path = 'openimis.json'

if args.filename :
    conf_file_path = args.filename

if not conf_file_path:
    sys.exit("Missing config file path argument")
if not os.path.isfile(conf_file_path):
    sys.exit("Config file parameter refers to missing file %s" % conf_file_path)


def extract_requirement(module):
    return "%s" % module["pip"]

OPENIMIS_CONF = load_openimis_conf(conf_file_path)
MODULES = list(map(extract_requirement, OPENIMIS_CONF["modules"]))


if args.save:
    with open('modules-requirements.txt', 'w') as f:
        f.write('\n'.join(MODULES))
else:
    print('\n'.join(MODULES))