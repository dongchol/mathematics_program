def comp(a,b):
    tmp = 0
    if a>b:
        tmp = a
        a = b
        b = tmp
        return a,b
    else: return a,b

input_lst = [7,4,5,1,3,10,5,7,16,2,24]

for i in range(0, len(input_lst)):
    for j in range(i+1, len(input_lst)):
        input_lst[i], input_lst[j] = comp(input_lst[i], input_lst[j])
print(input_lst)

#중첩 for문을 작성하기 때문에 정렬 알고리즘 시간 복잡도는 O(n^2)이다. best/avg/worst 전부 같은 시간 복잡도
