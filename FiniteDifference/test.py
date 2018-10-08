def f(x1,x2,x3):
    return x1+x2+x3



def df(funct,wrt=(0,)):
    def derivatives(*list):
        result = []
        for idx in wrt:
            head, interst, tail = list[0:idx],list[idx],list[idx+1:]
            newList=head+(interst,)+tail
            result.append(funct(*newList))
        return result
    return derivatives

dfff = df(f,wrt=(0,))

print(dfff(3.0,7.0,1.0))