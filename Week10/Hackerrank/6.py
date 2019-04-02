def mutate_string(string, position, character):
    s = list(string)
    s[position] = character
    res = ""
    for x in s:
        res += x
    return res

if __name__ == '__main__':