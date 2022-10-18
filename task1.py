from array import array


def func():
    a="hello"
    s=[]
    for i in a:
        if a.count(i)>1:
            if i not in s:
                s.append(i)
                print(s)
func() 