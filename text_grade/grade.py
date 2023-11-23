from enum import StrEnum


class Grade(StrEnum):
    VERY_EASY: str = "very easy"
    EASY: str = "easy"
    FAIRLY_DIFFICULT: str = "fairly difficult"
    VERY_DIFFICULT: str = "very difficult"
    UNKNOWN: str = "unknown"
