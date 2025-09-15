
def custom_append(lst, item):
    #Add item at the end of the list.
    lst += [item]  # same as lst = lst + [item]
    return lst

def custom_insert(lst, index, item):
    #Insert item at a given index.
    if index < 0:
        index = 0
    if index > len(lst):
        index = len(lst)
    lst[:] = lst[:index] + [item] + lst[index:]
    return lst

def custom_pop(lst, index=-1):
    #Remove and return item at index.
    if not lst:
        raise IndexError("pop from empty list")
    if index < 0:
        index += len(lst)
    if index < 0 or index >= len(lst):
        raise IndexError("pop index out of range")
    item = lst[index]
    lst[:] = lst[:index] + lst[index+1:]
    return item

def custom_remove(lst, item):
    #Remove first instance of item.
    for i, val in enumerate(lst):
        if val == item:
            lst[:] = lst[:i] + lst[i+1:]
            return lst
    raise ValueError(f"{item} not in list")
