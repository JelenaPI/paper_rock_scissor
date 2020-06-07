import random
scores = open("rating.txt", 'r')
datas=scores.readlines()
scores.close()
player = input("Enter your name: ")
for line in datas:
    if player == line[0]:
        score = int(line[1])
    else:
        score = 0
print("Hello, " + player)
input_list = input().split(',')
list_elements = input_list if input_list != [''] else ['rock', 'paper', 'scissors']

mid = len(list_elements)//2
winning_set = [i for i in range(mid+1)]
winning_set.extend([i for i in range(-len(list_elements)+1,-mid)])
computer = ""
addition = ["!exit", "!rating"]
extended_list = list_elements.copy() #this is becouse we dont want to change list_elements when append exit and rating for extended list
extended_list.extend(addition)
print("Okay, let's start")

while player != "!exit":
    player = input()
    if player in extended_list:
        if player == "!rating":
            print("Your rating: ",score)
        elif player == "!exit":
            print('Bye!')
            exit()
        else:
            computer = random.choice(list_elements)
            # if pl_num - comp_num in winning_set:
            if list_elements.index(player) - list_elements.index(computer) == 0:
                print(f'There is a draw ({computer})')
                score += 50
            elif list_elements.index(player) - list_elements.index(computer) in winning_set:
                print(f'Well done. Computer chose {computer} and failed')
                score += 100
            else:
                print(f'Sorry, but computer chose {computer}')
    else:
        print("Invalid input")
