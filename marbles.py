from random import randint
def main():
    # Simple user input for testing
    if input('Would you like to play a detailed game? (y/n)').lower().startswith('y'):
        print(marble_game(
            # Get input for num_plays
            num_plays=int(input('How many games would you like to play?')),
            # List comprehension, first split user input into a list based off of spaces, then cast each item in the list to an integer.
            marble_list=[int(num) for num in input('Please enter the number of marbles in the bag of each type, separated by spaces.').split(' ')],
            # Simple casting for the other pieces of user input
            win_requirement=int(input('How many marbles should be drawn each game?')),
            cost=float(input('How much is the ante for each game?')),
            reward=float(input('How much will the player win?'))
        ))
    else:
        print(marble_game(int(input('How many games would you like to play?'))))
'''
Input:
    num_plays = number of games user would like to play
    marble_list = list of the quantity of the different types of marbles in the bag
    win_requirement = how many marbles should be drawn each game, and thus how many need to be the same for the game to count as a 'win'
    cost = 'ante' each turn
    reward = ammount of money rewarded for a win
Output:
    List of running totals after each turn of the game
'''
def marble_game(num_plays, marble_list=[3, 2, 1], win_requirement=2, cost=1, reward=2):
    # Init score to 0
    score = [0]
    # For each game
    for i in range(num_plays):
        # Ante in the cost
        score.append(score[-1] - cost)
        # Set marble bag to be a list of individual marbles and their types, rather than quantites.
        # i.e [1, 2, 3] becomes [0, 1, 1, 2, 2, 2]
        marble_bag = [i for i in range(len(marble_list)) for j in range(marble_list[i])]
        # Draw however many marbles from the bag
        marbles_drawn = [draw_and_remove(marble_bag) for i in range(win_requirement)]
        # Casting to a set removes duplicates. Thus, if the set has only one item, there were no duplicates, and the user won
        if len(set(marbles_drawn)) == 1:
            # Increment the current running total by the reward
            score[-1] += reward
    # Return the running total, except for the initial value of 0
    return score[1:]
# Function draws a random index from a list, removes that item, and then returns the item.
def draw_and_remove(list):
    # Draw item randomly
    drawn_index = randint(0, len(list) - 1)
    drawn_item = list[drawn_index]
    # Remove that item
    list.pop(drawn_index)
    # Return that item
    return drawn_item
if __name__ == '__main__':
    main()
