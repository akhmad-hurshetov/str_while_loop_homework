def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    oddsum=0
    while i<len(s):
        if int(s[i])%2!=0:
            oddsum+=int(s[i])
        i+=1
    return oddsum