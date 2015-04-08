import simplegui

time = 0
wins = 0
tries = 0
semaphore = False

def format(t):
    seconds_n_f = t/10
    seconds = seconds_n_f%60
        
    one_tenth = t%10
    one_tenth = str(one_tenth)
    
    minutes = seconds_n_f/60
    
    if int(seconds)<10:
        seconds = str(seconds)
        seconds = "0" + seconds
        
        
    minutes = str(minutes)
    seconds = str(seconds)
    
    return minutes + ":" +seconds + "." + one_tenth

def button_start():
    global semaphore
    timer.start()
    semaphore = True
    
def button_stop():
    global wins, tries, semaphore
    timer.stop()
    if(semaphore):
        if(time%10 ==0):
            wins+=1
        tries += 1
    semaphore = False

def button_reset():
    global wins, tries, time
    wins = 0
    tries = 0
    time = 0
    
def tick():
    global time
    time +=1
    
def draw_handler(canvas):
    canvas.draw_text(format(time), [50,100], 40, "White")
    canvas.draw_text(str(wins), [140, 20], 24, "Yellow")
    canvas.draw_text("/", [170, 20], 24, "Yellow")
    canvas.draw_text(str(tries), [185, 20], 24, "Yellow")
    
frame = simplegui.create_frame("Stopwatch!", 210, 200)

timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw_handler)
start = frame.add_button("Start", button_start, 100)
stop = frame.add_button("Stop", button_stop, 100)
reset = frame.add_button("Reset", button_reset, 100)

frame.start()
