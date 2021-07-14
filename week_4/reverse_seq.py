def seq_rev():
    n = int(input())
    if n != 0:
        seq_rev()
    print(n)


seq_rev()
