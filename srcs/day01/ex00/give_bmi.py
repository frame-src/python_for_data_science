def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    #your code here
    if height is None or weight is None: 
        return None
    if len(height)!= len(weight):
        return None
    bmi = []
    for val_h, val_w in zip(height,weight):
        bmi.append( val_w / (val_h * val_h))
    return bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if bmi is None:
        return None
    check = []
    for value in bmi:
        if value > limit:
            check.append(True)
        else :
            check.append(False)
    return check