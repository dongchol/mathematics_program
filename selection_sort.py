def comp(a,b):
    #인자를 제외하고 나머지 리스트에서 최솟값
    tmp = 0
    if a>b:
        a = tmp
        a = b
        b = tmp
    return a,b

def min_num(i_lst):
    min = i_lst[0]
    for i in range(0, len(i_lst)):
        if i_lst[i] < min:
            min = i_lst[i]
    return min

def swap(a,b):
    tmp = a
    a = b
    b = tmp
    return a,b

tmp_lst = [9,6,7,3,5]
input_lst = [9,6,7,3,5]
output = []

for i in range(0, len(input_lst)):
    min_idx = i
    for j in range(i+1, len(input_lst)):
        if input_lst[j] < input_lst[min_idx]:
            min_idx = j
    input_lst[i], input_lst[min_idx] = input_lst[min_idx], input_lst[i]

print(input_lst)
# 문제 해결 방향은 맞았으나, 인덱스를 사용하느냐 값을 받아 인덱스로 다시 변환하느냐의 차이로 난이도가 매우 달라짐
# 또한 값을 받아 다시 인덱스로 변환하게 될경우 구현한 swap 함수가 적용되지 않음. 따라서 인덱스를 사용하는것이 훨씬 간단함
# bubble sort 처럼 매번 바꾸는 것이 아니라 최소값을 찾아 해당 값만 위치 변동이 이루어짐

#for i in range(0, len(input_lst)):
#    k = input_lst[i]
#    t = input_lst[input_lst.index(min_num(input_lst[i:]))]
#    print(i, k, t)
#    k, t = swap(k,t)
#    input_lst[i], input_lst[input_lst.index(min_num(input_lst[i:]))] = k,t
#    print(k,t)
#    print(input_lst[i], input_lst[input_lst.index(min_num(input_lst[i:]))])
#    print()
#print(input_lst)
#print(min(input_lst))
