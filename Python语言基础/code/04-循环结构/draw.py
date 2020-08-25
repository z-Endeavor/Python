"""
打印各种三角形图案
*
**
***
****
*****
    *
   **
  ***
 ****
*****
    *
   ***
  *****
 *******
*********
"""

row = int(input("Input Row: "))

for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if row - j > i + 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
