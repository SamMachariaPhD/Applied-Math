# import the libraries you intend to use
import numpy as np

# translate the main equation into a function
def cow_weight(r):
    cw = rho * ((4*np.pi)/3)*r**3 * g
    return cw

# define the variables
rho = 1850 # kg/m^3 bone?[https://physics.nist.gov/cgi-bin/Star/compos.pl?matno=119] (assumed constant)
g = 9.8 # m/m^2 (assumed constant) 
r1 = 0.6 # m (normal cow radius)
r2 = 3*r1 # m (super cow radius - thrice)

# get answers to your questions
Wnc = cow_weight(r1)
Wsc = cow_weight(r2)
ratio = Wsc/Wnc

# print answers (IN SCIENTIFIC NOTATION!) 
print("Normal Cow Weight ~\t %.2E kg.m/s^2" %Wnc) # (= N) confirm units
print("Super Cow Weight ~\t %.2E N" %Wsc)
print("Super Cow Weighs ~%.2E more than the Normal Cow" %ratio)
