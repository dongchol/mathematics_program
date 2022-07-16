input_lst = [8,5,6,2,4,11,20,1,3,3]

for i in range(1, len(input_lst)):
    idx = i
    for j in range(i,0,-1):
        if input_lst[j-1] > input_lst[j]:
            input_lst[j-1], input_lst[j] = input_lst[j], input_lst[j-1]

print(input_lst)
