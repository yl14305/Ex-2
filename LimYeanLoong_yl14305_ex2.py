# Excercise 2
import math
import numpy as np
import matplotlib.pyplot as plt
##############################################################################
# Main menu


def Fresneler():
    MyInput = "0"
    while MyInput != "q":
        MyInput = input("Enter a choice, 'a', 'b', 'c', 'd' or 'q' to quit: ")
        print("You entered the choice: ", MyInput)
        if MyInput == "a":
            print("You have chosen part (a)")
            DeterminingA()
        elif MyInput == "b":
            print("You have chosen part (b)")
            DeterminingB()
        elif MyInput == "c":
            print("You have chosen part (c)")
            DeterminingC()
        elif MyInput == "d":
            print("You have chosen part (d)")
            DeterminingD()
        elif MyInput == "q":
            print("You have chosen to finish - goodbye.")
        else:
            print("Nonsense , your response is irrational")
##############################################################################
# Starting part(a)
# Part (A) guide Determining boundary condition > f(x), function > final


def DeterminingA():
    """"Initial step to determining the input is rational or irrational"""
    # do for lower limit & upper limit & name of the function
    # & number of times, N
    n = 0
    Upper_limit = np.pi
    Lower_limit = 0
    valid_n_input = False
    valid_overall_input = False
    while not valid_overall_input:
        while not valid_n_input:
            try:
                n = int(input("What is the number of interval "
                              "for integration?? "
                              "Only even number is acceptable. "
                              "Type in: "))
                if n == 0:
                    print("no zero you pimp, try again")
                    valid_n_input = False
                else:
                    valid_n_input = True
            except ValueError:
                print("Wrong input type of keys, only REAL"
                      "numerical values pls")
            except:
                print("Unknown error 404 , please try again")
        if (n % 2 == 0):
            valid_n_input = True
            valid_overall_input = True
            break
        else:
            print("please type even number only")
            valid_n_input = False
    Type_function(Upper_limit, Lower_limit, n)
# whole, number, 1,2,3,4,5, rather than with decimal places except :


def Type_function(Upper_limit, Lower_limit, n):
    """To determine what type of function to integrate over, giving
    other options, cosine, sine and tan"""
    valid_function_input = False
    Type_function = 0
    while not valid_function_input:
        Type_function = input("What is the type desired function"
                              ", 'sine', 'tan' or 'cosine': ")
        valid_function_input = True
        if (Type_function == 'sine' or Type_function == 'sin'):
            Function = math.sin
            break
        elif (Type_function == 'tan'):
            Function = math.tan
            break
        elif (Type_function == 'cosine' or Type_function == 'cos'):
            Function = math.cos
            break
        else:
            valid_function_input = False
            print("please choose from the list only")
    Simpson_1d(Upper_limit, Lower_limit, Function, n)


def Simpson_1d(Upper_limit, Lower_limit, Function, n):
    """method of numerical integration, which is usually use to approximate
    the area for, in this case it's 1 dimentional and
    using Simpson 1/3 rule"""
    f = Function
    Sum_of_odd = 0
    Sum_of_even = 0
    for i in range(0, n):
        h = (Upper_limit - Lower_limit) / n
        S = (f(Lower_limit) + f(Upper_limit))
        if i % 2 == 0:
            Sum_of_even += 2*f(Lower_limit + i*h)
        elif i % 2 != 0:
            Sum_of_odd += 4*f(Lower_limit + i*h)
        i += 1
    Integral = h/3 * (S + Sum_of_odd + Sum_of_even)
    print('Value of integral over 0 to pi: ', Integral)
##############################################################################
# Part(B)


def DeterminingB():
    """"Initial step to determining the input is rational or irrational"""
    # do for lower limit & upper limit & name of the function
    # & number of times, N
    n = 0
    Upper_limit = 0
    Lower_limit = 0
    z = 0
    x = 0
    k = 0
    valid_n_input = False
    valid_overall_input = False
    while not valid_overall_input:
        while not valid_n_input:
            try:
                n = int(input("What is the number of interval "
                              "for integration??"
                              " \nOnly even number is acceptable. "
                              "Type in: "))
                z = int(input("Acceptable range of z is above 10. "
                              "Type in desired value for z: "))
                if n == 0:  # Error for when user assign zero for n
                    print("no zero you pimp, try again")
                    valid_n_input = False
                else:
                    valid_n_input = True
            except ValueError:  # Error for when input is not numerical
                print("Wrong input type of keys, only REAL"
                      "numerical values pls")
            except:
                print("Unknown error 404 , please try again")
        if (n % 2 == 0):  # To determine if n is even number or else loop back
            valid_n_input = True
            valid_overall_input = True
            break
        else:
            print("please type even number only")
            valid_n_input = False
    plotshow(Upper_limit, Lower_limit, n, z, x, k)


def Simpson_2d(Upper_limit, Lower_limit, n, z, x, k):
    """method of numerical integration, which is usually use to approximate
    the area for, in this case it's 1 dimentional and
    using Simpson 1/3 rule"""
    F_X_a = np.exp((k*1j*((x - Lower_limit)**2)) / 2*z)
    F_X_b = np.exp((k*1j*((x - Upper_limit)**2)) / 2*z)
    Sum_of_odd = 0
    Sum_of_even = 0
    h = (Upper_limit - Lower_limit) / n
    S = (F_X_b + F_X_a)
    for i in range(0, n):
        if i % 2 == 0:
            Sum_of_even += 2 * np.exp((k*1j*((x-(Lower_limit + i*h))**2))/2*z)
        elif i % 2 != 0:
            Sum_of_odd += 4 * np.exp((k*1j*((x-(Lower_limit + i*h))**2))/2*z)
        i += 1
    Integral = h/3 * (S + Sum_of_odd + Sum_of_even)
    Integral2 = (abs(Integral))**2
    return Integral2


def plotshow(Upper_limit, Lower_limit, n, z, x, k):
    NumPoints = 200
    xmin = -0.1
    xmax = 0.1
    dx = (xmax - xmin) / (NumPoints - 1)  # i start counting from 0
    xvals = [0.0] * NumPoints
    yvals = np.zeros(NumPoints)
    for i in range(NumPoints):
        xvals[i] = xmin + i * dx
        yvals[i] = Simpson_2d(2e-6, -2e-6, n, z, xvals[i], 2*np.pi/(6e-7))
    plt.plot(xvals, yvals)
    plt.xlabel('|X(x)|^2', fontsize=16)
    plt.ylabel('x-axis of the screen', fontsize=16)
    plt.show()   # will look like a single slit diffraction
##############################################################################
# Part(c)


def DeterminingC():
    """"Initial step to determining the input is rational or irrational"""
    # do for lower limit & upper limit & name of the function
    # & number of times, N
    print("---------------------------------------------------------"
          "----------")
    print("---------------------------------------------------------"
          "----------")
    print("Note that for part(c), Upper and Lower limit of aperture had"
          " already been chosen as 1.5e-3 and 0.5e-3 respectively, wavelength "
          "of the laser is chosen as 6e-7.")
    n = 0
    Upper_limit = 0
    Lower_limit = 0
    z = 0
    x = 0
    k = 0
    valid_n_input = False
    valid_overall_input = False
    while not valid_overall_input:
        while not valid_n_input:
            try:
                n = int(input("For testing, it's recommended to use 20 to "
                              "generate the plot faster at 'low quality' "
                              "then use 100 for final once determined z."
                              "In addition , values lower than 20 are unclear"
                              "and slightly shifted from the centre."
                              "So what is the number of interval for"
                              " integration?? "
                              "Only even number is acceptable. "
                              "Type in: "))
                z = int(input("Range of valid values is z > 1. "
                              "Type in desired value for z: "))
                if n == 0:  # Error for when user assign zero for n
                    print("no zero you pimp, try again")
                    valid_n_input = False
                else:
                    valid_n_input = True
            except ValueError:  # Error for when input is not numerical
                print("Wrong input type of keys, only REAL"
                      "numerical values pls")
            except:
                print("Unknown error 404 , please try again")
        if (n % 2 == 0):  # To determine if n is even number or else loop back
            valid_n_input = True
            valid_overall_input = True
            break
        else:
            print("please type even number only")
            valid_n_input = False
    plotshow2(Upper_limit, Lower_limit, n, z, x, k)


def Simpson_x(Upper_limit_x, Lower_limit_x, n, z, x, k):
    F_x_a = np.exp((k*1j*((x - Lower_limit_x)**2))/2*z)
    F_x_b = np.exp((k*1j*((x - Upper_limit_x)**2))/2*z)
    Sum_of_odd_x = 0
    Sum_of_even_x = 0
    h_x = (Upper_limit_x - Lower_limit_x) / n
    S_x = (F_x_b + F_x_a)
    for i in range(0, n):
        if i % 2 == 0:
            Sum_of_even_x += 2 * np.exp((k*1j*((x-(Lower_limit_x + i*h_x))**2))/2*z)
        elif i % 2 != 0:
            Sum_of_odd_x += 4 * np.exp((k*1j*((x-(Lower_limit_x + i*h_x))**2))/2*z)
        i += 1
    Integral_x = h_x/3 * (S_x + Sum_of_odd_x + Sum_of_even_x)
    return Integral_x


def Simpson_y(Upper_limit_y, Lower_limit_y, n, z, y, k):
    E_o = 1
    factor = (k * E_o)/(2 * np.pi * z)
    F_y_a = np.exp((k*1j*((y - Lower_limit_y)**2))/2*z)
    F_y_b = np.exp((k*1j*((y - Upper_limit_y)**2))/2*z)
    Sum_of_odd_y = 0
    Sum_of_even_y = 0
    h_y = (Upper_limit_y - Lower_limit_y) / n
    S_y = (F_y_b + F_y_a)
    for i in range(0, n):
        if i % 2 == 0:
            Sum_of_even_y += 2 * np.exp((k*1j*((y-(Lower_limit_y + i*h_y))**2))/2*z)
        elif i % 2 != 0:
            Sum_of_odd_y += 4 * np.exp((k*1j*((y-(Lower_limit_y + i*h_y))**2))/2*z)
        i += 1
    Integral_y = h_y/3 * (S_y + Sum_of_odd_y + Sum_of_even_y)
    finalE = factor * Integral_y
    return finalE


def plotshow2(Upper_limit_y, Lower_limit_y, n, z, y, k):
    NumPoints = 200
    xmin = -1e-3
    xmax = 1e-3
    delta = (xmax-xmin) / (NumPoints - 1)
    intensity = np.zeros((NumPoints, NumPoints))
    for i in range(NumPoints):
        x = (i * delta)
        for j in range(NumPoints):
            y = (j * delta)
            c = 1
            eo = 1
            intensity[i, j] = eo * c * (abs(Simpson_x(1.5e-3, 0.5e-3, n, z, x, 2*np.pi/(6e-7)) * Simpson_y(1.5e-3, 0.5e-3, n, z, y, 2*np.pi/(6e-7))))**2
    plt.imshow(intensity)
    plt.title('Scattering pattern due to Fresnel diffraction '
              'from an aperture', fontsize=14)
    plt.xlabel('x-axis of the screen', fontsize=16)
    plt.ylabel('y-axis of the screen', fontsize=16)
    plt.show()
##############################################################################
# Part(d)
    

def DeterminingD():
    """"Initial step to determining the input is rational or irrational"""
    # do for lower limit & upper limit & name of the function
    # & number of times, N
    print("---------------------------------------------------------"
          "----------")
    print("---------------------------------------------------------"
          "----------")
    print("Note that for part(c), Upper and Lower limit of aperture had"
          " already been chosen as 1.5e-3 and 0.5e-3 respectively, wavelength "
          "of the laser is chosen as 6e-7.")
    n = 0
    Upper_limit = 0
    Lower_limit = 0
    z = 0
    x = 0
    k = 0
    valid_n_input = False
    valid_overall_input = False
    while not valid_overall_input:
        while not valid_n_input:
            try:
                n = int(input("For testing, it's recommended to use 20 to "
                              "generate the plot faster at 'low quality' "
                              "then use 100 for final once determined z."
                              "In addition , values lower than 20 are unclear"
                              "and slightly shifted from the centre."
                              "So what is the number of interval for"
                              " integration?? "
                              "Only even number is acceptable. "
                              "Type in: "))
                z = int(input("Range of valid values is z > 1. "
                              "Type in desired value for z: "))
                if n == 0:  # Error for when user assign zero for n
                    print("no zero you pimp, try again")
                    valid_n_input = False
                else:
                    valid_n_input = True
            except ValueError:  # Error for when input is not numerical
                print("Wrong input type of keys, only REAL"
                      "numerical values pls")
            except:
                print("Unknown error 404 , please try again")
        if (n % 2 == 0):  # To determine if n is even number or else loop back
            valid_n_input = True
            valid_overall_input = True
            break
        else:
            print("please type even number only")
            valid_n_input = False
    plotshow3(Upper_limit, Lower_limit, n, z, x, k)
  

# For circle, need to choose the limits of integration in such that it's
# the function of circle. where one of the axis represents as the subject.
def Lower_limit2_x(Upper_limit_y, Lower_limit_y):  # defining 1axis for circle
    return -np.sqrt(((Upper_limit_y)**2) - ((Lower_limit_y)**2))


def Upper_limit2_x(Upper_limit_y, Lower_limit_y):
    return np.sqrt(((Upper_limit_y)**2) - ((Lower_limit_y)**2))


def Simpson_2x(Upper_limit_y, Lower_limit_y, n, z, x, k):
    F_x_a = np.exp((k*1j*((x - Lower_limit2_x(Upper_limit_y, Lower_limit_y) )**2))/2*z)
    F_x_b = np.exp((k*1j*((x - Upper_limit2_x(Upper_limit_y, Lower_limit_y) )**2))/2*z)
    Sum_of_odd_x = 0
    Sum_of_even_x = 0
    h_x = (Upper_limit2_x(Upper_limit_y, Lower_limit_y) - Lower_limit2_x(Upper_limit_y, Lower_limit_y) ) / n
    S_x = (F_x_b + F_x_a)
    for i in range(0, n):
        if i % 2 == 0:
            Sum_of_even_x += 2 * np.exp((k*1j*((x-(Lower_limit2_x(Upper_limit_y, Lower_limit_y) + i*h_x))**2))/2*z)
        elif i % 2 != 0:
            Sum_of_odd_x += 4 * np.exp((k*1j*((x-(Lower_limit2_x(Upper_limit_y, Lower_limit_y) + i*h_x))**2))/2*z)
        i += 1
    Integral_x = (h_x)/3 * (S_x + Sum_of_odd_x + Sum_of_even_x)
    return Integral_x
# all the original limits in simpson_x must be replaced with the newly defined
# limits of the circle, however this does not apply to y-axis.

def Simpson_2y(Upper_limit_y, Lower_limit_y, n, z, y, k):
    E_o = 1
    factor = (k * E_o)/(2 * np.pi * z)
    F_y_a = np.exp((k*1j*((y - Lower_limit_y)**2))/2*z)
    F_y_b = np.exp((k*1j*((y - Upper_limit_y)**2))/2*z)
    Sum_of_odd_y = 0
    Sum_of_even_y = 0
    h_y = (Upper_limit_y - Lower_limit_y) / n
    S_y = (F_y_b + F_y_a)
    for i in range(0, n):
        if i % 2 == 0:
            Sum_of_even_y += 2 * np.exp((k*1j*((y-(Lower_limit_y + i*h_y))**2))/2*z)
        elif i % 2 != 0:
            Sum_of_odd_y += 4 * np.exp((k*1j*((y-(Lower_limit_y + i*h_y))**2))/2*z)
        i += 1
    Integral_y = h_y/3 * (S_y + Sum_of_odd_y + Sum_of_even_y)
    finalE = factor * Integral_y
    return finalE


def plotshow3(Upper_limit_y, Lower_limit_y, n, z, y, k):
    NumPoints = 200
    xmin = -1e-3
    xmax = 1e-3
    delta = (xmax-xmin) / (NumPoints - 1)
    intensity = np.zeros((NumPoints, NumPoints))
    for i in range(NumPoints):
        x = (i * delta)
        for j in range(NumPoints):
            y = (j * delta)
            c = 1
            eo = 1
            intensity[i, j] = eo * c * (abs(Simpson_2x(1.5e-3, 0.5e-3, n, z, x, 2*np.pi/(6e-7)) * (Simpson_2y(1.5e-3, 0.5e-3, n, z, y, 2*np.pi/(6e-7))))**2)
    plt.imshow(intensity)
    plt.xlabel('x-axis of the screen', fontsize=16)
    plt.ylabel('y-axis of the screen', fontsize=16)
    plt.show()

##############################################################################
Fresneler()  # This is used to run main menu.s
