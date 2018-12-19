# ddbopcu

## Install

```
$ mkdir test_dir && cd test_dir
$ echo '-e git+https://github.com/a4t/ddbopcu.git@v0.0.2#egg=ddbopcu' > requirements.txt
$ pip install -r requirements.txt
```

## Usage

```python
import yaml
from ddbopcu import opcu

tables = [
    'test-table1',
    'test-table2'
]

ddbopcu = opcu.Opcu(tables)
now_cu = ddbopcu.get_cu()

print(yaml.dump(now_cu, default_flow_style=False))
```

## Run

```
$ python main.py
common:
  record_end_time: '1545199694'
  record_start_time: '1545199693'
tables:
- GlobalSecondaryIndexes:
  - IndexName: foo
    ProvisionedThroughput:
      ReadCapacityUnits: 1
      WriteCapacityUnits: 2
  - IndexName: bar
    ProvisionedThroughput:
      ReadCapacityUnits: 1
      WriteCapacityUnits: 2
  ProvisionedThroughput:
    ReadCapacityUnits: 1
    WriteCapacityUnits: 2
  name: test-table1
- GlobalSecondaryIndexes:
  - IndexName: piyo
    ProvisionedThroughput:
      ReadCapacityUnits: 1
      WriteCapacityUnits: 2
  ProvisionedThroughput:
    ReadCapacityUnits: 1
    WriteCapacityUnits: 2
  name: test-table2
``` 

## Test

```
make test
```

## Format

```
make fmt
```
