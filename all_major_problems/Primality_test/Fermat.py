import random
import math
def Fermat_primality(Num):
    if Num ==1 and Num ==4:
        return False
    if Num ==2 and Num ==3:
        return True
    for i in range(5):
        a= random.randint(2, Num - 2)
        mod= a**(Num-1) % Num
        if mod !=1 :
            return False 
    return True

if __name__=="__main__":
    if(Fermat_primality(561)):
        print("The number is prime.")
    else:
        print("Composite number")