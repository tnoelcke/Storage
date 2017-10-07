import math

#returns the index of value or the nearest element less than value
def binarySearchI(toSearch, value, low, high, i):
	i = i + 1
	if( i == 10):
		return -1
	#sets the first position to check
	#damn you python that doesn't do integer trucation automatically like c...
	pos = int(math.ceil((high - low) / 2)) + low
	#if we found our value stop and return because we are done
	if value == toSearch[pos]:
		return pos
	#if we get down to one item and its smaller than value return pos.
	if high - low == 1 and value > toSearch[pos]:
		return pos
	#if the last value we found is larger than value return the element
	#one index lower because we know it will be less than value.
	if high - low == 1 and value < toSearch[pos]:
		return pos - 1 
	if(value < toSearch[pos]):
		return binarySearchI(toSearch, value, low, pos - 1, i)	
	else:
		return binarySearchI(toSearch, value, pos + 1, high, i)
i = 0
array1 = [1, 3, 4 , 6 ,7 , 9, 13, 25]
for i in range(1, 10):
	print binarySearchI(array1, i, 0 , len(array1), i)
	i = 0
