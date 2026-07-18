def solution(N, number):
    dp = [set() for _ in range(9)]

    for seq in range(1, 9):
        added_set = set()
        added_set.add(int(str(N)*seq))

        for i in range(1, seq//2 + 1):
            set_1 = dp[i]
            set_2 = dp[seq-i]

            for value_1 in set_1:
                for value_2 in set_2:
                    added_set.add(value_1+value_2)

                    if (value_1-value_2) > 0:
                        added_set.add(value_1-value_2)

                    if (value_2-value_1) > 0:
                        added_set.add(value_2-value_1)

                    added_set.add(value_1*value_2)

                    if value_2 > 0 and value_1 > 0:
                        added_set.add(value_1//value_2)
                        added_set.add(value_2//value_1)

        dp[seq] = added_set

    for i, group in enumerate(dp):
        for j in group:
            if number == j:
                return i
            
    return -1