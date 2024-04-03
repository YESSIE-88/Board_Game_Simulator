#Jessie Sellars

#Importing pygame and random
import pygame, random
#Initiating pygame modules
pygame.init()

#Defining board as a pygame surface that will be used as the empty boardgame
board = pygame.Surface((1440, 720))
#Defining screen as a pygame surface that will be displayed
screen = pygame.display.set_mode((1440, 720))

#MAKING THE GRIDBOXES
#
#For loop to visit each row
for y in range(6):
    #Nested for loop to vist each columb
    for x in range(12):
        #If statement to chage the color of blocks in a stagered patern
        if x % 2 == y % 2:
            #Drawing a rectangle on the surface board with the color white at points x and y of height and width 120 pixels
            pygame.draw.rect(board, (255, 255, 255), ((x*120), (y*120), 120, 120))

#MAKING RED BOXES
#
#Defining red_box as a list of all the x position of the "go back" boxes
red_box = [2, 5, 6, 9, 8, 4]
#Making a loop that will repeat 6 times
for i in range(6):
    #Drawing red rectangles at the proper spots
    pygame.draw.rect(board, (255, 0, 0), (((red_box[i])*120), (i*120), 120, 120))

#MAKING GREEN BOXES
#
#Defining green_box as a list of all the x position of the "extra turn" boxes
green_box = [8, 9, 3, 10, 3, 7]
#Making a loop that will repeat 6 times
for i in range(6):
    #Drawing green rectangles at the proper spots
    pygame.draw.rect(board, (0, 255, 0), (((green_box[i])*120), (i*120), 120, 120))

#DRAW NUMBERS FUNCTION
#
#Defining the draw_number function that takes arguments for x, y and the string you want drawn
def draw_number(a, b, c):
    #Defining box_num as pygame text whith string counter and the color purple with a size of 18 and a font of "freesansbold.ttf"
    box_num = (pygame.font.Font("freesansbold.ttf", 18)).render(str(c), True, (144, 0, 255))
    #Making a rectangle the size of the text
    textRect = box_num.get_rect()
    #Setting the center of where the text will be drawn at the proper columb and row
    textRect.center = (((a*120)+15), ((b*120)+15))
    #Blitting the text to the surface board
    board.blit(box_num, textRect)

#DRAWING THE NUMBERS FOR EACH BOX AND MAKING A LOCATION LIST
#
#Defining the variable counter
counter = 0
#Defining the variable position
position = []
#For loop to visit each row (bottom to top)
for y in range(5, -1, -1):
    #Nested for loop to vist each columb counting up
    if y % 2 != 0:
        for x in range(12):
            counter = counter + 1
            #Using the draw number function to add the numbers to the board
            draw_number(x, y, counter)
            #Adding the cordinates of the position counter to the list
            position.append((x*120, y*120))
    else:
        for x in range(11, -1, -1):
            counter = counter + 1
            #Using the draw number function to add the numbers to the board
            draw_number(x, y, counter)
            #Adding the cordinates of the position counter to the list
            position.append((x*120, y*120))

#Defines the positions for the players and sets them to 0, 0
player_1 = 0
player_2 = 0

#REFRESH FUNCTION
#
#Defining the refresh function
def refresh():
    #Blitting the board to the screen
    screen.blit(board, (0, 0))
    #Draws the player_1 game piece at the right box
    pygame.draw.circle(screen, (0, 0, 255), (((position[player_1])[0]+30), ((position[player_1])[1]+90)), 20)
    #Draws the player_2 game piece at the right box
    pygame.draw.circle(screen, (255, 201, 14), (((position[player_2])[0]+90), ((position[player_2])[1]+30)), 20)
    #Updating the pygame window
    pygame.display.update()

#ROLL FUNCTION
#
#Defining the roll function
def roll(z):
    #Defining dice_1 and dice_2 as a random integer from 1-4
    dice_1 = random.randint(1, 4)
    dice_2 = random.randint(1, 4)
    #Printing the dice rolls
    print(f"Player {z} rolled a {dice_1} and a {dice_2}")
    return dice_1 + dice_2

refresh()

#Looping until a player wins
while True:

    #PLAYER 1 LOOP
    #
    #Setting extra as true so the loop will run
    extra = True
    while extra == True:
        pygame.time.delay(2000)
        #Adding the roll to player_1 position
        player_1 = player_1 + roll(1)
        #Checking to see if the player landed on an extra turn box
        if player_1 == 7 or player_1 == 20 or player_1 == 34 or player_1 == 44 or player_1 == 57 or player_1 == 63:
            #Printing that the player landed on an extra turn box
            print("player 1 landed on extra turn")
            #Keeping extra as true so the turn loop runs 1 more time
            extra = True
        #Eding the turn loop because the player did not land on an extra turn block
        else:
            extra = False
        #Updating the display if the player has not won
        if player_1 < 71:
            refresh()
        #Cheking to see if player_1 has landed on a move back 4 squares box
        if player_1 == 4 or player_1 == 15 or player_1 == 33 or player_1 == 41 or player_1 == 53 or player_1 == 69:
            #Printing that player_1 has landed on a move back 4 squares box
            print("player 1 landed on move back 4 boxes")
            #Subtracting 4 from the players position
            player_1 = player_1 - 4
            pygame.time.delay(2000)
            #Updating the display
            refresh()

    #Checking to see if player 1 has won
    if player_1 >= 71:
        player_1 = 71
        #Prinitng that player 1 has won
        print("player 1 wins")
        #Exiting the loop
        break

    #PLAYER 2 LOOP
    #
    #Setting extra as True so the loop will run
    extra = True
    while extra == True:
        pygame.time.delay(2000)
        #Adding the roll to player_2 position
        player_2 = player_2 + roll(2)
        #Checking to see if the player landed on an extra turn box
        if player_2 == 7 or player_2 == 20 or player_2 == 34 or player_2 == 44 or player_2 == 57 or player_2 == 63:
            #Printing that the player landed on an extra turn box
            print("player 2 landed on extra turn")
            #Keeping extra as true so the turn loop runs 1 more time
            extra = True
        #Eding the turn loop because the player did not land on an extra turn block
        else:
            extra = False
        #Updating the display if the player has not won
        if player_2 < 71:
            refresh()
        #Cheking to see if player_2 has landed on a move back 4 squares box
        if player_2 == 4 or player_2 == 15 or player_2 == 33 or player_2 == 41 or player_2 == 53 or player_2 == 69:
            #Printing that player_2 has landed on a move back 4 squares box
            print("player 2 landed on move back 4 boxes")
            #Subtracting 4 from the players position
            player_2 = player_2 - 4
            pygame.time.delay(2000)
            #Updating the display
            refresh()

    #Checking to see if player 2 has won
    if player_2 >= 71:
        player_2 = 71
        #Prinitng that player 2 has won
        print("player 2 wins")
        #Exiting the loop
        break

#Updating the display
refresh()
pygame.time.delay(5000)
