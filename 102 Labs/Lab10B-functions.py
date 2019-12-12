#################################################
######## Ty Ridings                     #########
######## Lab 10B - Function Definitions #########
######## Section -  C                   #########
#################################################

# Imports
import math

################################################
########   Function 1 : PrintOutput    #########
################################################

def PrintOutput(word):
    print('OUTPUT', word)

################################################
########   Function 2 : TriangleArea   #########
################################################

def TriangleArea(height,width):
    area = '%0.2f' % (0.50 * height * width)
    PrintOutput(area)

################################################
########   Function 3 : FeetToMeters   #########
################################################

def FeetToMeters(feet):
    meters = '%0.3f' % (feet * 0.3048)
    PrintOutput(meters)

################################################
########   Function 4 : PolarCoords    #########
################################################

def PolarCoords(x,y):
    r = 'r: ' + '%0.1f' % (math.sqrt(x**2 + y**2))
    theta = 'theta: ' + '%0.1f' % (math.degrees(math.atan(y/x)))
    PrintOutput(r)
    PrintOutput(theta)

################################################
########   Function 5 : EurosToDollars #########
################################################

def EurosToDollars(euros):
    dollars = '%0.2f' % (euros * 1.12)
    PrintOutput(dollars)
