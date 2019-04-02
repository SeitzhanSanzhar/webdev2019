if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    maxi = max(arr)
    while max(arr) == maxi:
        arr.remove(max(arr))
print max(arr)
