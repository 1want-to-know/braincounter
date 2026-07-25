commands = ["round", "operator", "num1", "num2", "length", "correct", "wrong"]
# There are low register since it will compare with sth which is already lowered
comm_sqbrkts = ["[val]", "[last]"]


def write_res(rnd, oper, first, second, length, crt, wrg):
    #Adding results to file
    with open('Results.txt', 'a') as fi:
        fi.write(f"Round: {rnd}\n")
        fi.write(f"Operator: {oper}\n")
        fi.write(f"Num1: {first}\n")
        fi.write(f"Num2: {second}\n")
        fi.write(f"Length: {length}\n")
        fi.write(f"Correct: {crt}\n")
        fi.write(f"Wrong: {wrg}\n")
        fi.write("\n")


def read_this(sth):

    if sth == 'help':
        print("------------------------------------")
        print("If you enter a word - Program would try to find it and")
        print("print all of words it found")
        print("        (ex. Correct -> finds all of lines with word 'Correct')")
        print("[val] - finds a value for a key")
        print("        (ex. 'Correct [val] -> finds all of numbers for 'Correct')")
        print("[last] - finds a last line with this word")
        print("        (ex. 'Round [last] -> finds last line with 'Round')")
        print("Words file include (you can write them with any registration):")
        print("Round", "Operator")
        print("Num1", "Num2")
        print("Lenght", "Correct")
        print("Wrong")
        return

    cl_sth = find_word(sth)
    if cl_sth is None:
        print("You have made a mistake. Try again!")
        return


    print("------------------------------------")
    with open('Results.txt', 'r') as fi:
        for line in fi:
            if cl_sth in line.lower():
                if '[val]' in sth:
                    parts = line.split(': ', 1)
                    if len(parts) == 2:
                        value = parts[1].strip()
                        print(value)
                elif '[last]' in sth:
                    last_value = line.strip()
                else:
                    print(line.strip())


def find_word(sth): #for finding sth in commands
    for cmd in commands: #check from 'commands' list above
        if cmd in sth:
            cl_sth = cmd
            return cl_sth
