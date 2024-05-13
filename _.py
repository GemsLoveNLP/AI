# object is just an integer
GOAL = 30
LIMIT = 10

def is_over(obj):
    return obj == GOAL

def minimax(obj,maximizing):
    if maximizing:
        if is_over(obj):
            return -1
        max_value = -2
        for i in range(1,min(LIMIT+1,GOAL-obj+1)):
            new_value = minimax(obj+i,False)
            if new_value > max_value:
                max_value = new_value
        return max_value
    else:
        if is_over(obj):
            return 1
        min_value = 2
        for i in range(1,min(LIMIT+1,GOAL-obj+1)):
            new_value = minimax(obj+i,True)
            if new_value < min_value:
                min_value = new_value
        return min_value
    
def get_best_move(obj):
    max_value = -2
    max_move = 1
    for i in range(1,min(LIMIT+1,GOAL-obj+1)):
        new_value = minimax(obj+i,False)
        if new_value > max_value:
            max_value = new_value
            max_move = i
    return max_move

def main():
    obj = 0
    i = 0
    while True:
        i += 1
        print(f"round {i}")
        obj += int(input("Enter your number: "))
        print(f"SUM = {obj}")
        if is_over(obj):
            print("Human wins")
            return
        best_move = get_best_move(obj)
        print(f"Bot: {best_move}")
        obj += best_move
        print(f"SUM = {obj}")
        if is_over(obj):
            print("Bot wins")
            return
        print()

main()