# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH/2, HEIGHT/2] 
score1 = 0
score2 = 0
ball_vel = [0,0]
paddle1_pos = HEIGHT/2
paddle2_pos= HEIGHT/2
paddle1_vel = paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists   
    ball_pos = [WIDTH/2, HEIGHT/2]
    
    x = random.randrange(120, 240)/60.0
    y = random.randrange(60, 180)/60.0
    
    if direction == RIGHT:
        ball_vel[0] = x
        ball_vel[1] = -y
    if direction == LEFT:
        ball_vel[0] = -x
        ball_vel[1] = -y

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global LEFT, RIGHT
    
    dir = random.randrange(1,3) #random direction to spawn after reset or after first start
    if dir == 1:
        spawn_ball(LEFT)
    elif dir == 2:
        spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel #2 ostatnie usunac
            
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 2, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White")
       
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if paddle1_pos <= HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    elif paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    if paddle2_pos <= HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    elif paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
        
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos+HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, paddle1_pos-HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT],[WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    
    # determine whether paddle and ball collide    
    #left paddle wins
    if (ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS) and ((ball_pos[1] > paddle2_pos + HALF_PAD_HEIGHT) or (ball_pos[1] < paddle2_pos - HALF_PAD_HEIGHT)):
        score1 += 1
        spawn_ball(LEFT)
    elif (ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS):
        ball_vel[0] = -(1.1)*ball_vel[0]
    #right paddle wins
    if (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS) and ((ball_pos[1] > paddle1_pos + HALF_PAD_HEIGHT) or (ball_pos[1] < paddle1_pos - HALF_PAD_HEIGHT)):
        score2 += 1
        spawn_ball(RIGHT)
    elif (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS):
        ball_vel[0] = -(1.1)*ball_vel[0]
    
    # draw scores
    canvas.draw_text(str(score1), (215, 100), 50, 'White')
    canvas.draw_text(str(score2), (360, 100), 50, 'White')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 4
    
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
        
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
  
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"] or simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"] or simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

def button_handler():
    global score1, score2
    score1 = 0
    score2 = 0
    new_game()
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background('Black') #by default
button1 = frame.add_button('Restart', button_handler, 100)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
