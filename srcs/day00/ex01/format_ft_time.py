#!/usr/bin/env python3

import time 
import datetime
import sys

def format_time(input_time = None):
  
  if input_time is None:
      input_time = time.time()
      print(type(input_time))
      print(input_time)
  human_readable_time = datetime.datetime.fromtimestamp(input_time).strftime("%b %d %Y")

  scientific_notation = f"{input_time:.2e}"
  return input_time, human_readable_time, scientific_notation


def main(input = None):
    epoch_time, human_readable_time, scientific_notation = format_time(input)
    print(f"Second since January 1, 1970: {epoch_time:,.4f} or {scientific_notation} in scientific notation")
    print(f"{human_readable_time}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_value : float = 0
        try: 
            print(input_value)
            input_value = float(sys.argv[1])
        except:
            input_value = None
        main(input_value)

        
