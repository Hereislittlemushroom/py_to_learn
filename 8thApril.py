def funcname(*x,n):
    g1=[n for i in x if i<n]
    g2=[n for i in x if i>n]
    return g1+g2

