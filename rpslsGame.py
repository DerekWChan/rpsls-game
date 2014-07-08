from random import randint

def main():
    interface()

def interface():
    print " · Rock · Paper · Scissor · Lizard · Spock · "
    # 0 = Rock
    # 1 = Paper
    # 2 = Scissor
    # 3 = Lizard
    # 4 = Spock
    actions = ['rock', 'paper', 'scissor', 'lizard', 'spock']
    # Priority of actions
    strategy = {'rock'      : ['scissor', 'lizard'], 
                'paper'     : ['rock', 'spock'], 
                'scissor'   : ['paper', 'lizard'],
                'lizard'    : ['paper', 'spock'],
                'spock'     : ['rock', 'scissor']}
    compAction = actions[randint(0, 4)]
    userAction = raw_input("Choose an action:\n").lower()
    print ""
    # Invalid action given
    if userAction not in actions:
        print "You can't use that!"
        print "Try picking a different action..."
        interface()
    # User action is same as computer action
    if userAction == compAction:
        print "You draw your " + userAction + ", but the robot does the same!"
        print "Evenly matched, the battle remains inconclusive."
        print "The struggle between man and machine rages on, try again!\n"
        interface()
    # Computer beats user
    elif userAction in strategy[compAction]:
        print "You draw your " + userAction + ", but before you can do anything, the robot reveals its " + compAction + "!"
        print "The robot's " + compAction + " easily beats your " + userAction + "."
        print "It was a failure, the robot's " + compAction + " was too powerful.\n"
        playAgain()
    # User beats computer
    else: 
        print "The robot draws its " + compAction + " and begins its assault!"
        print "You smile and counter gracefully, armed with your almighty " + userAction + "."
        print "As you stand proudly over the robot, with your " + userAction + " in hand, the robot pleads mercy."
        print "'Twas a victory! You have won!\n"
        playAgain()

def playAgain():
    userChoice = raw_input("Play again? (y/n)")
    if userChoice == 'y':
        interface()

if __name__ == "__main__":
    main()
