import json
import os

def bar(get):
    with open(get, 'r') as file:
        try:
            if get:
              data = json.load(file)
              return data
            else:
                return []

        except json.JSONDecodeError:
            return []