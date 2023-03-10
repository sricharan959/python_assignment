def anagram_checker(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    if len(s1)!=len(s2):
        return False
    a1=sorted(s1)
    a2=sorted(s2)
    if a1==a2:return True
    else:return False
print(anagram_checker('the eyes','they see'))
# test cases
# part,trap
# Triangle,Integral
