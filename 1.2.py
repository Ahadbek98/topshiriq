R1=float(input("R1="))
R2=float(input("R2="))
R3=float(input("R3="))
if(R1>0 and R2>0 and R3>0):
    R=pow((1/R1+1/R2+1/R3),-1)
    print("R=",R)