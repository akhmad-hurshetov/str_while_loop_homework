def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    n=len(s)
    i=0
    count=0
    s=s.lower()
    while i<n:
        x = s[i]
        if not(x=='a' or x=='e' or x=='i' or x=='o' or x== 'u') and x.isalpha():
            count+=1
        i+=1
    return count
print(main('helloworld! @'))



'''
def main(s):
    n=len(s)
    i=0
    count=0
    s=s.lower()
    vowels='aeiou'
    while i<n:
        x=s[i]
        if vowels.find(x)==-1:
            count+=1
        i+=1
    return count
print(main('absec'))
'''