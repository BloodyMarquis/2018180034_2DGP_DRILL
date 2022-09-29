from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global frame_y
    global x, y
    global dx, dy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                if x > 40 or x < 1240:
                    dx += 1
                    frame_y = 1
                elif x <= 40 or x >= 1240:
                    dx -= 1
            elif event.key == SDLK_LEFT:
                if x > 40 or x < 1240:
                    dx -= 1
                    frame_y = 0
                elif x <= 40 or x >= 1240:
                    dx += 1
            elif event.key == SDLK_UP:
                if frame_y == 3:
                    dy += 1
                    frame_y = 1
                elif frame_y == 2:
                    dy += 1
                    frame_y = 0
            elif event.key == SDLK_DOWN:
                if frame_y == 3:
                    dy -= 1
                    frame_y = 1
                elif frame_y == 2:
                    dy -= 1
                    frame_y = 0
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dx -= 1
                frame_y = 3
            elif event.key == SDLK_LEFT:
                dx += 1
                frame_y = 2
            elif event.key == SDLK_UP:
                if frame_y == 1:
                    dy -= 1
                    frame_y = 3
                elif frame_y == 0:
                    dy -= 1
                    frame_y = 2
            elif event.key == SDLK_DOWN:
                if frame_y == 1:
                    dy += 1
                    frame_y = 3
                elif frame_y == 0:
                    dy += 1
                    frame_y = 2
    pass


open_canvas(TUK_WIDTH, TUK_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame_x = 0
frame_y = 3
dx = 0
dy = 0

while running:
    clear_canvas()
    kpu_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame_x = (frame_x + 1) % 8
    if x > 1240:
        y += dy * 5
    elif x < 40:
        y += dy * 5
    elif y > 984:
        x += dx * 5
    elif y < 40:
        x += dx * 5
    else:
        x += dx * 5
        y += dy * 5



    delay(0.01)

close_canvas()

