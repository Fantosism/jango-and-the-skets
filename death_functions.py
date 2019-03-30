import libtcodpy as libtcod

from game_messages import Message
from game_states import GameStates


def kill_player(player):
    player.char = "%"
    player.color = libtcod.dark_red

    return Message("You is kill...", libtcod.red), GameStates.PLAYER_DEAD


def kill_monster(monster):
    death_message = Message(
        "{0} is kill by you".format(monster.name.capitalize()), libtcod.orange
    )

    monster.char = "%"
    monster.color = libtcod.dark_red
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = "remains of " + monster.name

    return death_message

