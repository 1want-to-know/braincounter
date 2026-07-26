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
    rnd = 0 #It must be 'last round', not 0
    

def game():
    rnd = 0 #It must be 'last round', not 0
    while True:
        crt = 0 #correct answers
        wrg = 0 #wrong answers
        #preparing for a game
        print("How many problems?")
        leng = length = int(input()) #leng is for write_res
        if length > 0:
            print("Enter operator: +, -, *, /")
            oper = input()
            print("Enter 2 numbers: minimum, maximum")
            nums = list(map(int, input().split()))

            if len(nums) == 2:
                while length > 0:
                    #the game starts
                    first = random.randint(nums[0], nums[1])
                    second = random.randint(nums[0], nums[1])
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
                print("------------------------------------") #Results
                rnd += 1
                print("Results of round:")
                print(f"Correct answers: {crt}")
                print(f"Wrong answers: {wrg}")
                write_res(rnd, oper, nums[0], nums[1], leng, crt, wrg)

                print("Are you want to try again? y/n")
                restart = input()
                match restart:
                    case 'y':
                        continue #start a new game
                    case 'n':
                        print("----------------------------------------------")
                        main() #main menu
            elif nums[1] == 0:
                print("You can't divide by 0!!!!!")
            else:
                print("Try again!")
        else:
            print("Enter another num!")


if __name__ == "__main__":
    print("Welcome to BrainCounter!")
    main()