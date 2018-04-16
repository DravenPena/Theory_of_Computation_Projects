from queue import Queue
import numpy as np
from numpy import linalg

from Helper import DFA_matrix


def main():
	prompt = "Please select a problem from the list:\n[1]\tProblem 1\n[2]\tProblem 2\n[3]\tExit Program\nSelection: "
	selection = input(prompt)

	while("3" not in selection):
		print()
		if ("1" in selection):
			p1()
		elif ("2" in selection):
			p2()
		print()
		selection = input(prompt)

	print("Exiting")


def p1():
	n = int(input("Enter length of string: "))

	#                        1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38
	start_state = np.matrix([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=object)
	accept_state = np.matrix([[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [0]], dtype=object)

	A = linalg.matrix_power(DFA_matrix, n) # Turns out this step is actually pretty important.
	B = np.dot(start_state, A)
	C = np.dot(B, accept_state)

	print("Number of strings of length " + str(n) + " is: " + str(C.item()))


def p2():
    k = 7  # int(input("Please give me number for k: "))
    alphabet = [1, 3]  # []

	# a = input("gib input: ")
	# alphabet.append(int(a))
	# while(a is not ""):
	#       a = input("a: ")
	#       if(a is not "" and int(a) not in alphabet):
	#               alphabet.append(int(a))

    Table = [[(row * 10 + letter) % k for letter in alphabet] for row in range(k)]

    #print(Table)
    #print(alphabet)
    answer = []
    q = Queue()
    visited = [0 for x in range(0,k)]
    parent = [None for x in range(0,k)]
    q.put(0)
    while(not(q.empty())):
        x = q.get()
        for idx,y in enumerate( Table[x]):
            if( visited[y] == 0 ):
                visited[y] = 1 
                parent[y] = [x,alphabet[idx]]
                q.put( y )
        #print( list(q.queue) )
    #if( y == 0 ):#if there is a child that is zero go through the parent array starting at 
    y = 0
    while(not(parent[y][0] == 0)):
        answer.append( parent[y][1] )
        y = parent[y][0]
    answer.append(parent[y][1])
   # print( visited )
    print( parent )
    print( answer )
    print( answer[::-1] )










main()
