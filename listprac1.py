n = int(input())
arr = []
for i in range(n):
	l = list(input().split())
	if(l[0] == "insert"):
		arr.insert(l[1],l[2])
	elif l[0] == "print":
		print(arr)
	elif l[0] == "remove":
		arr.remove(l[1])
	elif l[0] == "append":
		arr.append(l[1])
	elif l[0] == "sort":
		arr.sort()
	elif l[0] == "pop":
		arr.pop()
	elif l[0] == "reverse":
		arr.sort(reverse=True)
	else:
		pring("wrong")
