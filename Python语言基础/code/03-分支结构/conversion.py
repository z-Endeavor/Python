"""
英制单位英寸和公制单位厘米互换
"""

value = float(input("Input Length: "))
unit = input("Input Unit: ")
if unit == 'in':
    print('%.1f in = %.1f cm' % (value, value * 2.54))
elif unit == 'cm':
    print('%.1f cm = %.1f in' % (value, value / 2.54))
else:
    print("Invaild Unit!")
