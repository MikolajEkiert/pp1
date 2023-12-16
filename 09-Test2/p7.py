import re
def f(arr):
    valid_usernames = 0
    for word in arr:
        if re.match("^[a-z0-9_]{4,12}$", word):
            valid_usernames += 1
    return valid_usernames
print(f(["uek", "water_7_x", "anna.may", "a_b_c_d_e_f"]))

