import random
import csv
import matplotlib.pyplot as plt


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
	>>> sumRows("test.csv")
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

	for i in lstPlots:
		prob = i[0] / (i[0]+i[1])
		rarb = i[0]/i[1]
		plt.plot([prob], [rarb], 'o')
		plt.annotate(i, xy=(prob, rarb) )
	plt.xlabel("Probability")
	plt.ylabel("ra/rb")
	plt.title("Probability that player A wins against ra/rb")
	plt.grid()
	plt.show()





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





# 					2

def gamePars(p):
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

	return a+b

def gameEng(p, serverA = True):
	a = 0 				# team a score
	b = 0 				# team b score
	r = 0 				# random float
	tie = 0				# decider between 9 or 10 in a tie
	end = 9				# in case of tie, play to 9 ot 10
	time = 0
	gameOver = False

	while gameOver == False:
		r = random.random()  # Get random float value 0-1 to see who 'won'
		if r < p:
			if serverA == True:  	# If A served first
				a += 1				# Add to a's score
			serverA = True			# else just make a serve next
		else:
			if serverA == False:
				b += 1
			serverA = False	
		time +=1
		
		# Check the scores according to the rules
		if a == 8 and b == 8:
			tie = random.randrange(1,3)
			if tie == 1:
				end = 9
			else:
				end = 10


		if (a >= end or b >= end):
			gameOver = True

	return time

def scorringPlot():
	import numpy
	p = numpy.arange(0.05, 1.5 , 0.05) # A player win probability
	linePars = []
	lineEng = []
	for prob in p:
		linePars.append(gamePars(prob))
		lineEng.append(gameEng(prob))


	plt.plot(p, linePars, color='b')
	plt.plot(p, lineEng, color='g')
	plt.ylim((5, 50))
	plt.xlim((0.1,1.5))
	plt.xlabel("Relative player ability")
	plt.ylabel("Time in minutes")
	plt.title("Difference between PARS and English scoring")
	plt.legend(['PARS system', 'English System'], loc = 'upper right')

	plt.show()


#			 Answer
# When the player ability is similar, the English scoring system will
# often make longer matches as the players don't receive points unless
# they were the ones serving making them play more matches.
# However when one player has majorly higher ability, PARS system takes longer,
# Simply because of the score that needs to be reached.
