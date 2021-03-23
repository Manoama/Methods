# 2*x^3 -4*x^2 - x + 2 = 0

def f(x):
    return 2*(x**3) - 4*(x**2) - x + 2

def df(x):
    return 6*(x**2) - 8*x - 1

def bisect_meth(a ,b ,e=0.001):
    if f(a)*f(b) < 0:
        i = 1
        while abs(a-b) > e:
            c = (a+b) / 2
            if f(c)*f(a) < 0:
                b = c
            elif f(c)*f(b) < 0:
                a = c
            print(f'№{i} f({c}) = {f(c)}             |{a} - {b}| < {e} - {"False" if abs(a-b) > e else "True"}')
            i+=1
        return (a+b) / 2
            

def hord_meth(a,b,e=0.001):
    if f(a)*f(b) < 0:
        c = a
        c_prev = 0
        i = 1
        while abs(c - c_prev) > e:
            c_prev = c

            num = a*f(b) - b*f(a)
            denum = f(b) - f(a)
            c = num / denum

            if f(c)*f(a) < 0:
                b = c
            elif f(c)*f(b) < 0:
                a = c
            print(f'№{i} f({c}) = {f(c)}             |{c} - {c_prev}| < {e} - {"False" if abs(c-c_prev) > e else "True"}')
            i+=1
        return c


def neuton_meth(x0,e=0.001):
    x = x0
    x_next = x0 - (f(x0)/df(x0)) 
    print(f'№{0} f({x}) = {f(x)}             |{x} - {x_next}| < {e} - {"False" if abs(x - x_next) > e else "True"}')
    i = 1
    while abs(x - x_next) > e:
        x = x_next
        x_next = x - (f(x)/df(x))
        print(f'№{i} f({x}) = {f(x)}             |{x} - {x_next}| < {e} - {"False" if abs(x - x_next) > e else "True"}')
        i+=1
    return x_next

def choose_method():
    print('1 - Bisection method')
    print('2 - Chord method')
    print('3 - Newton\'s method')

def choose_interval():
    print('1 - (-0.8, -0.4)')
    print('2 - (0.7, 1)')
    print('3 - (1.9, 2.2)')



def main():
    choose_method()
    choise = int(input('Choose method:'))
    if choise == 1:
        choose_interval()
        choise = int(input('Choose interval:'))
        if choise == 1:
            print(f'Result = {bisect_meth(-0.8,-0.4)}')
        elif choise == 2:
            print(f'Result = {bisect_meth(0.7, 1)}')
        elif choise == 3:
            print(f'Result = {bisect_meth(1.9,2.2)}')
        else:
            print("Wrong input")
    elif choise == 2:
        choose_interval()
        choise = int(input('Choose interval:'))
        if choise == 1:
            print(f'Result = {hord_meth(-0.8,-0.4)}')
        elif choise == 2:
            print(f'Result = {hord_meth(0.7, 1)}')
        elif choise == 3:
            print(f'Result = {hord_meth(1.9,2.2)}')
        else:
            print("Wrong input")
    elif choise == 3:
        choose_interval()
        choise = int(input('Choose interval:'))
        if choise == 1:
            print(f'1 - a = -0.8')
            print(f'2 - b = -0.4')
            choise = int(input('Choose initial approximation:'))
            if choise == 1:
                print(neuton_meth(-0.8))
            elif choise == 2:
                print(neuton_meth(-0.4))
            else:
                print('Wrong input')
        elif choise == 2:
            print(f'1 - a = 0.7')
            print(f'2 - b = 1')
            choise = int(input('Choose initial approximation:'))
            if choise == 1:
                print(neuton_meth(0.7))
            elif choise == 2:
                print(neuton_meth(1))
            else:
                print('Wrong input')
        elif choise == 3:
            print(f'1 - a = 1.9')
            print(f'2 - b = 2.2')
            choise = int(input('Choose initial approximation:'))
            if choise == 1:
                print(neuton_meth(1.9))
            elif choise == 2:
                print(neuton_meth(2.2))
            else:
                print('Wrong input')
    else:
        print('Wrong input')

if __name__ == "__main__":
    main()