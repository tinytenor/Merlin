from dearpygui.core import *
from dearpygui.simple import *


class Button:
    def __init__(self, ident, state):
        self.ident = ident
        self.state = state


b0 = Button("b0", False)


if not b0.state:
    pass


def b0_cb():
    pass


def b1_cb():
    pass


def b2_cb():
    pass


def b3_cb():
    pass


def b4_cb():
    pass


def b5_cb():
    pass


def b6_cb():
    pass


def b7_cb():
    pass


def b8_cb():
    pass


def new_game_2p_cb():
    pass


def new_game_1p_cb():
    pass


with window("Tic Tac Toe"):
    set_main_window_size(278, 450)
    button_x = 75
    button_y = 75
    add_button("b0", label="", width=button_x, height=button_y, callback=b0_cb)
    add_same_line(spacing=10)
    add_button("b1", label="", width=button_x, height=button_y, callback=b1_cb)
    add_same_line(spacing=10)
    add_button("b2", label="", width=button_x, height=button_y, callback=b2_cb)
    add_button("b3", label="", width=button_x, height=button_y, callback=b3_cb)
    add_same_line(spacing=10)
    add_button("b4", label="", width=button_x, height=button_y, callback=b4_cb)
    add_same_line(spacing=10)
    add_button("b5", label="", width=button_x, height=button_y, callback=b5_cb)
    add_button("b6", label="", width=button_x, height=button_y, callback=b6_cb)
    add_same_line(spacing=10)
    add_button("b7", label="", width=button_x, height=button_y, callback=b7_cb)
    add_same_line(spacing=10)
    add_button("b8", label="", width=button_x, height=button_y, callback=b8_cb)
    add_button("b_new_game2", label="New Game - two players", width=button_x * 3, callback=new_game_2p_cb)
    add_button("b_new_game1", label="New Game - one player", width=button_x * 3, callback=new_game_1p_cb)
    add_label_text("win_lbl", label="")


start_dearpygui(primary_window="Tic Tac Toe")
