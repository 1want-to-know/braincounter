import random
from correct_ans import cor_ans
from file_work import write_res, read_this

def main():
    while True:
        print("1 - start a game, 2 - looking for in 'results', 3 - quit")
        chz = input()
        match chz:
            case '1':
                game()

            case '2':
                print("What do you want to find?")
                print("Write 'help' to discover commands")
                sth = input().lower()
                read_this(sth)
                print("------------------------------------")

            case '3':
                quit()

            case _:
                print("Enter something else!")
                print("------------------------------------")

def game():
    while True:
        #preparing for a game
        rnd, leng_res, lenght, oper, nums = prepare_game() 
        start_game(rnd, leng_res, lenght, oper, nums)
        #results in start_game cuz i didn't get how to send data to results in another way


def prepare_game():
    rnd = 0
    operators_unlocked = ['+', '-', '*', '/']
    while True:
        print("How many problems?")
        leng_res = length = int(input()) #leng is for write_res
        if length > 0:
            print("Enter operator: +, -, *, /")
            oper = input()
            if oper in operators_unlocked:
                print("Enter 2 numbers: minimum, maximum")
                nums = list(map(int, input().split()))
                if len(nums) == 2:
                    return rnd, leng_res, length, oper, nums
                else:
                    print("ERROR: you have entered either too many or too few numbers")
            else:
                print("ERROR: please, enter either +, -, *, or /")
        else:
            print("Enter another num!")


def start_game(rnd, leng_res, lenght, oper, nums):
    crt = 0 #correct answers
    wrg = 0 #wrong answers
    num1 = nums[0]
    num2 = nums[1]
    while lenght > 0:
        first = random.randint(num1, num2)
        second = random.randint(num1, num2)
        res_cor = cor_ans(first, second, oper) #counting correct answer
        print("------------------------------------")
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
            main()


if __name__ == "__main__":
    print("Welcome to BrainCounter!")
    main()