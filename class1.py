#WAP which will print sum of all the keys whos value are the factor of 12.
dt={1:2,2:3,3:4,6:12,17:18,18:12}
ans=0
for k,v in dt.items():
    if 12%v==0:
        ans+=k

print(ans)