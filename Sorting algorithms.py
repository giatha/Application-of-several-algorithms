

def bubble(list_to_sort, ascend = True):
    if ascend == True:
        for i in range(0,len(list_to_sort)-1):
            for j in range(len(list_to_sort)-1,i,-1):
                if list_to_sort[j] < list_to_sort[j-1]:
                    exch = list_to_sort[j]
                    list_to_sort[j] = list_to_sort[j-1]
                    list_to_sort[j-1] = exch
    else:
        for i in range(0,len(list_to_sort)-1):
            for j in range(len(list_to_sort)-1,i,-1):
                if list_to_sort[j] > list_to_sort[j-1]:
                    exch = list_to_sort[j]
                    list_to_sort[j] = list_to_sort[j-1]
                    list_to_sort[j-1] = exch
    return list_to_sort

def insertion(list_to_sort, ascend = True):
    if ascend == True:
        for i in range(1,len(list_to_sort)):
            val = list_to_sort[i]
            j = i-1
            while j >= 0 and val < list_to_sort[j]:
                list_to_sort[j+1] = list_to_sort[j]
                j = j - 1
            list_to_sort[j+1] = val
    else:
        for i in range(1,len(list_to_sort)):
            val = list_to_sort[i]
            j = i-1
            while j >= 0 and val > list_to_sort[j]:
                list_to_sort[j+1] = list_to_sort[j]
                j = j - 1
            list_to_sort[j+1] = val
    return list_to_sort


def merge(list_to_sort,ascend = True):
    if len(list_to_sort) > 1:
        if ascend == True:
            mid = (len(list_to_sort)+1)//2
            l_list = list_to_sort[:mid]
            r_list = list_to_sort[mid:]

            merge(l_list,True)
            merge(r_list,True)

            i = 0
            j = 0
            p = 0

            while i < len(l_list) and j < len(r_list):
                if l_list[i] < r_list[j]:
                    list_to_sort[p] = l_list[i]
                    i +=  1
                else:
                    list_to_sort[p] = r_list[j]
                    j += 1
                p += 1

            while i < len(l_list):
                list_to_sort[p] = l_list[i]
                i += 1
                p += 1

            while j < len(r_list):
                list_to_sort[p] = r_list[j]
                j += 1
                p += 1
        else:
            mid = (len(list_to_sort) + 1) // 2
            l_list = list_to_sort[:mid]
            r_list = list_to_sort[mid:]

            merge(l_list, False)
            merge(r_list, False)

            i = 0
            j = 0
            p = 0

            while i < len(l_list) and j < len(r_list):
                if l_list[i] > r_list[j]:
                    list_to_sort[p] = l_list[i]
                    i += 1
                else:
                    list_to_sort[p] = r_list[j]
                    j += 1
                p += 1

            while i < len(l_list):
                list_to_sort[p] = l_list[i]
                i += 1
                p += 1

            while j < len(r_list):
                list_to_sort[p] = r_list[j]
                j += 1
                p += 1
    return list_to_sort
