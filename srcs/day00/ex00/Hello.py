#!/usr/bin/env python3

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


def mod_list(l:list):
    ''' Lists: 
            - are used to store multiple items in a single variable. 
            - List's items are ordered, CHANGEABLE, and allow duplicate values.  
            - List's items are indexed, 
                the first item has index [0], 
                the second item has index [1]
                ecc... [len-1]      
    '''
    try :
        l[1] = "World!"
    except:
        return None
    return l


def mod_tuple(t:tuple):
    ''' Tuples:
            - are used to store multiple items in a single variable.
            - Tuple's items are ordered, UNCHANGEABLE, and allow duplicate values.
            - Tuple's items are indexed,
                the first item has index [0], 
                the second item has index [1]
                ecc... [len-1]
    '''
    tmp = []
    try:
        tmp = list(t)
        tmp[1] = "Germany!"
    except:
        return None
    new_tuple = tuple(tmp)
    return new_tuple

def mod_set(s:set):
    ''' Sets:
            - are used to store multiple items in a single variable.
            - Set's items are unordered, UNCHANGEABLE, and unindexed.
            - Set's items are unchangeable but:
                you can add new items, 
                you can remove items.
            - Sets do not allow duplicate values.
        NOTE: Sets are unordered, so:
            - you cannot be sure in which order the items will appear.
    '''
    new_set = {}
    try: 
        new_set = { "Heilbronn!","tutu!"}
        new_set ^= s
        s =  new_set
    except:
        return None
    return new_set


def mod_dict(d:dict):
    ''' Dict:
            - are used to store data values in KEY:VALUE pairs.
            - Dict's items are ordered, CHANGEABLE, and do not allow duplicates.
            - Dict's items can be referred to by using the key name.
    '''
    try: 
        d["Hello"] = "42Heilbronn!"
    except:
        return None
    return d

ft_list = mod_list(ft_list)
ft_tuple = mod_tuple(ft_tuple)
ft_set = mod_set(ft_set)
ft_dict = mod_dict(ft_dict)

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
