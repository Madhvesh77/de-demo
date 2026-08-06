from enum import IntEnum


class Stage(IntEnum):

    OLTP = 1
    WAREHOUSE = 2
    FULL_REFRESH = 3
    INCREMENTAL = 4
    AI = 5
    CDC = 6

    def __str__(self):

        return self.name.replace("_", " ").title()