import sys
'''
def angryChildren(k, arr):
    # Complete this function
	tmp = list(itertools.permutations(arr, k))
	diff = max(arr)
	for i in tmp:
		minimum = min(i)
		maximum = max(i)
		tmp = maximum - minimum
		if(tmp < diff):
			diff = tmp
	return diff   
'''

def angryChildren(k, arr):
	n = len(arr)
	i = 0
	j = k - 1
	arr.sort()
	diff = max(arr)
	while(j < n):
		tmp = arr[j]-arr[i]
		if(tmp < diff):
			diff = tmp
		j += 1
		i += 1
	return diff
	
if __name__ == "__main__":
	n = int(input().strip())
	k = int(input().strip())
	arr = []
	arr_i = 0
	for arr_i in range(n):
		arr_t = int(input().strip())
		arr.append(arr_t)
	result = angryChildren(k, arr)
	print(result)

