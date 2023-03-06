"""Example function for unit tests"""

def sum(xs: list[float]) -> float:
    """return sum off all elements in xs"""
    sum_total: float = 0.0
    idx: int = 0

    for sum_total in xs:
        sum_total += xs[idx]
        idx += 1
        return sum_total