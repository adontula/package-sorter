import subprocess
from package_sort.sort import sort

# subprocess.run("python -m pytest -v test_sort.py".split(" "))

while True:
  print("Please enter the width(cm), length(cm), height(cm), and mass(kg) of the package you wish to sort, separated by spaces. Enter \"exit\" to exit:")
  try:
    package_dims = input().strip().split(" ")
    if len(package_dims) > 0 and package_dims[0] == "exit":
      break
    if len(package_dims) != 4:
      raise ValueError
    width = float(package_dims[0])
    length = float(package_dims[1])
    height = float(package_dims[2])
    mass = float(package_dims[3])

    print("\nPackage is in category: " + sort(width, length, height, mass) + "\n")
  except ValueError as e:
    print("Invalid input. Please enter positive numbers for width, length, height and mass separated by spaces.\n")