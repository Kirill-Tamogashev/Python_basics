from math import sqrt

print(
     *filter(
            lambda x: all(
                map(
                    lambda y: x % y or y == x,
                    range(
                        2,
                        round(
                            sqrt(x)) + 1
                    )
                )
            ),
            range(
                2,
                int(input()) + 1
            )
     )

)
