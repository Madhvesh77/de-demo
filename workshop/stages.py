from enum import IntEnum


class Stage(IntEnum):

    OLTP = 1

    WAREHOUSE = 2

    FULL_REFRESH = 3

    INCREMENTAL = 4

    AI_FAILURE = 5

    SEMANTIC_LAYER = 6

    CDC = 7