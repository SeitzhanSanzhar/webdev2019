def swap_case(s):
    res = ""
    for x in s:
        if x.isupper() == True:
            res += x.lower()
        else:
            res += x.upper()
    return res

if __name__ == '__main__':