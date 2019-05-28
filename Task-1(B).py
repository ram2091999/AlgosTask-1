def divide(a):
    if(len(a)==1):
      return 0
    else:
      if(a[:(len(a)/2)]==a[(len(a)/2):]):
       return 1+divide(a[:len(a)/2])
      else:
       return 0


def main():
    n=int(input(""))
    a=input("")
    print(divide(a))

if __name__=="__main__":
    main()

       
