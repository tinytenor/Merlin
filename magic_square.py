from dearpygui.core import *
from dearpygui.simple import *
from random import randrange


#declare global vars====================================================================================================
click_count = 0
board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]


#changes the color of buttons===========================================================================================
def update_ui():
    true = [255, 0, 0, 255]
    true_hover = [255, 100, 100, 255]
    false = [0, 255, 0, 255]
    false_hover = [100, 255, 100, 255]
    global click_count

    set_item_label("click_lbl", "Clicks: " + str(click_count))
    hide_item("win_lbl")

    for i in range(9):
        if board[i] == 1:
            set_item_color("b" + str(i), mvGuiCol_Button, color=true)
            set_item_color("b" + str(i), mvGuiCol_ButtonHovered, color=true_hover)
        else:
            set_item_color("b" + str(i), mvGuiCol_Button, color=false)
            set_item_color("b" + str(i), mvGuiCol_ButtonHovered, color=false_hover)

    if check_win():
        show_item("win_lbl")
        set_item_color("Merlin Magic Square", mvGuiCol_WindowBg, color=[0, 0, 255, 255])
    else:
        set_item_color("Merlin Magic Square", mvGuiCol_WindowBg, [0, 0, 0, 255])


#generates new board and unlocks it=====================================================================================
def new_game():
    global click_count
    click_count = 0
    for i in range(9):
        board[i] = randrange(0, 2)
        update_ui()


#checks to see if the board is locked then sends list to flip_buttons()=================================================
def make_move(list):
    if not check_win():
        global click_count
        click_count += 1
        flip_buttons(list)
        check_win()
        update_ui()


#flips the color of the targeted squares depending on the button========================================================
def flip_buttons(list):
    for i in range(9):
        if list[i] == 1:
            if board[i] == 0:
                board[i] = 1
            else:
                board[i] = 0


def check_win():
    if board == [0, 0, 0,
                 0, 1, 0,
                 0, 0, 0]:
        return True
    else:
        return False


#button callbacks. 1s in the array are the buttons that get changed when that button is clicked.========================
def b0_cb():
    make_move([1, 1, 0,
               1, 1, 0,
               0, 0, 0])


def b1_cb():
    make_move([1, 1, 1,
               0, 0, 0,
               0, 0, 0])


def b2_cb():
    make_move([0, 1, 1,
               0, 1, 1,
               0, 0, 0])


def b3_cb():
    make_move([1, 0, 0,
               1, 0, 0,
               1, 0, 0])


def b4_cb():
    make_move([0, 1, 0,
               1, 1, 1,
               0, 1, 0])


def b5_cb():
    make_move([0, 0, 1,
               0, 0, 1,
               0, 0, 1])


def b6_cb():
    make_move([0, 0, 0,
               1, 1, 0,
               1, 1, 0])


def b7_cb():
    make_move([0, 0, 0,
               0, 0, 0,
               1, 1, 1])


def b8_cb():
    make_move([0, 0, 0,
               0, 1, 1,
               0, 1, 1])


#calls new game function================================================================================================
def new_game_cb():
    new_game()


#configure gui==========================================================================================================
with window("Merlin Magic Square"):
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
    add_button("b_new_game", label="New Game", width=button_x, callback=new_game_cb)
    add_label_text("click_lbl", label="Clicks: ")
    add_label_text("win_lbl", label="Win!")


#update button colors before launching window===========================================================================
update_ui()
#setting button 4 to red to show win condition without triggering check_win()===========================================
set_item_color("b4", mvGuiCol_Button, color=[255, 0, 0, 255])
set_item_color("b4", mvGuiCol_ButtonHovered, color=[255, 100, 100, 255])
start_dearpygui(primary_window="Merlin Magic Square")
