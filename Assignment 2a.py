hrs= input("Enter hours:")
h= float(hrs)
r= input("Enter rate")
r=float(r)
salary=(float(hrs*r))
if h>35:
   print(35*r+(hrs-35)*2.75*r)
   print(salary)