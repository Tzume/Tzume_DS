import numpy as np

def random_predict(number:int=1) -> int:
    """Guess the number randomly for less that 20 attempt

    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: Amount of attempts
    """
    
    count=0
    min=1
    max=100
    number=np.random.randint(min,max)

    while True:
        count+=1
        mid=int((min+max)//2)
        if mid>number:
            max=mid
        elif mid<number:
            min=mid
        else:
            break #the end of the game, exit from the cycle
    return count
print(f'The computer guessed the number by {random_predict()} attempt.')

def score_game(random_predict) -> int:
    """The average amount of attempt used to guess the number if we aplly the algorithm 1000 times

    Args:
        random_predict ([type]): function that guesses the number

    Returns:
        int: average amount of attempt
    """

    count_ls = [] # the list where the amount of attempt is collected
    np.random.seed(1) # fix seed number for reproducibility
    random_array = np.random.randint(1, 101, size=(1000)) # set the list of numbers

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # find the average amount of attempt

    print(f'In average the algorithm guesses the number by the following amount of attempt: {score}')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)
