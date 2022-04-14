def find_slope(x1,y1,x2,y2):
    slopes = (y2-y1)/(x2-x1)
    return slopes
x1 = int(input("please enter value x1:"))
y1 = int(input("please enter value y1:"))
x2 = int(input("please enter value x2:"))
y2 = int(input("please enter value y2:"))
find_slope(x1,y1,x2,y2)
print(find_slope(x1,y1,x2,y2))