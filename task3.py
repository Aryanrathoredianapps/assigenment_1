
l=[]
def convert_list(s):
        if len(s)>1:
                l.append(s[0])
                convert_list(s[1])
        else:
                l.append(s[0])
s=[1,[2,[3,[4,[5,[6,[7]]]]]]]
convert_list(s)
print(l)








