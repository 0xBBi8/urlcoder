#!/usr/bin/env python3
import urllib.parse
import sys

def print_usage():
    print("Usage:")
    print("  urlencode.py -e 'text to encode'")
    print("  urlencode.py -d 'text to decode'")
    sys.exit(1)

if len(sys.argv) < 3:
    print_usage()

mode = sys.argv[1]
text = ' '.join(sys.argv[2:])

if mode == '-e':
    print(urllib.parse.quote(text))
elif mode == '-d':
    print(urllib.parse.unquote(text))
else:
    print("Error: Invalid flag. Use -e to encode or -d to decode.")
    print_usage()
