# dbb
dbb


```bash
➜  dbb git:(master) ✗ db.py -d pq/mysql/sqlite; go build; ./dbb
[mysql postgres sqlite3]
➜  dbb git:(master) ✗ db.py -d pq; go build; ./dbb
[postgres]
➜  dbb git:(master) ✗ db.py -d mysql/sqlite; go build; ./dbb
[mysql sqlite3]
➜  dbb git:(master) ✗ db.py -d sqlite; go build; ./dbb
[sqlite3]
```