def is_long_pressed(name, typed):
    name_len = len(name)
    typed_len = len(typed)
    i = 0
    j = 0

    while j < typed_len: # loops until we complete all letters in name
        if i < name_len and name[i] == typed[j]: # makes sure i isn't greater than name
            i += 1
            j += 1
        elif j > 0 and typed[j] == typed[j - 1]:
            j += 1
        else:
            return False
    return i == name_len

name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))

