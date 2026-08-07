import random
from correct_ans import corr_ans
from file_work import write_res, read_this


def gen_ex(min: int, max: int, oper):
    a = random.randint(min, max)
    b = random.randint(min, max)
    corr_val = int(corr_ans(a, b, oper))
    return a, b, corr_val


def answer(user_ans, corr_val, crt, wrg, amou_ex):
    if amou_ex >= 1:
        amou_ex -= 1
        if user_ans == corr_val:
            crt += 1
            return crt, wrg, amou_ex
        else:
            wrg += 1
            return crt, wrg, amou_ex
    else:
        return


def open_last_round():
    with open('Results.txt', 'r') as fi:
        for line in fi:
            if line.startswith('Round: '):
                parts = line.split(': ', 1)
                return int(parts[1])
        return 0
