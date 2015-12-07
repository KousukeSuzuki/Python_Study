import math

def eulerpj_7() :
    """10001番目の素数を返す関数"""

    odr=6
    num=14 #6番目までは問題にあるため、7番目から探索を始める

    while odr<=10001:
        
        if (num%2)==0:
            num+=1
            continue
        if (num%3)==0:
            num+=1
            continue
        if (num%5)==0:
            num+=1
            continue

        mxdv=math.floor(math.sqrt(num))
        flg=True
        for i in range(7,mxdv+1):
            if (num%i)==0:
                flg=False #素数ならTrue, そうでなければFalse
                num+=1
                break
        if flg==True:
            odr+=1
            if odr==10001:
            	return num
        num+=1
