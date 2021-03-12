n=int(input('Enter The number of lines:-'))
z=0
for i in range(n):
    ans=""
    for j in range(i+1):
        ans+=" "+chr(65+z)    #using ascii value of A <-65 here
        z+=1
    print(ans)
