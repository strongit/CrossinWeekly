def function(n):
    if ((n%1 > 0) or (n < 5) or (n > 54)):
        return False
    n = int(n)
    num = []
    for i in range(1,n//2):
        for j in range(n//2-i):
            num.append(int(str(int(i))+str(int(j))+str(int((n//2-i-j)))*(int(2/(n%2+1)))+str(int(j))+str(int(i))))
    return num

if __name__ == "__main__":
    num = function(float(input()))
    try:
        num.sort()
        for x in num:
            print (x)
    except:
        print ("Invalid number.")
