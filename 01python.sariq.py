import random 
n=100
numbers = list (range(1,n+1))
x=numbers.pop(random.randint(1,n+1))
#print(x)
# x ni toping
#print(sum(numbers2)-sum(numbers))


##	if i not in numbers:
#		print(i)
#		break

summa = n*(n+1)/2
print(summa - sum(numbers))