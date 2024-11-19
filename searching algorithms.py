
def seq_search(mylist, target):
    i=0
    length=len(mylist)
    while i< length:
        if mylist[i] == target:
            return True
        else:
            i+=1
    return False


def fast_seq_search(mylist, target):
    i=0
    length=len(mylist)
    mylist.append(target)
    while mylist[i] != target:
        i+=1
    if i == length:
        return False
    return True

def binary_search(mylist, first, last, target):
    if mylist[first] <= mylist[last]:
        middle=first+last//2
        if mylist[middle] == target:
            return True
        elif mylist[middle] > target:
            return binary_search(mylist, first, middle-1, target)
        else :
            return binary_search(mylist, middle+1, last, target)
    else:
        return False

def self_org_search1(mylist, target):   # move to first method
    rng=range(len(mylist))
    for item in mylist:
        if item == target:
            mylist.remove(target)
            mylist.insert(0,target)
            return True
    return False
    
def self_org_search2(mylist, target):   # transpose method
    for item in mylist:
        if item == target:
            index=mylist.index(item)
            mylist[index]=mylist[index-1]
            mylist[index-1]=target
            return True
    return False
    
def BS_tree():
    pass #needs pointers and nodes

def AVL_tree():
    pass #needs pointers and nodes




my_list=[12,36,45,87,47,69,81,34]
print(seq_search(my_list,47))
print(fast_seq_search(my_list,47))
print(binary_search(my_list,0,len(my_list)-1,47))
print(self_org_search1(my_list,47))
print(self_org_search2(my_list,47))



