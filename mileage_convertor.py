print("how many kilometers did you run today?")#prints this out for the user to see
kms = input() #the input allows us to take user input then assign it to the kms variable
miles = float(kms)/1.60934 #the value of kms is converted to a float and then assigned to the variable miles
miles = round(miles,2) #this function rounds off miles to trwo decimal places
print(f"okay, your {kms} km  run  is eqaul to {miles} miles") #f format allows us to mix different data types