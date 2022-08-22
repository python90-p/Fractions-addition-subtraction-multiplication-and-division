#We first import the fraction module to write fractions . The code inside this module is :

#the code has a variable set for numerator and denominator and divides them and writes in a new line with a dash in middle 
# this is the code inside the module set in a class.

from fractions import Fraction

#This while loop means that the interface asks for numerator and denominator until the user exits it.
i = 1
while i<=5:
#The below code asks the input and enters all the basic functions answers.

    en = int(input('Enter Numerator of first fraction: '))
    sn = int(input('Enter denominator of first fraction: '))

    ff = Fraction(en, sn)

    print('  ')

    rn = int(input('Enter Numerator of second fraction: '))
    qn = int(input('Enter denominator of second fraction: '))

    sf = Fraction(rn, qn)

    print('  ')

    sumf = ff+sf
    print('Sum of the two fractions is: ')
    print(sumf)

    print('  ')

    subf = ff-sf
    print('Difference of the two fractions is:')
    print(subf)

    print('  ')

    mulf = ff*sf
    print('The product of the two fractions is:')
    print(mulf)

    print('  ')

    divf = ff/sf
    print('The quotient of the two fractions is:')
    print(divf)

