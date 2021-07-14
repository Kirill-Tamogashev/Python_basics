import itertools
print(
    0 in list(
        map(
            lambda r: int(
                r()
            ),
            itertools.repeat(
                input,
                int(input())
            )
        )
    )
)
