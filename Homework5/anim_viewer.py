from pico2d import *

open_canvas()

character = load_image('sprite_sheet.png')

x = 0
y = 0
frame = 0
while (x < 800):
    clear_canvas()
    character.clip_draw(frame * 172, y * 183, 172, 172, x, 90)
    update_canvas()
    frame = (frame + 1) % 5
    if frame == 0 and y == 0:
        y = 1
    elif frame == 0 and y == 1:
        y = 0
    x += 5
    delay(0.05)
    get_events()
    

close_canvas()
