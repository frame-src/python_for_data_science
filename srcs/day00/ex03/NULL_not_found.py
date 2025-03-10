#!/usr/bin/env python3

def NULL_not_found(object: any) -> int:
    if object and object == object:
        print("Type not Found")
        return 1
    try:
        print(f"None obj: {object} {type(object)}")
    except: 
        return 1
    return 0

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
