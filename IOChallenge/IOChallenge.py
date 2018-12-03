#question: it creates a file named jabberwocky.txt, but it doesn´t
#write anything to it --> solved!!!! --> wichtig: "file = time_table" bei print beachten

with open("jabberwocky.txt", 'w') as time_table:
	for i in range(1, 13):
		print("{} times {} is {}".format(i, 2, i*2), file=time_table)
