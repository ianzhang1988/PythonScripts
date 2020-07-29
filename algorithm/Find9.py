# 0-9 1
# 0-59 5
# 0-99 20

def find9_in_num(n):
    sum = 0
    while n>0:
        remainder=n%10
        if remainder == 9:
            sum += 1
        n=n//10
    return sum

def find9_brute(n):
    sum = 0
    for i in range(n+1):
        sum += find9_in_num(i)
    return sum

def find9(n):
    sum = 0
    num_in_list = []
    while n>0:
        remainder=n%10
        num_in_list.append(remainder)
        n=n//10

    # 每个进位上，有多少个9
    # helper_list[0] 无意义 helper_list[1] 十位前有多少9 helper_list[2] 百位前有多少9
    helper_list=[0 for _ in range(len(num_in_list))]

    for i in range(len(num_in_list)):
        if i == 0:
            helper_list[i] = 1

        # 1-8 * 前一位9的数量  9*** 不考虑***的变化有 10**3 个9 ***的变化有 helper_list[i-1] 再加上 上一个数位的变化
        helper_list[i]=8*helper_list[i-1]+10**i+helper_list[i-1]+helper_list[i-1]

    if num_in_list[0] == 9:
        sum+=1

    for i in range(1,len(num_in_list)):
        # print(num_in_list[i] , helper_list[i-1])

        # (1901 +1) (1911 + 11) (1991 +91 + 1)
        if num_in_list[i] == 9:
            idx = i-1
            addition = 0
            while idx > -1:
                addition+=num_in_list[idx]*10**idx
                if idx == 0:
                    addition += 1
                idx -= 1
            sum += num_in_list[i] * helper_list[i - 1] + addition
        else:
            sum+=num_in_list[i]*helper_list[i-1]

    return sum

if __name__ == '__main__':
    print(find9_in_num(190909))
    # for i in range(7):
    #     print(find9_brute(10**(i+1)))

    print(find9_brute(5360))
    print(5 * 300 + 3 * 20 + 6)
    print(find9(5360))

    for i in range(1,10000):
        val_1 = find9_brute(i)
        val_2 = find9(i)
        if val_1 != val_2:
            print('error', i, val_1, val_2, val_1 - val_2)