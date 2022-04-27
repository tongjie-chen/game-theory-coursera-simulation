import random
a = [random.random() for i in range(100000)]
price = 100
sum([1.5*i*100-price for i in a if price > i*100])/len(a)
