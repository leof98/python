# Implement a program in Python that prompts the user for mass as an integer (in kilograms) 
# and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

def main():
    mass = int(input("m: "))
    nstn(mass)

def nstn(m):
    c = 300000000
    e = m * (c ** 2)
    print(e)
    
main()
