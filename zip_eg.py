# Zip function example program
x = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursaday", "Friday", "Saturday"]
y = [1,2,3,4,5,6,7]
for days, num in zip(x,y):
    print("Week day {0} and its number is {1}".format(days, num))
