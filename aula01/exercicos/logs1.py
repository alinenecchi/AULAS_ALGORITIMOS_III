def processLogs(logs, threshold):
    x2 = logs
    y = set()
    for i in range(len(x2)):
        for j in range(len(x2[i])):
            count = 0
            for k in range(i + 1, len(x2)):
                for l in range(len(x2[k])):
                    print(x2[i][j], "compared to", x2[k][l])
                    if (x2[i][j] == x2[k][l]):
                        count += 1

                if (count >= threshold):
                    y.add(x2[i][j])

    z = list(y)
    z.sort()
    return z


test1 = [[1, 2, 4], [4, 0, 2], [4, 2, 8]]
print(processLogs(test1, 2))