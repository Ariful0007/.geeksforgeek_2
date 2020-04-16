def check(x):
    dec=0
    i=1
    while x !=0 :
        rem=x % 2
        x=x//2
        dec=dec+rem*i
        i*=10
    return  dec





for _ in range(int(input())):
    n = int(input())
    print(check(n))

if __name__ == '__main__':
    pass

