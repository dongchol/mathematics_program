import random
import time

def NoD(actual_number): #Number of digit, 자리수
    return len(str(actual_number))-2

def actual_num_generater(r): #r means range
    lst = []
    for i in range(0,r):
        R = random.random() # 0~1까지의 소수점 아래 k자리 실수 발생
        lst += [R]
    return lst

def verification_arg(r, gen_num):
    check_sum = 0
    for i in range(0, len(r)):
        if(r[i] != gen_num):
            check_sum += 1
    if check_sum == len(r):
        return 'proof completed', check_sum
    else: return 'proof failed'


def batch(range_num, k, diagonal_arg_num_str):
        for i in range(0, range_num):
            #print(str(i) + ' : ' + str(k[i]) + ' : ' + str(NoD(k[i]))) #can check generate actual number and trial_num
            if len(diagonal_arg_num_str) > 18: break

            if (NoD(k[i]) > i):
                if int(str(k[i])[i+2])+1 == 10:
                    diagonal_arg_num_str += '0'
                else:
                    diagonal_arg_num_str += str(int(str(k[i])[i+2])+1)
            else: diagonal_arg_num_str += '1'

        diagonal_arg_num = float(str('0.' + str(diagonal_arg_num_str)))
        #print(diagonal_arg_num_str)
        print(diagonal_arg_num)
        p, ck_sum = verification_arg(k, diagonal_arg_num)
        print(p, ck_sum)


range_num = 18 #1000만까지 계산 시간 무난
#k = actual_num_generater(range_num)
diagonal_arg_num_str = ''
#print(k)

for i in range(0,100):
    start = time.time()
    random.seed(start)
    k = actual_num_generater(range_num)
    print('number of batch trials: ' + str(i) + ' ' + str(start))
    batch(range_num, k, diagonal_arg_num_str)
    time.sleep(0.1)
    print('시간 경과 : ' + str(time.time()-start))
    print()