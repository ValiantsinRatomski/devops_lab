ls = []
result = list()

cnt = int(input("Enter the number of commands: "))

for i in range(cnt):
    cmd = input("Enter " + str(i + 1) + " command:")
    if "insert" in cmd:
        cmd = cmd.split()
        pos = int(cmd[-2])
        value = int(cmd[-1])
        ls.insert(pos, value)
        continue
    elif "print" in cmd:
        curLs = []
        curLs = ls.copy()
        result.append(curLs)
        # print(result)
        continue
    elif "remove" in cmd:
        cmd = cmd.split()
        value = int(cmd[-1])
        ls.remove(value)
        # if value in ls:
        # 	del ls[cmd.index(value)]
        continue
    elif "append" in cmd:
        cmd = cmd.split()
        value = int(cmd[-1])
        ls.append(value)
        continue
    elif "sort" in cmd:
        ls.sort()
        continue
    elif "pop" in cmd:
        ls.pop()
        continue
    elif "reverse" in cmd:
        ls.reverse()
        continue

for x in result:
    print(x)
