import random

def rangen(num,start,myrange):
    ranlst = []
    a = 0
    b = 0
    for i in range(num):
        a = random.randrange(start, myrange, 1)
        if a != b:
            ranlst.append(a)
            b = a
        else:
            a=random.randrange(start,myrange,1)
            ranlst.append(a)
            b = a
    return ranlst


def myview(a, num):
    b=[]
    c=[]                     #take a list A and create sublist of length num
    for i in a:              #b is a buffer
        b.append(i)
        if len(b) == num:
            c.append(b)
            b = []

    if b==[]:
        return c
    else:
        c.append(b)
        return c


def random_lst_gen(lst, num):   #generte  a non repeating random list
    copy = []
    for i in lst:
        copy.append(i)
    ran_lst = []
    for i in range(num):
        a=random.choice(copy)    #select a random element
        copy.remove(a)           #remove the element from the list
        ran_lst.append(a)
    return ran_lst