
def corr_ans(fir, sec, oper):
    match oper:
        case '+':
            return fir + sec
        case '-':
            return fir - sec
        case '*':
            return fir * sec
        case '/':
            return fir / sec