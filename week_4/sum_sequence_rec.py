def sum_seq(sum):
    num = int(input())
    if num == 0:
        return sum
    sum += num
    return sum_seq(sum)


print(sum_seq(0))
