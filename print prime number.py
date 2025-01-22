""" PRINT THE GIVEN NUMBER IS PRIME OR NOT """
# input a number by user
num=int(input(" enetr a number"))
i=2
if num>1:
    while i<num:
        if num%i==0:
            print("not prime number")
            break
        i=i+1

    else:
        print("number is prime")


else:
    print("error")        