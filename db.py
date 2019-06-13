#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='choose db')
parser.add_argument('-d', '--db', help='target db(mysql/oracle/pq/sqlite)')
args = parser.parse_args()

if not args.db:
    parser.print_help()
    exit(0)

dbs = args.db.split('/')
with open('dbi/dbi.go', 'r') as f:
    dbi_lines = f.readlines()

found_lines = {}

lineIndex = -1
for line in dbi_lines:
    lineIndex += 1

    if '_' not in line:
        continue

    db_found = ''
    for db in dbs:
        if db in line:
            db_found = db
            break

    if db_found:
        if '//' in line:
            dbi_lines[lineIndex] = line.replace('// ', '', 1)
    else:
        if '//' not in line:
            dbi_lines[lineIndex] = line.replace('_', '// _', 1)

with open('dbi/dbi.go', 'w') as f:
    for line in dbi_lines:
        f.write(line)
