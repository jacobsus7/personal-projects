COAL = 500
DIST = 800
STEP = 100

WIDTH = 700
HEIGHT = 500

bg = color(95, 39, 156)

# preliminary stuff
margin = 0.15
track_length = (1-margin)*WIDTH
n = (DIST/STEP)+1
gap = (track_length)/(n-1)
track_start = (WIDTH/2)-(track_length/2)
sections = [0]*n
for i in range(0,n):
    sections[i] = track_start+gap*i
    
coal_ind = [0]*n

curr_ind = 0

class Train():

    def __init__(self, coal_used = 0, coal = COAL):
        self.coal_used = coal_used
        self.coal = coal
        
    def move(self, distance):
        self.coal_used += abs(distance)
        self.coal -= abs(distance)
        
    def drop_coal(self, amount):
        self.coal -= amount
    
    def add_coal(self, amount):
        self.coal += amount

        
# instantiate the train   
train = Train() 

def setup():
    
    size(WIDTH, HEIGHT)
    colorMode(RGB)
    background(bg)
    noStroke()
    rectMode(CENTER)
    
    # text stuff
    f = createFont("Arial", 16, True)
    textFont(f,36)
    textAlign(CENTER)
    
    #horizontal rectangle
    fill(255,255,255)
    rect(WIDTH/2,HEIGHT/2, track_length, 20)
    
    
    #vertical track sections
    for i in range(0,n):
        fill(255,255,255)
        rect(sections[i], HEIGHT/2, 20, 80) #hard coded track sizes for now
        
# score = loadStrings("high_score.txt")

game_over = False

def draw():
    
    clear_screen()
    draw_train()
    if curr_ind == 0 and train.coal < COAL:
        train.coal = 500
    
    # fill(255,255,255)
    # textAlign(LEFT)
    # text("High Score:" + '\n' + str(score), 10, 30)
    # textAlign(CENTER)
    
    if train.coal <= STEP:
        fill(255,0,0)
    else: 
        fill(255,255,255)
    text(str(train.coal),sections[curr_ind],HEIGHT/2 - 115)
    
    fill(255,255,255)
    text("Coal Used:"+'\n'+str(train.coal_used), WIDTH/2, HEIGHT-80)
    
    for c in range(1,n):
        amt = coal_ind[c]
        if  amt != 0:
            draw_coal(c)
            amt_str = str(amt*STEP)
            fill(255,255,255)
            text(amt_str,sections[c],HEIGHT/2+ 125)
    
    #check win/lose conditions
    
    # LOSE
    if train.coal <= 0 and curr_ind != n-1 and coal_ind[curr_ind] <= 0:
        # fill(bg)
        # rectMode(CORNERS)
        # rect(0,0,WIDTH,HEIGHT)
        
        fill(255)
        text("GAME OVER", WIDTH/2, HEIGHT/2)
        #game_over = True
        
        refresh()
        setup()
        
    elif curr_ind == n-1:
        text("YOU WIN!", WIDTH/2, 80)

def refresh():
    global curr_ind
    global coal_ind
    clear_screen()
    train.coal = COAL
    train.coal_used = 0
    curr_ind = 0
    coal_ind = [0]*n
    
def move_train(val):
    #train only moves as much as STEP value
    train.move(val)
    
def draw_train():
    rectMode(CENTER)
    fill(60,50,40)
    rect(sections[curr_ind],HEIGHT/2 - 80, 75, 35)

def clear_screen():
    rectMode(CORNERS)
    fill(bg)
    rect(0,0,WIDTH,HEIGHT/2-60) #cover up prev train
    fill(bg)
    rect(0,HEIGHT/2+40,WIDTH, HEIGHT)
    
def draw_coal(ind):
    fill(0,0,0)
    ellipse(sections[ind], HEIGHT/2 + 70, 25,25)
    
# def erase_coal(ind):
#     fill(bg)
#     ellipse(sections[ind], HEIGHT/2 +70 , 26,26)
    
def keyPressed():
    if not game_over:
        
        global curr_ind
        if (key == CODED):

            # pick up coal 
            if keyCode == UP:
                if coal_ind[curr_ind] > 0 and train.coal < COAL:
                    train.add_coal(STEP)
                    coal_ind[curr_ind] -= 1
                    # if coal_ind[curr_ind] == 0:
                    #     erase_coal(curr_ind)
            
            # drop coal
            elif keyCode == DOWN:
                if train.coal > 0:
                    train.drop_coal(STEP)
                    # if coal_ind[curr_ind] == 0:
                    #     draw_coal(curr_ind)
                    coal_ind[curr_ind] += 1    
            
            # move right
            elif keyCode == RIGHT:
                if train.coal > 0:
                    move_train(STEP)
                    curr_ind += 1
                    # clear_screen()
                    # draw_train()

            
            # move left
            elif keyCode == LEFT:
                if train.coal > 0 and curr_ind > 0:
                     move_train(STEP)
                     curr_ind -= 1
                     # clear_screen()
                     # draw_train()
