hrs = input("Enter hours:")
h = float(hrs)
xx = input("Enter the rate:")
x = float(xx)
if h <= 40:
    print(h * x)
elif h > 40:
    print(40* x + (h-40)*1.5*x)
    