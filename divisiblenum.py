# write a program which will print if the no. is divisible by both 3 and 5 from the no. 1 to 3

for i in range( 1,51):
    if( (i%5)==0):
        print ("fizz")
    elif(i%3)==0:
        print ("bizz")
    elif ((i%5)&(i%3))==0:
        print ("fizz & bizz")
    else :(i)