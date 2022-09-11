def binary_search2(a:list, find):
	if find > a[-1]:
		return [len(a)-1,len(a)]

	if len(a) <= 1:
		return [0,len(a)]
	middle = len(a)//2
	# print(a)
	# print(middle)
	# print(a[middle])
	left = a[:middle]
	right = a[middle:]
	left_border = 0
	right_border = len(a)
	if a[middle] > find:
		# print(f"left")
		left_border, right_border = binary_search(left, find)
	elif a[middle] < find:
		# print(f"right")
		left_border, right_border = binary_search(right, find)
		left_border , right_border = left_border + middle, right_border + middle
	elif a[middle] == find:
		# find_left
		left_border = middle
		right_border = middle
		for i in range(middle, 0, -1):
			if a[i] == find:
				left_border = i
			else:
				break
		for i in range(middle, len(a)):
			if a[i] == find:
				right_border = i
			else:
				break
		# print(left_border, right_border)
		# return left_border, right_border
	return left_border, right_border


def left_border(a:list, find:int):
	left = -1
	right = len(a)

	while left < right - 1:
		middle = (left + right)//2
		# print(f"middle: {middle}, a[m]:{a[middle]}")
		if find <= a[middle]:
			right = middle
		else:
			left = middle
	return left

def right_border(a:list, find:int):
	left = -1
	right = len(a)

	while left < right - 1:
		middle = (left + right)//2
		# print(f"middle: {middle}, a[m]:{a[middle]}")
		if find < a[middle]:
			right = middle
		else:
			left = middle
	return right



def binary_search(a:list, find:int):
	left = left_border(a, find)
	right = right_border(a,find)
	# print(f"left: {left}, right: {right}")
	return [left, right]



a = [1,2,2,2,3,3,4,5,    5,5,5,5,5,7,7,7,7]
test_finds = [
	[0,[-1,0]],
	[1,[-1,1]],
	[2,[0,4]],
	[3,[3,6]],
	[4,[5,7]],
	[5,[6,13]],
	[6,[12,13]],
	[7,[12,17]],
	[8,[16,17]],
]


def test_binary_search(a, test_finds):
	a = sorted(a)
	print(a)
	print(len(a))
	for i, f in enumerate(test_finds):
		test_in = f[0]
		test_out = f[1]
		calc_out = list(binary_search(a, find = test_in))
		print(f"test # {i}: ", "Ok" if calc_out == test_out else "Fail", f"\t test_in: {test_in}, test_out: {test_out}, calc_out: {calc_out}")
test_binary_search(a, test_finds)





def fib(n: int):
	if n <= 1:
		return n
	# print(n)
	return fib(n-2) + fib(n-1)


def fib2(n: int):
	fib = [0,1]
	for i in range(2,n+1):
		fib.append(fib[-1] + fib[-2])
	return fib[-1]

def fib3(n: int):
	fib = [0,1] + [0]*(n-2)
	for i in range(2,n):
		# fib.append(fib[-1] + fib[-2])
		fib[i] = fib[-1] + fib[-2]
	return fib[-1]

# 1, 1, 2, 3, 5, 8
# print(fib(30))
import time
s = time.time()
# print(fib2(30))
# print(fib2(10000))
fib2(100000)
print(time.time() - s)
s = time.time()
fib3(100000)
print(time.time() - s)





def kuznec(n:int, combination = []):
	count_combo = 0
	if n < 0:
		return 0
	if n == 0:
		print(combination)
		print(len(combination))
		return 1
	for step in [1,2]:
		# if sum(combination+[step]) == 4 or sum(combination+[step]) == 7:
		# 	continue
		count_combo += kuznec(n-step, combination+[step])
	return count_combo

def kuznec2(n:int, combination = []):
	if n < 0:
		return
	if n == 0:
		print(combination)
		return combination
	for step in [1,2]:
		kuznec(n-step, combination+[step])



import time
s = time.time()
# print(fib2(30))
# print(fib2(10000))
# 1 2 3 5 8 13
# 1 2 3 4 5 6 7 8
# 1 1 2 2 3 3 4 4
count_combo = kuznec(3)
print(f"count_combo: {count_combo}")
count_combo = 0
print(time.time() - s)
s = time.time()
# kuznec(5)
print(time.time() - s)

# n = 9
# print(n//2 + (1 if n%2 > 0 else 0))




# 2
# [2]
# [1,1]

# 4
# [2,2]
# [1,1,2]
# [1,2,1]
# [2,1,1]
# [1,1,1,1]


# def kuznec_cost(n:int, price, combination = []):
# 	count_combo = 0
# 	if n < 0:
# 		return 0
# 	if n == 0:
# 		print(combination)
# 		print(len(combination))
# 		return 1
# 	for step in [1,2]:
# 		# if sum(combination+[step]) == 4 or sum(combination+[step]) == 7:
# 		# 	continue
# 		count_combo += kuznec(n-step, combination+[step])
# 	return count_combo

# kuznec_cost(3,[0.5,0.4,0.3])


# 1 2 3 4 5 6 7 8 9
# 1 1 2 2 3 3 4 4 5

print("kuznec_dynamic")
def kuznec_dynamic_one(n: int):
	k = [0,1] + [0]*n
	for i in range(2,n+2):
		k[i] = k[i-2] + k[i-1]
	print(k)
	return k[-1]
kuznec_dynamic_one(5)

# 1 1 2
# 1 2 1
# 2 1 1
# 1 1 1 1
# 2 2






print("kuznec_dynamic with cost")

def kuznec_dynamic(n: int, price:list):
	cost = 0
	k = [0,1] + [0]*n
	for i in range(2,n+2):
		k[i] = k[i-2] + k[i-1]
		cost+= k[i]*price[i-2]
		c_k_2 = k[i-2]*price[i-2-2]
		c_k_1 = k[i-1]*price[i-1-2]
		if c_k_1 < c_k_2:
			k[i] = c_k_1
		else:
			k[i] = c_k_2
	print(k)
	print(cost)
kuznec_dynamic(4, [0.5,0.4,0.3, 0.2])
kuznec_dynamic(4, [1,1,1, 1])

print("kuznec_cost2")

def kuznec_cost2(n, price):
	c = [0, price[1], price[1] + price[2]] + [0]*(n-2)
	for i in range(3, n+1):
		c[i] = price[i] + min(c[i-1], c[i-2])
	print(c)
kuznec_cost2(3, [0, 0.5,0.4,0.3])
kuznec_cost2(4, [0, 0.5,0.4,0.3, 0.2])


n = 5
m = 3
a = [[0]*m]*n
print(a)
a[0][1] = 2
print(a)

b = [[0]*m for _ in range(n)]
print(b)
b[0][1] = 2
print(b)

c = list([list([0]).copy()*m]).copy()*n
print(c)
c[0][1] = 2
print(c)

# print(a)