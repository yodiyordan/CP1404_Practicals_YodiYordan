name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

print("My guitar: " + name + ", first made in " + str(year))

print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

print("My {} would cost ${:,.2f}".format(name, cost))

numbers = [1, 19, 123, 456, -25]
for i in range(len(numbers)):
    print("Number {0} is {1:>5}".format(i + 1, numbers[i]))

for i, number in enumerate(numbers):
    print("Number {0} is {1:>5}".format(i + 1, number))

for number in range(0, 101, 50):
    print("{:3}".format(number))