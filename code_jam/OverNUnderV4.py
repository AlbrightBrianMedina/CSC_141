# Buttons
from random import randint
import pygame

pygame.init()
#setting up the main game's borders, text/visual, global default settings
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 48)
text_font = pygame.font.SysFont("Arial.tff", 60)
pygame.display.set_caption("Over N' Under!")
button1_enabled = True
new_press = True

#define the functions to be used for the game
def draw_text(text, sfont, text_col, x, y):
    img = sfont.render(text, True, text_col)
    screen.blit(img, (x, y))


class MyButton:
    def __init__(self, text, x_pos, y_pos, width, height, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.enabled = enabled

    def draw(self):
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        if self.enabled:
            if self.check_click():
                pygame.draw.rect(screen, 'dark gray', button_rect, 0, 5)
            else:
                pygame.draw.rect(screen, 'light gray', button_rect, 0, 5)
            # else:
            #     pygame.draw.rect(screen, 'black', button_rect, 0, 5)
        pygame.draw.rect(screen, 'black', button_rect, 2, 5)
        screen.blit(button_text, (self.x_pos + 3, self.y_pos + 3))

    def check_click(self): #checks if button is clicked by comparing the mouse clicked positions
        pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        if left_click and button_rect.collidepoint(pos) and self.enabled:
            return True
        else:
            return False
        
#defining these variables into global integers 
computer_pick = 0 
player_pick = 0
run = True

#what to do when the Over button is selected
def over_clicked():
    global run  #do this at beginning of functions
    screen.fill('white')  #sets up the border for the next screen
    if player_pick > computer_pick:
        draw_text(f'You Win', text_font, 'black', 30, 50)
    elif player_pick < computer_pick:
        draw_text(f'You Lose', text_font, 'black', 30, 50)
    elif player_pick == computer_pick:
        draw_text(f'Tie', text_font, 'black', 30, 50)
  
#additional text for the results screen   
    draw_text(f"First number: {computer_pick}", text_font, 'black', 30, 100)
    draw_text(f"Second number: {player_pick}", text_font, 'black', 30, 150 )
    draw_text(f"Try Again?", text_font, 'black', 30, 200)

    yes_button = MyButton('Yes', 180, 350, 100, 60, True)
    no_button = MyButton('No', 180, 420, 100, 60, True)
    yes_button.draw()
    no_button.draw()
#Make a secondary loop AFTER display.flip() AND THEN set up what the next event is and when to do event    
    pygame.display.flip() #updates screen to show what it currently looks like
    while True:
        event = pygame.event.wait()
        while event.type != pygame.MOUSEBUTTONDOWN and event.type != pygame.QUIT:
            event = pygame.event.wait()

        if event.type == pygame.QUIT or no_button.check_click():
            run = False
            return
        if yes_button.check_click():
            return      

#what to do when the Under button is selected
def under_clicked():
    global run  #do this at beginning of functions
    screen.fill('white') #sets up border for the next screen
    if player_pick < computer_pick:
        draw_text(f'You Win', text_font, 'black', 30, 50)
    elif player_pick > computer_pick:
        draw_text(f'You Lose', text_font, 'black', 30, 50)
    elif player_pick == computer_pick:
        draw_text(f'Tie', text_font, 'black', 30, 50)
  
#additional text for the results screen   
    draw_text(f"First number: {computer_pick}", text_font, 'black', 30, 100)
    draw_text(f"Second number: {player_pick}", text_font, 'black', 30, 150 )
    draw_text(f"Try Again?", text_font, 'black', 30, 200)

    yes_button = MyButton('Yes', 180, 350, 100, 60, True)
    no_button = MyButton('No', 180, 420, 100, 60, True)
    yes_button.draw()
    no_button.draw()
#Make a secondary loop AFTER display.flip() AND THEN set up what the next event is and when to do event    
    pygame.display.flip()
    while True:
        event = pygame.event.wait()
        while event.type != pygame.MOUSEBUTTONDOWN and event.type != pygame.QUIT:
            event = pygame.event.wait()

        if event.type == pygame.QUIT or no_button.check_click():
            run = False
            return
        if yes_button.check_click():
            return      
    

#when the game is turned on
def main():
    global computer_pick, player_pick, run
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        if not run:
            break

        #mouse_pos = pygame.mouse.get_pos()
        timer.tick(fps)

        computer_pick = randint(1, 21)
        player_pick = randint(1, 21)

        screen.fill('white')

        draw_text("Make your choice!", text_font, (0, 0, 0), 60, 100)
        draw_text("The CPU landed on", text_font, (0, 0, 0), 50, 180)
        draw_text(f"{computer_pick}", text_font, (0, 0, 0), 217, 250)
        draw_text("Place Your Bet", text_font, (0, 0, 0), 100, 300)

        over_button = MyButton('Over', 180, 350, 120, 60, True)
        under_button = MyButton('Under', 165, 420, 150, 60, True)

        over_button.draw()
        under_button.draw()
        pygame.display.flip()
        while True:

            event = pygame.event.wait()
            while event.type != pygame.MOUSEBUTTONDOWN and event.type != pygame.QUIT:
                event = pygame.event.wait()

            if event.type == pygame.QUIT:
                run = False
                break

            if over_button.check_click():
                print("Over button clicked")
                over_clicked()
                break

            elif under_button.check_click():
                print("Under button clicked")
                under_clicked()
                break

            # this is when you press down left click AND when you unpress left click
            #    if pygame.mouse.get_pressed()[0] and new_press:
            #        new_press = False
            #        print("IT works")
            #    if not pygame.mouse.get_pressed()[0] and not new_press:
            #        new_press = True
            #        print("This also works")

    pygame.quit()

if __name__ == "__main__":
    main()