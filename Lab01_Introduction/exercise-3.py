
#The program calculates the gravity acceleration.

#input
massJones = float(input('Enter the mass of Mr. Jones in Kg. '))

#calculations
earthRad = 6378 * 10 **3
earthMass = 5.9742 * 10 ** 24
gravConst = 6.67300 * 10 ** -11
gravForce = gravConst * earthMass * massJones / earthRad ** 2
gravAcceleration = gravForce / massJones

#output
print("The resulting value of g is", format(gravAcceleration, ',.4f'), "which is close to the earth's gravitacional force.") 

#ask user to quit program
input("\n\nPress any key to quit...")

##Output with 5 test cases
##
##Test Case 1.
##
##Enter the mass of Mr. Jones in Kg. 100
##The resulting va;ue of g is 9.8001 which is close to the earth's gravitacional force. 
##
##Test Case 2.
##
##Enter the mass of Mr. Jones in Kg. 200
##The resulting value of g is 9.8001 which is close to the earth's gravitacional force. 
##
##Test Case 3.
##
##Enter the mass of Mr. Jones in Kg. 75
##The resulting value of g is 9.8001 which is close to the earth's gravitacional force.
##
##Test Case 4.
##
##Enter the mass of Mr. Jones in Kg. 50
##The resulting value of g is 9.8001 which is close to the earth's gravitacional force.
##
##Test Case 5.
##
##Enter the mass of Mr. Jones in Kg. 1000000
##The resulting value of g is 9.8001 which is close to the earth's gravitacional force.