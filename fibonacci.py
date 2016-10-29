
def seriesFibonnaci(n):
	""" Function takes integer n as an input and returns a sequence of fibonnaci numbers to that point """
	series =[]
	fine_series =[]
	for i in range(n):
		series.append(Fibonnaci(i))
	for i in series:
		if i<n:
			fine_series.append(i)
		elif i>n:
			break
	return fine_series






def Fibonnaci(n):
    

    
    if n == 0: 
    	return 0
    elif n == 1: 
    	return 1
    else: 
    	return Fibonnaci(n-1)+Fibonnaci(n-2)








print seriesFibonnaci(10)


"""
ASYMPTOTIC ANALYIS


series =[] ------------------------------------>BigO(1)
	for i in range(n):------------------------->BigO(n)
		series.append(Fibonnaci(i))------------>BigO(n^2)
	return series ----------------------------->BigO(1)

	==========>BigO(1) + BigO(n) + BigO(n^2) + BigO(1)


Answer ===============> BigO(2^n)


"""