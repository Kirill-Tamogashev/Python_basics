print(
    *map(
        lambda y: int(
            sum(y) % 2 != 0
        ),
        zip(
            *map(
                lambda x: map(
                    int, input().split()
                ),
                range(
                    int(
                        input()
                    )
                )
            )
        )
    )
)
