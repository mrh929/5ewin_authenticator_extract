#!/usr/bin/python

import sqlite3
import argparse


def OpenDatabase(dbpath):
    conn = sqlite3.connect("file:%s?mode=ro" % dbpath, uri=True)

    c = conn.cursor()
    cursor = c.execute("SELECT DYNAMIC_TOKEN FROM USER_BEAN;")

    secret = []
    for row in cursor:
        secret.append(row[0])

    conn.close()

    if len(secret) == 0 or secret[0] == "":
        print("No secret is found.")
        print("Please check if your face verify passes.")
    elif len(secret) > 1:
        print("Some exception is found, please contact the developer if you have problems.")
    else:
        print("Your secret is: %s" % secret[0])
        print("TOTP link is %s" % ("otpauth://totp/5e?secret=%s" % secret[0]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Extract TOTP secret from fiveeDB.')
    parser.add_argument('dbpath', metavar='database', type=str,
                        help='path for the 5e database')

    args = parser.parse_args()
    OpenDatabase(args.dbpath)
