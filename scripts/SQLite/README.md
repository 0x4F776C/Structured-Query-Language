# SQLite exploit script

## DO NOT USE THIS SCRIPT AGAINST UNAUTHORISED SYSTEM(S)

## Guide

1. Install all required imports

``` bash
pip install -r requirements.txt
```

2. Execute script

``` bash
# Get help information
python3 SQLinjector.py -h
```

``` bash
# Test if site is vulnerable
python3 SQLinjector.py --argument 1
```

``` bash
# Get table name
python3 SQLinjector.py --argument 2
```

``` bash
# Get columns name
python3 SQLinjector.py --argument 3
```

``` bash
# Get numbers of columns in the specified database
python3 SQLinjector.py --argument 4
```

``` bash
# Get flag from column
python3 SQLinjector.py --argument 5
```
