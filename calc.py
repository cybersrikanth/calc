
def start_calc(a):
    lena=len(a)
    curlen=0
    d=''
    f=e=0
    opr='+'
    for i in a:
        curlen+=1
        try:
            b=int(i)
            c=str(b)
            d+=c
            e=int(d)
            if lena==curlen:
                try:
                    int(i)
                    f=calc(f,e,opr)
                    print(int(f))
                except ValueError:
                    print("Error Occured")
                
        except ValueError:
            f=calc(f,e,opr)
            if i== '+' or '-' or '*' or '/':
                opr=i
                d=''
                if f==0:
                    continue
            else:
                print("Error")

def calc(f,e,opr):
    if opr=='+':
        return(f+e)
    if opr=='-':
        return(f-e)
    if opr=='*':
        return(f*e)
    if opr=='/':
        return(f/e)


user_input=input("Enter the equation:")
start_calc(user_input)
