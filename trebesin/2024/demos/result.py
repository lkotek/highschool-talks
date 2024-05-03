#!/usr/bin/env python3

import requests
import sys

data = requests.get(sys.argv[1])
json_data = data.json()

print(json_data["result"]["overall"])
