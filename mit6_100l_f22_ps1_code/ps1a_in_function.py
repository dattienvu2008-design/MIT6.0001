def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	amount_saved = 0
	r = 0.05
	time = 0
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while True:
	    amount_saved = amount_saved + amount_saved*(r/12)
	    amount_saved += (yearly_salary/12)*portion_saved
	    time+=1
	    if amount_saved >= cost_of_dream_home*0.25:
	        break
	
	print("Number of months: ", time)
	
	
	
	
	return months