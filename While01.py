def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    a=""
    while i<len(s):
        if s[i].isdigit():
            a += s[i]
        i+=1
    a=len(a)
    return int(a)