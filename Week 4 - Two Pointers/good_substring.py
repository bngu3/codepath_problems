def count_good_substrings(s):
    count = 0
    for i in range(len(s) - 2):
        window = s[i:i+3]
        window_set = set(window)
        if len(window_set) == 3:
            count += 1
    return count

    

s1 = "xyzzaz"
s2 = "xyzxyz"
print(count_good_substrings(s1))
print(count_good_substrings(s2))