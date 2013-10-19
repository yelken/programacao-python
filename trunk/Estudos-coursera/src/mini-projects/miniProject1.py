# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"

    
def name_to_number(name):
    if number == "rock":
        return 0
    elif number == "Spock":
        return 1
    elif number == "paper":
        return 2
    elif number == "lizard":
        return 3 
    elif number == "scissors":
        return 4


def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number

    # compute random guess for comp_number using random.randrange()

    # compute difference of player_number and comp_number modulo five

    # use if/elif/else to determine winner

    # convert comp_number to name using number_to_name
    
    # print results

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


# Testing template for name_to_number()

###################################################
# Cut and paste your definition of name_to_number() here


###################################################
# Test calls to name_to_number()
print name_to_number("rock")
print name_to_number("Spock")
print name_to_number("paper")
print name_to_number("lizard")
print name_to_number("scissors")


###################################################
# Output to the console should have the form:
# 0
# 1
# 2
# 3
# 4

###################################################
# Test calls to name_to_number()
print number_to_name(0)
print number_to_name(1)
print number_to_name(2)
print number_to_name(3)
print number_to_name(4)



###################################################
# Output to the console should have the form:
# rock
# Spock
# paper
# lizard
# scissors

# always remember to check your completed program against the grading rubric
