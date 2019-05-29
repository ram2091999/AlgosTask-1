import collections

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac




def TwoNumberFinder(a):
    result=[]
    primeFactors=primes(a);
    counter=collections.Counter(primeFactors)
    if 5 in primeFactors:
        result.append(10)

    if 7 in primeFactors:
        result.append(7)
    if 43 in primeFactors:
        result.append(43)
    if 3 in primeFactors:
        result.append(9)
    if counter[2]==3 and not 5 in primeFactors:
        result.append(8)
    if counter[2]==4 and  5 in primeFactors:
        result.append(8)
    if counter[2]==4 and not 5 in primeFactors:
        result.append(16)
    if counter[2]==5 and  5 in primeFactors:
        result.append(16)
    if counter[2]==7 :
        result=[8,16]
    return result

def arrayextend(list1,list2):
    if len(list1)==2:
       if list1[0]==list2[0]:
         list1[0],list1[1]=list1[1],list1[0]
         list1.append(list2[1])
       elif list1[0]==list2[1]:
         list1[0],list1[1]=list1[1],list1[0]
         list1.append(list2[0])
       elif list1[1]==list2[0]:
         list1.append(list2[1])
       elif list1[1]==list2[1]:
         list1.append(list2[0])
    else:
       if list1[-1]==list2[0]:
         list1.append(list2[1])
       elif list1[-1]==list2[1]:
         list1.append(list2[0])
    return list1




def main():
    order=[]
    print("1 2")
    n1=int(input(">"))
    order.extend(TwoNumberFinder(n1))

    print("2 3")
    n2=int(input(">"))
    order=arrayextend(order,TwoNumberFinder(n2))

    print("3 4")
    n3=int(input(">"))
    order=arrayextend(order,TwoNumberFinder(n3))

    print("4 5")
    n4=int(input(">"))
    order=arrayextend(order,TwoNumberFinder(n4))
    if not 10 in order:
        order.append(10)
    if not 8 in order:
        order.append(8)
    if not 16 in order:
        order.append(16)
    if not 7 in order:
        order.append(7)
    if not 43 in order:
        order.append(43)
    if not 9 in order:
        order.append(9)
    print(order)

if __name__=="__main__":
     main()
