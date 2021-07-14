print(
    len(
        (
                [2] + list(
            filter(
                lambda x:
                (2 ** (x - 1)) % x == 1,
                range(
                    2,
                    int(
                        input()
                    ) + 1)
            )
        )
        )
    )
)
