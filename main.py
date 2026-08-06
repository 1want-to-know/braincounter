import random
from correct_ans import corr_ans
from file_work import write_res, read_this


def gen_ex(min: int, max: int, oper):
    a = random.randint(min, max)
    b = random.randint(min, max)
    corr_val = int(corr_ans(a, b, oper))
    return a, b, corr_val

def answer(user_ans, corr_val):
    if user_ans == corr_val:
        return True
    else:
        return False


def open_last_round():
    with open('Results.txt', 'r') as fi:
        for line in fi:
            if line.startswith('Round: '):
                parts = line.split(': ', 1)
                return int(parts[1])
        return 0

    
"""
def start_game(rnd, leng_res, length, oper, nums):
    while length > 0:
        if second < 0:
            print(f"{first}{oper}({second})=?")
        elif second >= 0:
            print(f"{first}{oper}{second}=?")
        res = int(input())
        if res == res_cor:
            print("Great!")
            length -= 1
            crt += 1
        else:
            print("Wrong!")
            length -= 1
            wrg += 1
    results(rnd, oper, num1, num2, leng_res, crt, wrg)
"""

def results(rnd, oper, num1, num2, leng_res, crt, wrg):
    print("------------------------------------") #Results
    rnd += 1 #you need to check if rnd == 1 'cause in results you'll don't get where is a new session
    print("Results of round:")
    print(f"Correct answers: {crt}")
    print(f"Wrong answers: {wrg}")
    write_res(rnd, oper, num1, num2, leng_res, crt, wrg)
    print("Are you want to try again? y/n")
    restart = input()
    match restart:
        case 'y':
            game()
        case 'n':
            print("----------------------------------------------")
