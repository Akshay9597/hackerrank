t = int(input())
for i in range(t):
	count = 0
	n,k = map(int,input().split())
	for p in range(1,n+1):
		for q in range(1+p,n+1):
		#	print(p,q)
			if((p+q) % k == 0):
				count += 1
	print(count)
