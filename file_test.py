import os
f = open("data.csv", "r", encoding="utf-8")
for line in f:
    print(line)
f.close()

f = open('data.csv', "a", encoding="utf-8")
f.write("2,3\n")
f.flush()
f.close()