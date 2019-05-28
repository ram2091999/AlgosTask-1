def printAverage(a,n):
    if(a[1:]=="0"*(n-1)||a=="1"*n):
      print("-1")
    else:
      b=int(a,2)
      print(bin(b-1)[2:]+" "+bin(b+1)[2:])


def main():
    n=int(input(""))
    a=input("")
    printAverage(a,n)

if __name__=="__main__":
    main()
    
