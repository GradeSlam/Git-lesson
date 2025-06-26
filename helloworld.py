import math

def median(input):
  if len(input) % 2 == 0:
    top_middle = len(input) // 2
    bottom_middle = top_middle - 1
    return (input[bottom_middle] + input[top_middle]) / 2
  else:
    middle = len(input) // 2
    return input[middle]

my_list = [0, 1, 2, 3, 4, 5]
print(median(my_list))