import math

print('To exit type "-1"')
print('Enter your grade as a float or integer:')

i = 1

while i != -1:
  i = float(input("Enter your grade %: "))
  grade_4 = 0
  if i < 65:
    grade_4 = 0.0
  elif i < 66:
    grade_4 = 1.0
  elif i <= 95:
    grade_4 = 1.0 + math.ceil(i - 66) / 10.0
  else:
    grade_4 = 4.0
  print('Your grade is %.1f' % grade_4)