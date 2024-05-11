def integration(a,b,c,d,rectangles):
    dx = (b-a)/rectangles
    dy = (d-c)/rectangles
    sum = 0
    
    for i in range(1,rectangles + 1):
        for j in range(1, rectangles + 1): ## riemann sums
            x = a + ((i-0.5)*dx)
            y = c + ((j-0.5)*dy)
            fxyz = eval(function) #function goes here
            sum = sum + fxyz
        
    return sum*dx*dy

    
## ∫∫fxydA 
##   
## where dA can be arrangements of dx*dy (by Fubini's Theorem). Default: dx*dy
##
## ∫∫fxydA is integrated over Region = {(x,y) | a≤x≤b, c≤y≤d} 
##

function = input("Enter the function f(x,y) = ")
a_bound = float(input("Lower bound for the dx integral (a): "))
b_bound = float(input("Upper bound for the dx integral (b): "))

c_bound = float(input("Lower bound for the dy integral (c): "))
d_bound = float(input("Upper bound for the dy integral (d): "))


rectangles = 100 ## more rectangles = more accurate approx.

tripleintegral = (integration(a_bound,b_bound,c_bound,d_bound,rectangles))
print("∫∫",function," = ", tripleintegral)
