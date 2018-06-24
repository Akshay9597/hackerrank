import sys

def chocolateFeast(n, c, m):
    # Complete this function
	w = 0
	count = 0
	while(n >= c):
		t = int(n / c)
		n = n - (t * c)
		w = w + t
	#	print('t,n,w',t,n,w)
		count += t
		if(w >= m):
			tmp = int(w/m)
			w = w - tmp * m
			n = n + tmp * c
	#		print('tmp,w,n',tmp,w,n)
	return count
    

if __name__ == "__main__":
	t = int(input().strip())
	for a0 in range(t):
		n, c, m = input().strip().split(' ')
		n, c, m = [int(n), int(c), int(m)]
		result = chocolateFeast(n, c, m)
		print(result)
