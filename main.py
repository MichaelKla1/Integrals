import math

import sympy as sp
x = sp.symbols('x')

polinom = sp.sin(x) #function
start_point = 0
end_point = math.pi
n = 4 #number of sections

def trapezMethod(polinom,start_point,end_point,n):
    """
    Finds and returns the result of integral by trapez method
    :param polinom: function on which apply the integral
    :param start_point: star point
    :param end_point: end point
    :param n: number of section
    :return: the result of integral by trapez method
    """
    f = sp.lambdify(x, polinom)
    result = 0
    section_size = (end_point-start_point)/n
    i = 0
    while i < n:
        result += 0.5*(section_size)*(f(start_point)+f(start_point+section_size))
        print(str(i+1) + ": result = result + 0.5 * " + str(section_size) + " * (" + str(f(start_point)) + " + " + str(f(start_point+section_size)) + ") = " + str(result))
        start_point += section_size
        i += 1
    return result

def simpsonMethod(polinom,start_point,end_point,n):
    """
    Finds and returns the result of integral by simpson method
    :param polinom: function on which apply the integral
    :param start_point: star point
    :param end_point: end point
    :param n: number of section
    :return: the result of integral by simpson method
    """
    if n % 2 != 0:
        return "In simpson methon number of sections must be even"
    f = sp.lambdify(x, polinom)
    section_size = (end_point - start_point) / n
    i = 0
    result = f(start_point) #add first element
    print("result = " + str(result))
    start_point += section_size
    while i < n - 1:
        if i % 2 == 0:
            result += 4 * f(start_point)
            print(str(i + 1) + ": result = result + 4 * " + str(f(start_point)) + " = " + str(result))
        else:
            result += 2 * f(start_point)
            print(str(i + 1) + ": result = result + 2 * " + str(f(start_point)) + " = " + str(result))
        start_point += section_size
        i += 1
    result += f(end_point) #add last element
    print(str(i + 1) + ": result = result + " + str(f(end_point)) + " = " + str(result))
    result = (1/3)*section_size*result
    print("result = result * (1/3) * " + str(section_size) + " = " + str(result))
    return result

print("Integral by trapez method:")
print(trapezMethod(polinom,start_point,end_point,n))
print("Integral by simpson method:")
print(simpsonMethod(polinom,start_point,end_point,n))