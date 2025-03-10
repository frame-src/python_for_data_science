def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list) and family is None:
        return None
    col = len(family)
    row = len (family[0])
    print(f"My shape is: ({col},{row})")
    if end > len(family) or start > len(family):
        return None
    slice_obj = slice(start,end)
    family = family[slice_obj]
    col = len(family)
    row = len (family[0])
    print(f"My new shape is: ({col},{row})")
    return family