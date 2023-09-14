hrs= input("Enter Hours:")
h= float(hrs)
r= input("Enter rate")
r= float(r)
if h>35:
    x=(r*2.75)*(h-35)+(35*r)
if h<=35:
    x=h*r
  