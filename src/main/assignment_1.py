import numpy as np
from numpy.polynomial import Polynomial

# 1) Use double precision, calculate the resulting values (format to 5 decimal places)


def double_pres_to_decimal(val, chop=-1, rounding=False):
    s_str = val[0:1]
    c_str = val[1:12]
    m_str = val[12:]

    s = (-1)**int(s_str[0])

    c = 0
    for i in range(len(c_str)):
        c += int(c_str[i]) * 2**(len(c_str)-i-1)

    m = 0
    for i in range(len(m_str)):
        m += int(m_str[i]) * (1/2)**(i+1)

    res = (s) * (2**(c-1023)) * (1+m)

    dot = str(res).find(".")

    if rounding:
        res = float(round(res, chop-dot))

    if chop != -1:
        str_res_chopped = str(res).replace(".", "")[:chop]

        res = float(str_res_chopped[:dot] + "." + str_res_chopped[dot:])

    return res


def abs_error(xt, x):
    return abs(xt-x)


def rel_error(xt, x):
    return abs_error(xt, x) / abs(xt)


ans1 = double_pres_to_decimal(val="010000000111111010111001" +
                              "0000000000000000000000000000000000000000")
print("%.5f" % ans1, '\n')

ans2 = double_pres_to_decimal(val="010000000111111010111001" +
                              "0000000000000000000000000000000000000000", chop=3)
print("%.5f" % ans2, '\n')

ans3 = double_pres_to_decimal(
    val="010000000111111010111001", chop=3, rounding=True)
print("%.5f" % ans3, '\n')

ans4 = abs_error(ans1, ans3)
print(ans4)

ans5 = rel_error(ans1, ans3)
print(ans5, '\n')

# 5) What is the minimum number of terms needed to computer f(1) with error < 10-4?

k = 1
x = 1
while True:
    v = (-1)**k * (x**k/k**3)
    if abs(v) < 10**-4:
        break
    k += 1

print(k-1, '\n')

# 6) Determine the number of iterations necessary to solve f(x) = x3 + 4x2 – 10 = 0 with
# accuracy 10-4 using a = 4 and b = 7.


def fnc(x):
    return (x**3) + (4*(x**2)) - 10


def bisect(f, right, left, tol, mx):
    i = 0
    while (abs(right - left) > tol and i < mx):
        i += 1
        p = (left + right) / 2

        if (f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0):
            right = p
        else:
            left = p

    return i


def newton(p_prev, tol, mx, fnc: Polynomial):
    i = 0
    fnc_deriv = fnc.deriv()

    while i < mx:
        if fnc_deriv(p_prev) == 0:
            return -1

        p_next = p_prev - fnc(p_prev)/fnc_deriv(p_prev)
        if abs(p_next - p_prev) < tol:
            return i

        i += 1
        p_prev = p_next

    return i


print(bisect(fnc, 7, -4, 10**-4, 100))
print(newton(-4, 10**-4, 100, Polynomial([-10, 0, 4, 1])))

# b) Using the newton Raphson method
