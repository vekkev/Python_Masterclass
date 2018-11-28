
IpAddress = input("Please enter an IP-Address: ")

segment = 1
segment_length = 0
char = ""

for char in IpAddress:
	if char == '.':
		print("segment {} contains {} characters".format(segment, segment_length))
		segment += 1
		segment_length = 0

	else:
		segment_length += 1

if char != '.':
	print("segment {} contains {} characters".format(segment, segment_length))



