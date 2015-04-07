# implementation of card game - Memory

import simplegui
import random

lst = []
exposed = []
x_pos = 7 #position for drawing text
offset = 0 #position for drawing filled rectangles
turns = 0

# helper function to initialize globals
def new_game():
    global lst, state, turns
    state = 0
    turns = 0
    label.set_text("Turns = 0")
    
    list1 = range(0,8)
    list2 = range(0,8)
    lst = list1 + list2
    random.shuffle(lst)
    
    #on start every card isn't exposed
    if len(exposed) == 0:
        for x in lst:
            exposed.append(False)
    
    #reset, every card isn't exposed
    for x in exposed:
        exposed[exposed.index(x)] = False    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, stan0, lst, stan1, turns
    act_pos =  list(pos)
    index_s_o = 0
    
    #ignoring mouseclick when card is exposed
    if not exposed[act_pos[0] / 50]: 
    
        if state == 0:
            stan0 = act_pos[0] / 50
            if act_pos[0] > 0 and act_pos[0] < 800:
                exposed[stan0] = True
                turns += 1
            state = 1
        elif state == 1:
            stan1 = act_pos[0] / 50
            if not exposed[stan1]:
                exposed[stan1] = True                  
                state = 2
        else:             
            if lst[stan0] != lst[stan1]:
                exposed[stan0] = False
                exposed[stan1] = False

            stan0 = act_pos[0] / 50
            if not exposed[stan0]:
                exposed[stan0] = True
                turns += 1
                state = 1
        
        label.set_text("Turns = " + str(turns))
                      
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, x_pos, offset, i
    x_pos = 7
    offset = 0
    i = 0
    
    for val in exposed:    
        if val:        
            canvas.draw_text(str(lst[i]), [x_pos, 70], 40, 'White')
                     
        else:
            canvas.draw_line((24 + offset, 0), (24 + offset, 100), 48, 'Green')
        
        x_pos+= 50
        offset += 50
      
        if i < 15:
            i += 1


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric