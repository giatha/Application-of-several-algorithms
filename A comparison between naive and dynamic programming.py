

def CanBeParsedFast(dict, str):
    if dict == {} or str == "":
        return None
    else:
        str1 = str.lower()
        a = list(dict)
        b = ' '.join(a)
        c = b.lower()
        dit = set(c.split(" "))
        t = [False]*(len(str1)+1)
        t[0] = True
        for i in range(0,len(str1)):
            if t[i] != True:
                continue
            for a in dit:
                n = len(a)
                end = i + n
                if end > len(str1):
                    continue
                if t[end] == True:
                    continue
                if str1[i:end] == a:
                    t[end] = True
        return t[len(str1)]




def CanBeParsedNaive(dict, str):
    if dict == {} or str == "":
        return None

    else:
        str1 = str.lower()
        a = list(dict)
        b = ' '.join(a)
        c = b.lower()
        dit = set(c.split(" "))
        lst = []
        for i in range(0,len(str1)+1):
            for j in range(i+1,len(str1)+1):
                if str1[j-i-1:j] in dit:
                        lst.append(list(range(j-i-1,j)))
    sort_lst = sorted(lst)
    lst2 = [sort_lst[0]]
    for i in range(0, len(sort_lst)):
        a = sort_lst[i]
        b = min(a)
        d = 0
        for l in range(0, len(lst2)):
            if b not in lst2[l]:
                lst2.append(lst2[l])
                lst2[l] = list(set().union(lst2[l], a))
                d += 1
        if d == 0:
            lst2.append(a)
    v = set(list(range(0,len(str1))))
    c = 0
    for i in range(0,len(lst2)):
        if set(lst2[i])== v:
            c += 1
    if c > 0:
        return True
    else:
        return False


