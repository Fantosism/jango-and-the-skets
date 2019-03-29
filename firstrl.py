import tdl

screen_width = 80
screen_height = 50
limit_fps = 20

console = tdl.init(screen_width, screen_height,
                   title="Jango and the Skets", fullscreen=False)

tdl.setFPS(limit_fps)

while not tdl.event.is_window_closed():
    console.draw_char(1, 1, "@", bg=None, fg=(255, 255, 255))
    tdl.flush()

playerx = screen_width//2
playery = screen_height//2


def handle_keys():
    global playerx, playery

    user_input = tdl.event.key_wait()

    # fullscreen mode
    if user_input.key == 'ENTER' and user_input.alt:
        # Alt + Enter
        tdl.set_fullscreen(not tdl.get_fullscreen())

    # Exit game
    elif user_input.key == 'ESCAPE':
        return True

    # movement keys
    if user_input.key == 'UP':
        plaery -= 1

    elif user_input.key == 'DOWN':
        player += 1

    elif user_input.key == 'LEFT':
        playerx -= 1

    elif user_input.key == 'RIGHT':
        playerx += 1
