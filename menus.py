import libtcodpy as libtcod


def menu(con, header, options, width, screen_width, screen_height):
    if len(options) > 26:
        raise ValueError("Cannot have a menu with more than 26 options")

    # calculate total height for the header (after auto-wrap) and one line per option
    header_height = libtcod.console_get_height_rect(
        con, 0, 0, width, screen_height, header
    )
    height = len(options) + header_height

    # create an off-screen console that represents the menu's window
    window = libtcod.console_new(width, height)

    # print the header, with auto-wrap
    libtcod.console_set_default_foreground(window, libtcod.white)
    libtcod.console_print_rect_ex(
        window, 0, 0, width, height, libtcod.BKGND_NONE, libtcod.LEFT, header
    )

    # print all the options
    y = header_height
    letter_index = ord("a")
    for option_text in options:
        text = "(" + chr(letter_index) + ") " + option_text
        libtcod.console_print_ex(window, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, text)
        y += 1
        letter_index += 1

    # blit the contents of the window to the root console
    x = int(screen_width / 2 - width / 2)
    y = int(screen_height / 2 - height / 2)
    libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.7)


def inventory_menu(
    con, header, inventory, inventory_width, screen_width, screen_height
):
    # show a menu with each item of the inventory as an option
    if len(inventory.items) == 0:
        options = ["Inventory is empty."]
    else:
        options = [item.name for item in inventory.items]

    menu(con, header, options, inventory_width, screen_width, screen_height)


def main_menu(con, background_image, screen_width, screen_height):
    libtcod.image_blit_2x(background_image, 0, 0, 0)

    libtcod.console_set_default_foreground(0, libtcod.light_yellow)
    libtcod.console_print_ex(
        0,
        int(screen_width / 2),
        int(screen_height / 2) - 4,
        libtcod.BKGND_NONE,
        libtcod.CENTER,
        "JANGO AND THE SKETS",
    )
    libtcod.console_print_ex(
        0,
        int(screen_width / 2),
        int(screen_height - 2),
        libtcod.BKGND_NONE,
        libtcod.CENTER,
        "By The Beej",
    )

    menu(
        con,
        "",
        ["Play a new game", "Continue last game", "Quit"],
        24,
        screen_width,
        screen_height,
    )


def message_box(con, header, width, screen_width, screen_height):
    menu(con, header, [], width, screen_width, screen_height)
