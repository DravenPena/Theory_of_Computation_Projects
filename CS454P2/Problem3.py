import queue
from Helpers import DFA

def P3():
	# Create dfa2 and dfa2 from the text files. The class will handle parsing
	dfa1 = DFA("dfa1.txt")
	dfa2 = DFA("dfa2.txt")

	# Get a new DFA which is the intersection of dfa1 and dfa2
	smashit = dotDFA(dfa1, dfa2)

	# Create an output file for the intersected DFA
	createOutputFile(smashit)


def createOutputFile(dfa):
	l1 = str(dfa.n) + ' ' + str(dfa.k) + '\n'
	l2 = ""
	for i in dfa.accepting:
		l2 += str(i) + ' '
	l2 = l2[:-1]
	l2 += '\n'

	ln = ""
	for i in dfa.transitions:
		for j in i:
			ln += str(j) + ' '
		ln = ln[:-1]
		ln += '\n'
	ln = ln[:-1]

	with open("dfa3.txt", 'w') as fp:
		fp.write(l1)
		fp.write(l2)
		fp.write(ln)


def dotDFA(dfa1, dfa2):
	resultDFA = DFA("") # bah
	# We can set k immediately
	resultDFA.k = dfa1.k

	# q is a FIFO Queue that will hold nodes that we need to process in the form of tuples (0, 0)
	q = queue.Queue()
	# tpl_map is a Map that will allow us to match a tuple (0, 0) to a proper index, 0
	tpl_map = {}
	# i will be the next available proper index, and will be the value
	# set for the keys in tpl_map
	i = 0

	# This block of logic adds the starting node to the queue so it will be
	# the first processed, since we only want to expand out from the starting node
	tpl = (0, 0)
	# Put tpl in the queue to be processed
	q.put(tpl)
	# The keys in tpl_map are just the string form of the tuple
	res_tpl_key = str(tpl)
	# Set the value equal to the next available index, i
	tpl_map[res_tpl_key] = i
	# Increment i to the next available index
	i += 1
	# Append a new row of transitions to the resultDFA so we can fill it out (in the loop below)
	resultDFA.transitions.append([0] * resultDFA.k)

	# Repeat until the queue is empty, meaning we've expanded to all reachable nodes (like BFS)
	while(not q.empty()):
		tpl = q.get()
		cur_tpl_key = str(tpl)

		# We want to add a transition for each letter in our alphabet since we're making a DFA
		for letter in range(resultDFA.k):
			# Individually figure out what the resulting node is after a transition on the input
			dfa1_res = dfa1.transitions[tpl[0]][letter]
			dfa2_res = dfa2.transitions[tpl[1]][letter]

			# Create a tuple from the results of the above transitions
			res_tpl = (dfa1_res, dfa2_res)
			res_tpl_key = str(res_tpl)

			# Check if we've already got this in our map. If not, then we need to add it in because
			# we've got a new row of transitions we now need to populate
			if(res_tpl_key not in tpl_map):
				# Add it into the queue so we can figure out its transitions later
				q.put(res_tpl)
				# Assign the next available index
				tpl_map[res_tpl_key] = i
				# Add in a new row of empty transitions to be filled out in a later loop
				resultDFA.transitions.append([0] * resultDFA.k)
				i += 1

			# Set the value for the current tuple (node) on the input letter to the resulting tuple
			resultDFA.transitions[tpl_map[cur_tpl_key]][letter] = tpl_map[res_tpl_key]

	# Create accepting matrix and populate it with 0s
	resultDFA.n = len(resultDFA.transitions)
	resultDFA.accepting = [0] * resultDFA.n

	for i in range(dfa1.n):
		for j in range(dfa2.n):
			tpl = (i, j)
			tpl_key = str(tpl)
			# Check if the tuple is even in the map first. If not, then it means we cannot reach it
			# from the starting state, so we ignore it
			if(tpl_key in tpl_map):
				# Since we're doing an intersection, BOTH individual parts of our tuple state must be
				# accepting states for the new state in resultDFA to be an accepting state
				if(dfa1.accepting[i] == 1 and dfa2.accepting[j] == 1):
					resultDFA.accepting[tpl_map[tpl_key]] = 1

	return resultDFA