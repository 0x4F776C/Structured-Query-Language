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

![help](https://github.com/0x4F776C/Structured-Query-Language/blob/main/scripts/SQLite/img/help.png)

``` bash
# Test if site is vulnerable
python3 SQLinjector.py --argument 1
```

![one](https://github.com/0x4F776C/Structured-Query-Language/blob/main/scripts/SQLite/img/one.png)

``` bash
# Get table name
python3 SQLinjector.py --argument 2
```

![two](https://github.com/0x4F776C/Structured-Query-Language/blob/main/scripts/SQLite/img/two.png)

``` bash
# Get columns name
python3 SQLinjector.py --argument 3
```

![three](https://github.com/0x4F776C/Structured-Query-Language/blob/main/scripts/SQLite/img/three.png)

``` bash
# Get numbers of columns in the specified database
python3 SQLinjector.py --argument 4
```

![four](https://github.com/0x4F776C/Structured-Query-Language/blob/main/scripts/SQLite/img/four.png)

``` bash
# Get flag from column
python3 SQLinjector.py --argument 5
```

![five](https://github.com/0x4F776C/Structured-Query-Language/blob/main/scripts/SQLite/img/five.png)
