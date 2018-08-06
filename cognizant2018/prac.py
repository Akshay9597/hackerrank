arr = list(map(int,input().split()))
print("arr",arr)
arr_set = set(arr)
print("arr_set",arr_set)
arr_list = list(arr_set)
print("arr_list",arr_list)
lenarr_set = len(arr_set)
maxand = 0
max1 = []
max2 = []
#find max
for i in range(lenarr_set-1):
	for j in range(i+1,lenarr_set):
		tmp1 = arr_list[i]
		tmp2 = arr_list[j]
		if((tmp1 & tmp2) > maxand):
			maxand = tmp1 & tmp2
print("maxand",maxand)
#find pairs with this max value
for i in range(lenarr_set):
	for j in range(i,lenarr_set):
		tmp1 = arr_list[i]
		tmp2 = arr_list[j]
		if(tmp1 & tmp2 == maxand):
			max1.append(tmp1)
			max2.append(tmp2)
			
print("max1",max1)
print(max2)
#max1 = set(max1)
#max2 = set(max2)
#all indices in pairs
indexmax1 = []
indexmax2 = []
while(len(max1) > 0):
	tmax1 = max1.pop()
	tmax2 = max2.pop()
	for i in range(len(arr)):
		if(arr[i] == tmax1):
			indexmax1.append(i)

	for i in range(len(arr)):
		if(arr[i] == tmax2):
			indexmax2.append(i)

print("indexmax1",indexmax1)
print("indexmax2",indexmax2)
for i in range(len(indexmax1)):
	for j in range(len(indexmax2)):
		if(indexmax1[i] == indexmax2[j]):
			continue
		if(indexmax1[i] < indexmax2[j]):
			tmp = indexmax1[i]
			indexmax1[i] = indexmax2[i]
			indexmax2[i] = tmp


print(indexmax1)
print(indexmax2)
validindex1 = []
validindex2 = []
#check in desc order if they are actually max1 and max2
for i in range(len(indexmax1)):
	p = indexmax1[i]
	q = indexmax2[i]
	tmp = []
	for j in range(p,q):
		tmp.append(arr[j])
	tmp.sort(reverse=True)
	print(tmp)
	if(arr[p] >= arr[q]):
		if(arr[p] == tmp[0] and arr[q] == tmp[1]):
			validindex1.append(p)
			validindex2.append(q)
	else:
		if(arr[p] == tmp[1] and arr[q] == tmp[0]):
			validindex1.append(q)
			validindex2.append(p)
#finding 1st L to be min.
L = []
R = []
min = 1024

for i in validindex1:
	if(i < min):
		min = i
		
for i in range(len(validindex1)):
	if(validindex[i] == min):
		L.append(validindex1[i])
		R.append(validindex2[i])

sdist = 1024

for i in range(len(L)):
	if(R[i]-L[i] < sdist):
		l = L[i]
		r = R[i]

print(l,r)




