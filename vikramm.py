num=2520
ss=str(num)
if len(str(num))%2==0:
    fh=int(ss[len(ss)//2:])
    sh=int(ss[:len(ss)//2])
    if (fh+sh)**2==num:
        print('tech number')
    else:
        print('not tech number')
else:
    print('not tech number')

