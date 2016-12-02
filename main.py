import random
import csv
#						1(a)
def game(ra,rb):
	"""
	>>> random.seed(57)
	>>> game(70, 30)
	(11, 5)
	"""

	p = ra / (ra + rb) 	# Probability value
	a = 0 				# team a score
	b = 0 				# team b score
	r = 0 				# random float

	gameOver = False

	while gameOver == False:
		r = random.random()  # Get random float value 0-1 to see who 'won'
		if r < p:
			a += 1
		else:
			b += 1
		# Check the scores according to the rules
		if (a >= 11 or b >= 11) and (a - b >= 2 or b - a >= 2):
			gameOver = True

	return a, b

#						1(b)
def winProbability(ra, rb, n):
	"""
	>>> winProbability(70, 30, 100)
	0.98
	"""
	a1 = 0 # Team a number of wins
	b1 = 0 # Team b number of wins
	i = 0 

	while i != n: 
		# Run game() number of times n 
		a,b = game(ra,rb)
		if a > b:
			# add 1 to total team a wins
			a1 += 1
		else:
			# add 1 to total team b wins
			b1 +=1

		i +=1
	answer = a1 / (a1 + b1) # store the probability

	print(str(answer)[:4])	#String so that the number can be cut off and not rounded.

#						1(c)

def sumRows(filename, header=True):
	"""
	>>> sumRows("players.csv")
	[(60, 20), (100, 55), (50, 40), (20, 70), (95, 85)]
	"""
	lst_names = []
	with open(filename) as csvfile:
		rdr = csv.reader(csvfile)
		if header == True:
			next(rdr)  # skip header row

		for row in rdr:
			lst_names.append((int(row[0]), int(row[1])))

	return lst_names

#						1(d)
def plotting(filename):


 	lstPlots = sumRows(filename)
 	print(lstPlots)






#						1(e)
def probabilities(ra,rb, n):

	import itertools
	import operator
	import functools

	a = ra / (ra+rb) 	# probability a wins
	b = 1 - a 			# probability b wins (same as a loses)

	probabilities = {'W':a, 'L':b}

	winProbability = 0

	for product in itertools.product(['W','L'], repeat=n): # repeat - number of games
		p = functools.reduce(operator.mul,
		[probabilities[p] for p in product])

		if product.count('W') > 1:
			winProbability += p


	return winProbability

def gameNum(ra,rb,winProb):
	"""
	>>> gameNum(60,40,0.9)
	5
	"""
	n = 1
	result = 0

	while result < winProb:
		result = probabilities(ra,rb, n)
		if result < winProb:
			n+=1

	return n



########## Answer ###########
# when n = 4, probability is 0.82 which is less than 0.9
# when n = 5, probability is 0.91 which is at least 0.9

# So lowest n = 5



import doctest
doctest.testmod()
