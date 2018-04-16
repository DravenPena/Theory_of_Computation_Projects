from Helpers import DFA


def P1():
	# tested with k = 7 N = 1243
	k = getInt("Enter an integer k: ")

	alphabet = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

	N = getInt("Enter an integer N: ")

	dfa = makeDFA(alphabet, k)

	result = doThing(dfa, N)

	print(result)


def doThing(dfa, N):
	N_str = str(N)
	cur_arr = [0] * 2 * dfa.k
	cur_arr[0] = 1

	for i in range(len(str(N))):
		new_arr = [0] * 2 * dfa.k

		cur_arr_idx = 0
		for j in cur_arr:
			if(j == 1):
				if(cur_arr_idx < dfa.k):
					# Add new prime at j'
					new_j_prime = cur_arr_idx
					new_arr[new_j_prime + dfa.k] = 1

					# Advance j
					new_j = dfa.transitions[cur_arr_idx][int(N_str[i])]
					new_arr[new_j] = 1
				else:
					# Advance all j''s
					new_j_prime = dfa.transitions[cur_arr_idx % dfa.k][int(N_str[i])]
					new_arr[new_j_prime + dfa.k] = 1
			cur_arr_idx += 1

		cur_arr = new_arr

	if(cur_arr[0] == 1 or cur_arr[dfa.k] == 1):
		return 'yes'
	return 'no'


def makeDFA(alphabet, k):
	resultDFA = DFA("")
	resultDFA.k = k
	alphabet_len = len(alphabet)
	resultDFA.n = alphabet_len

	for i in range(k):
		resultDFA.transitions.append([0] * alphabet_len)
		for j in alphabet:
			resultDFA.transitions[i][j] = (((i * 10) + j) % k)

	return resultDFA


def getInt(prompt):
	inp = input(prompt)
	valid = False

	while(not valid):
		try:
			inp = int(inp)
			valid = True
		except ValueError:
			inp = input("Invalid input - " + prompt)

	return inp