def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    oddnum=""
    while i<len(s):
        if int(s[i])%2!=0:
            oddnum+=s[i]
        i+=1
    oddnum=len(oddnum)
    return int(oddnum)