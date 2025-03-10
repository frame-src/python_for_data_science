#!/usr/bin/env python3
import sys

def main():
    
    try:
        assert 2 == len(sys.argv) 
        num = int(sys.argv[1])
     
        if num % 2 == 0: 
            print("I'm Even.")
        else:
            print("I'm Odd.")
    
    except ValueError as e: 
        print(f"ValueError: {e} the inserted argument is not an Int")

    except AssertionError as e:
        print(f"AssertionError: more than one argument is provide")
    
    except Exception as e:
        print(f"Unexpected error: {e}")



if __name__ == "__main__":
    main()
