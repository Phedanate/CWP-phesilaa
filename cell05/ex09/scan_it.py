#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    string = sys.argv[2]

    result = re.findall(keyword, string)

    if len(result) == 0:
        print("none")
    else:
        print(len(result))
