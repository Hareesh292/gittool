num=2025
dup=num
if len(str(num))%2==0:
    fh=num//100
    sh=num%100
    if (fh+sh)**2==num:
        print('tech number')
    else:
        print('not tech number')
else:
    print('not tech number')
#to check the given number is emirp number or not
num=20
dup=num
res=0
while num!=0:
    rem=num%10
    res=res*10+rem
    num//=10
if res!=dup:
    if dup>1:
        for val in range(2,dup//2+1):
            if dup%val==0:
                print('not emirp number')
                break
        else:
            if res>1:
                for val in range(2,res//2+1):
                    if res%val==0:
                        print(' not emirp number')
                        break
                else:
                    print('emirp number')
            else:
                print('not emirp number')
    else:
        print('not emirp number')
else:
    print ('not emirp number')
#To check the given number is spy number or not
num=1234
ss=0
mm=1
while num!=0:
    rem=num%10
    ss+=rem
    mm*=rem
    num//=10
if ss==mm:
    print('spy number')
else:
    print('not spy number')
#to check the given number is perfect squre or not
num=16
val=1
while val*val<=num:
    if val*val==num:
        print('perfect squre')
        break
    val+=1
else:
    print('not perfcet squre')
#to check the given number is lcm
a=4
b=12
if a>b:
    lcm=a
else:
    lcm=b
while True:
    if lcm%a==0 and lcm%b==0:
        print(lcm)
        break
    lcm+=1
#to check the give given number is gcd number or not
a=10
b=26
if a>b:
    gcd=b
else:
    gcd=a
while True:
    if a%gcd==0 and b%gcd==0:
        print(gcd)
        break
    gcd-=1
#to find out the given number is a happy number or not
num=13
res=0
if num>9:
    while num!=0:
        rem=num%10
        res=res+rem**2
        num//=10
    res=num
else:
    if num==1 or num==7:
        print('happy number')
    else:
        print('not happy number')



    
