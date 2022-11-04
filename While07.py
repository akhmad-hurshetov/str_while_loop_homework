def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i=0
    evnum=""
    while i<len(s):
        if int(s[i])%2==0:
            evnum+=s[i]
        i+=1
    evnum=len(evnum)
    return int(evnum)