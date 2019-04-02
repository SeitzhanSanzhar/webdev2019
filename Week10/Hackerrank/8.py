def split_and_join(line):
    # write your code here
    res = ""
    for x in line:
        if(x == ' ') :
            res += '-'
        else:
            res += x
    return res;
if __name__ == '__main__':