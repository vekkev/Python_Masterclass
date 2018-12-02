# This is my solution -> don´t know if correct!!!!

# songtext = set(input("Please enter your songtext here: "))
# #
# # vowels = {"a", "e", "i", "o", "u", "au", "ei", "ui"}
# #
# # finalList = []
# #
# # for words in songtext:
# # 	if vowels in songtext:
# # 		continue
# # 	else:
# # 		finalList += words
# # print(sorted(finalList))



songtext = input("Please enter your text:_")

vowels = frozenset("aeiou")
# or you could write -> vowels = {"a", "e", "i", "o", "u"}

finalSet = set(songtext).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)



