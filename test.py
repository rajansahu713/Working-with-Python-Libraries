li=[5,4,0,3,1,6,2]


def get_len(li, index_new, new_li = set()):
    len_set = len(new_li)
    while True:
        element = li[index_new]
        len_set = len(new_li)
        new_li.add(element)
        print(len(new_li), len_set)
        if len(new_li) == len_set:
            return len_set
        index_new=element
print(get_len(li, 0))
        
    