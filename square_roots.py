# Author: Bojan G. Kalicanin
# Date: 15-Oct-2016
# Newton's method for calculation of the square roots

def newton_root(a):
    epsilon = 0.0000001
    if a == 1:
        return 1
    else:
        x = a / 2
        while True:
            #print(x)
            y = (x + a/x) / 2
            if abs(y-x) < epsilon:
                break
            x = y
        return x
            

if __name__ == '__main__':
    a = newton_root(4)
    print("Square root of 4 is: " + str(a))
    b = newton_root(121)
    print("Square root of 121 is: " + str(b))
    c = newton_root(13)
    print("Square root of 13 is: " + str(c))