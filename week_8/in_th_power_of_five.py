from functools import reduce
print(
    reduce(
        lambda x, y: x * y,
        list(
            map(
                lambda x: x ** 5,
                list(
                    map(
                        int,
                        input().split())
                )
            )
        )
    )
)

