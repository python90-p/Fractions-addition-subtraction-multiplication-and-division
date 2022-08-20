from fractions import Fraction

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

