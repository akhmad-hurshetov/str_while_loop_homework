def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    a=""
    while i<len(s):
        if s[i].isalpha():
            a+=s[i]
        i+=1
    a=len(a)
    return a