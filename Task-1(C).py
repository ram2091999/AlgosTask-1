import collections

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
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
    if(counter[2]==3):
        result.append(8)
    if(counter[2]==4):
        result.append(16)
    if(counter[2]==7)
        result=[8,16]
    return result

def arrayextend(list1,list2):
    if len(list1)==2:
       if list1[0]==list2[0]:
         list1[0],list1[1]=list1[1],list[0]
         list1.append(list2[1])
       elif list1[0]==list2[1]:
         list1[0],list1[1]=list1[1],list[0]
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
