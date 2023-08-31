import pgzrun
import random

WIDTH = 1000
HEIGHT = 700

mario = Actor("mario" , (500 , 350))
over = Actor("over" , (500 , 350))
gameAgain = Actor("gameagain" , (100 , 600))
gharch = Actor("gharch" , (random.randint(100,900) , random.randint(100,600)))
enemy = Actor("enemy" , (random.randint(100,900) , random.randint(100,600)))
score = 0
gameOver = False

def update():
    global score , gameOver

    gharch.angle += 5

    if keyboard.up and mario.y >= 100:
        mario.y -= 2
    elif keyboard.down and mario.y <= 600:
        mario.y += 2
    elif keyboard.right and mario.x <= 900:
        mario.x += 2
    elif keyboard.left and mario.x >= 100:
        mario.x -= 2

    if mario.colliderect(gharch):
        gharch.pos = random.randint(100,900) , random.randint(100,600)
        enemy.pos = random.randint(100,900) , random.randint(100,600)
        score += 1
    
    if mario.colliderect(enemy):
        gameOver = True


def draw():
    global game
    def game():
        screen.fill("white")
        mario.draw()
        gharch.draw()
        enemy.draw()
        screen.draw.text(f"{score}",color="black",topleft=(50,50),fontsize=50,fontname="digital")
    game()

    if gameOver == True:
        over.draw()
        gameAgain.draw()
        screen.draw.text(f"{score}",color="white",topleft=(50,50),fontsize=50,fontname="digital")

def on_mouse_down(pos):
    global gameOver , score , game

    if gameOver == True and gameAgain.collidepoint(pos):
        gameOver = False
        enemy.pos = random.randint(100,900) , random.randint(100,600)
        score = 0
        game()

pgzrun.go()