'''This is a test document
   For some simple test
   User: miyunke
   Test mode
   Date: 2019-5-17'''

import turtle

def check_fermat(a, b, c, n):
   if n <= 2:
      print('The number of n is invalid,please input n > 2')
   elif ((a**n + b**n) == c**n):
      print('Oh,my god,Feima is wrong.')
   else:
      print("No,can't do that.")

def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)


bob = turtle.Turtle()

bob.pu()
bob.goto(-150, 90)
bob.pd()
snowflake(bob, 300)

turtle.mainloop()

