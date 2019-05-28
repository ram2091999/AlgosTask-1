def isPromoted(n,r,x,y,scn,contest):
    won=0
    for i in range(n):
        if scn[i]==1 and contest[i]==1:
            won=won+1
    if won*x -((n-won)*y)>0:
        print("Promoted")
    elif won*x -((n-won)*y)<0:
        print("demoted")
    else:
        print("No change")

def main():
    n,r,x,y=input("").split()
    c=input("").split()
    s=input("").split()
    contest=[int(i) for i in c]
    scn=[int(i) for i in s]
    isPromoted(int(n),int(r),int(x),int(y),scn,contest)

if __name__=="__main__":
     main()
