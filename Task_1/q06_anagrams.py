def anagrams(str1,str2):
    str1 = str1.replace(" ","")
    s1 = str1.lower()
    str2 = str2.replace(" ","")
    s2 = str2.lower()

    if len(s1) != len(s2):
        return False

    s1=sorted(s1)
    s2=sorted(s2)

    if s1 == s2:
        return True
    else:
        return False

print(anagrams("listen","silent"))
    
