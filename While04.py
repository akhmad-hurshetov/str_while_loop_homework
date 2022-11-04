def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    upper=""
    while i<len(s):
        if s[i].isupper():
            upper+=s[i]
        i+=1
    upper=len(upper)
    return upper