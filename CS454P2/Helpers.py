# Helper class to make life so much nicer
class DFA():
	def __init__(self, file):
		self.n = 0
		self.k = 0
		self.accepting = []
		self.transitions = []

		if(file != ""):
			# This is kinda hacky but oh well
			self.parseDFAFile(file)

	def parseDFAFile(self, file):
		with open(file) as fp:
			# read n and k
			n, k = fp.readline().split()

			# convert n and k to ints
			self.n = int(n)
			self.k = int(k)

			# Read in the line specifying accepting states
			F = fp.readline().split()

			# Convert those to ints, store
			for i in range(self.n):
				self.accepting.append(int(F[i]))

			# Process the input lines, which are the rows of the transition
			# matrix at this point
			for i in range(self.n):
				l = fp.readline().split()

				for j in range(len(l)):
					l[j] = int(l[j])

				self.transitions.append(l)