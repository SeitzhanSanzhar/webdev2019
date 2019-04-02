n = int(raw_input())

s = list()
for i in range(n): s.append([raw_input(), float(raw_input())])

best_2 = set([s[x][1] for x in range(n)])
best_2 = list(best_2)
best_2.sort()

s = [x[0] for x in s if x[1] == best_2[1]]
s.sort()

for s in s:
    print s
