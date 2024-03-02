#join
items = 'zero one two three'.split() #문자열을 띄어쓰기 단위로 분리하여 원소로 하는 리스트

colors = ['red', 'blue', 'green', 'yellow']
result = ','.join(colors) #콤마로 이어붙이기(' '안에 넣는 문자에 따라 다름)


#list comprehensions
list1 = [i for i in range(10) if i % 2 == 0] #filter 넣기(if문)

case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]

result = [i+j for i in case_1 for j in case_2 if not (i==j)] #리스트 안에 이중for문 넣기
result.sort()


#two-dimensional
result2 = [[i+j for i in case_1] for j in case_2] #두번째 for문 기준


#enumerate (번호를 붙여서 추출)
mylist = ["a", "b", "c", "d"]
result = [i for i in enumerate(mylist)]
result2 = {i:j for i, j, in enumerate('Gachon University is an academic'.split())}


#zip (두 list의 값을 병렬적으로 추출)
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

result = [sum(x) for x in zip((1,2,3), (10, 20, 30), (100, 200, 300))]

#for i, (a, b) in enumerate(zip(alist, blist)): #(a, b) 괄호로 묶기
    #print(i, a, b)
   
    
#lambda 
f = lambda x,y: x+y #def 대신에 사용
#print(f(-1, 4))

#list 원소들 lambda 사용
ex = [1, 2, 3, 4, 5]
g = lambda x: x**2
#print(list(map(g, ex))) #list(), map()

h = lambda x,y: x+y
#print(list(map(h, ex, ex)))

#print(list(map(lambda x: x**2 if x % 2 == 0 else x, ex)))

i = lambda x: x ** 2
#print(map(i, ex))
#for k in map(i, ex):
    #print(k)

    
import sys
sys.getsizeof(ex)
sys.getsizeof((map(lambda x: x+x, ex)))
sys.getsizeof(list(map(lambda x: x+x, ex)))

#Reduce
from functools import reduce
#print(reduce(lambda x, y: x+y, [1,2,3,4,5])) #reduce(func, iterable)


#factorial
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))
#print(factorial(5))
 
    
#asterisk
#*args
def asterisk_test(a, *args):
    print(a, args) #맨 앞 변수 a / 나머지는 튜플
    print(type(args))
#asterisk_test(1,2,3,4,5,6)

#kargs 키워드 
def asterisk_test2(a, **kargs):
    print(a, kargs) #dict 타입
    print(type(kargs))
#asterisk_test2(1, b=2, c=3, d=4, e=5, f=6)

def asterisk_test3(a, *args):
    print(a, args[0])
    print(a, args)
    print(type(args))
#asterisk_test3(1, (2,3,4,5,6)) #args : (2,3,4,5,6)을 하나의 원소로 하는 튜플 생성

def asterisk_test4(a, args):
    print(a, *args) #unpacking
    print(a, args)
    print(type(args))
#asterisk_test4(1, (2,3,4,5,6))


#unpacking
a, b, c = ([1,2], [3,4], [5,6])
#print(a, b, c)
data = ([1,2], [3,4], [5,6])
#print(*data)

#for data in zip(*([1,2], [3,4], [5,6])):
    #print(sum(data)) #(1,3,5)의 합 / (2,4,6)의 합
    
def asterisk_test5(a, b, c, d, e=0):
    print(a, b, c, d, e)
data = {"d":1, "c":2, "b":3, "e":56}
#asterisk_test5(10, **data)


#vector 계산 (zip)
u = [2,2]
v = [2,3]
z = [3,5]
a = 5
result = [a * sum(t) for t in zip(u, v, z)] #벡터의 합과 스칼라곱
#print(result)

#matrix 계산
matrix_a = [[3,6], [4,5]]
matrix_b = [[5,8], [6,7]]
#zip(*t) unpacking 이유: ([3,6], [5,8]) 튜플 형태로 묶어짐
result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]
#print(result)

#scalar matrix product
matrix_a = [[3,6],[4,5]]
alpha = 4
result = [[alpha * element for element in t] for t in matrix_a] #for t in matrix 큰 list의 원소들의 타입은 list 
#print(result)

#transpose
matrix_a = [[1,2,3],[4,5,6]]
result = [[element for element in t] for t in zip(*matrix_a)] #unpacking 해야함!!
#print(result)
#print(matrix_a) #list 전체
#print(*matrix_a) #원소 모두 따로 출력되는 unpacking 

#matrix product
matrix_a = [[1,1,2], [2,1,1]]
matrix_b = [[1,1],[2,1],[1,3]]
result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix_b)] for row in matrix_a]
print(result)
