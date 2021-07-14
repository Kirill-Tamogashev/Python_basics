from itertools import accumulate
print(
    *accumulate(
        list(
            map(
                int,
                input().split())
        )
    )
)
