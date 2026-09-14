## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
low = 0
high = 1
mid = 0.5
r = 0
##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
while True:
    if abs(initial_deposit*(1+mid/12)**36 - 800000*0.25) <= 100:
        print("Best saving rate: ", mid)
        break
    elif initial_deposit*(1+mid/12)**36 - 800000*0.25 > 0:
        high = mid
        mid = (high + low)/2
    elif initial_deposit*(1+mid/12)**36 - 800000*0.25 < 0:
        low = mid
        mid = (high + low)/2
    



