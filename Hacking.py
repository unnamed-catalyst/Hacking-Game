# Hacking
# This is a text-based password guessing game that displays a
# list of potential computer passwords. The player is allowed
# 1 attempt to guess the password. The game indicates that the
# player failed to guess the password correctly.

from uagame import Window
from time import sleep
from random import randint, choice

def main():
    location = [0,0]
    attempts_left = 4
    window = create_window()
    display_header(window, location, attempts_left)
    correct_password = display_password_list(window, location)
    guess = get_guesses(window, location, attempts_left, correct_password)
    end_game(window, location, correct_password, guess)

def create_window():
    #   Creates a 600x500 window
    window = Window("Hacking", 600, 500)
    window.set_font_name('couriernew')
    window.set_font_size(18)    
    window.set_font_color('green')
    window.set_bg_color('black')    
    return window

def display_header(window, location, attempts_left):
    #   Display a header on the top left corner of the window
    #      - window is the Window to display in
    #      - location is a list containing the x and y coords 
    #        of the strings to be displayed and it should be updated
    #        to one line below the displayed string        
    #      - attempts_left denotes the remaining guesses left
    header = ['DEBUG MODE', str(attempts_left) + ' ATTEMPT(S) LEFT', '']
    for header_line in header:
        display_line(window, header_line, location)
    
def display_line(window, string, location):
    #   Display a string in the window and update the location
    #      - window is the Window to display in
    #      - string is the String to be displayed
    #      - location is a list containing the x and y coords 
    #        of the string to be displayed and it should be updated
    #        to one line below the displayed string
    pause_time = 0.3
    string_height = window.get_font_height()    
    window.draw_string(string, location[0], location[1])
    sleep(pause_time)
    window.update()
    location[1] += string_height        
    
def display_password_list(window, location):
    #   Display a list of passwords in the window
    #      - window is the Window to display in
    #      - location is a list containing the x and y coords 
    #        of the strings to be displayed and it should be updated
    #        to one line below the displayed string    
    password_list = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 
                     'SURVIVE', 'HEARING', 'HUNTING', 'REALIZE', 'NOTHING', 
                     'OVERLAP', 'FINDING', 'PUTTING']
    for password in password_list:
        display_line(window, embed_password(password, 13), location)
    display_line(window, '', location)
    correct_password = choice(password_list)
    return correct_password
        
def embed_password(password, size):
    #   Embed password in between random symbols
    #      - password is the password to be embedded
    #      - size is the size of the whole string including both
    #        the password and the symbols
    fill = '!@#$%^&*()-+=~[]{}'
    embedding = ''
    password_size = len(password)
    split_index = randint(0, size)
    for index in range(0, split_index):
        embedding += choice(fill)
    embedding += password
    for index in range(split_index, size):
        embedding += choice(fill)
    return embedding
        
def get_guesses(window, location, attempts_left, correct_password):
    #   Get guesses for the password from the user
    #      - window is the Window to display in
    #      - location is a list containing the x and y coords 
    #        of the strings to be displayed and it should be updated
    #        to one line below the displayed string        
    #      - attempts_left denotes the remaining guesses left
    #      - correct_password is the correct password to the system
    guess = prompt_user(window, 'ENTER PASSWORD >', location)
    attempts_left -= 1
    hint_location = [0, 0]
    while attempts_left > 0 and guess != correct_password:
        display_hint(window, guess, correct_password, hint_location)
        header_location = [0, window.get_font_height()]
        display_line(window, str(attempts_left) + ' ATTEMPT(S) LEFT', header_location)
        check_warning(window, attempts_left)
        window.update()
        guess = prompt_user(window, 'ENTER PASSWORD >', location)
        attempts_left -= 1 
    return guess

def display_hint(window, guess, correct_password, location):
    #   Displays hint on the top left corner of the window based off
    #   the user's last guess
    #      - window is the Window to display in
    #      - guess is the last guess of the user
    #      - correct_password is the correct password to the system   
    #      - location is a list containing the x and y coords 
    #        of the strings to be displayed and it should be updated
    #        to one line below the displayed string
    guess_string = guess + ' INCORRECT'
    correct = 0
    index =0
    for letter in guess:
        if guess[index] == correct_password[index]:
            correct += 1    
        index += 1
    string = str(correct) + '/7 IN MATCHING POSITIONS'
    location[0] = 600 - window.get_string_width(string)
    display_line(window, guess_string, location)
    display_line(window, string, location)

def prompt_user(window, string, location):
    #   Prompts the user to enter some data
    #      - window is the Window to display in
    #      - string is the String displayed to prompt for data
    #      - location is a list containing the x and y coords 
    #        of the strings to be displayed and it should be updated
    #        to one line below the displayed string        
    string_height = window.get_font_height() 
    prompt = window.input_string(string, location[0], location[1])
    location[1] += string_height
    return prompt

def check_warning(window, attempts_left):
    #   Checks whether the user has one attempt left and displays 
    #   warning accordingly
    #      - window is the Window to display in
    #      - attempts_left denotes the remaining guesses left
    warning_message = '*** LOCKDOWN WARNING ***'
    warning_x = window.get_width() - window.get_string_width(warning_message)
    warning_y = window.get_height() - window.get_font_height()    
    if attempts_left == 1:
        window.draw_string(warning_message, warning_x, warning_y)    
    
def end_game(window, location, correct_password, guess):
    #   Reviews the user's guess and displays the outcome accordingly
    #      - window is the Window to display in
    #      - location is a list containing the x and y coords 
    #        of the strings to be displayed and it should be updated
    #        to one line below the displayed string    
    #      - correct_password is the correct password to the system
    #      - guess is the final guess of the user
    window.clear()
    outcome = []
    if guess == correct_password:
        outcome = [guess, '', 'EXITING DEBUG MODE', '', 'LOGIN SUCCESSFUL - WELCOME BACK', '']
        outcome_prompt = 'PRESS ENTER TO CONTINUE'
    else:
        outcome = [guess, '', 'LOGIN FAILURE - TERMINAL LOCKED', '', 'PLEASE CONTACT AN ADMINISTRATOR', '']
        outcome_prompt = 'PRESS ENTER TO EXIT'
    display_outcome(window, location, outcome)
    x_space = window.get_width() - window.get_string_width(outcome_prompt)
    location[0] = x_space // 2    
    prompt_user(window, outcome_prompt, location)
    window.close()

def display_outcome(window, location, outcome):
    #   Displays the outcome of the game
    #      - window is the Window to display in
    #      - location is a list containing the x and y coords 
    #        of the strings to be displayed and it should be updated
    #        to one line below the displayed string        
    #      - outcome refers to the final outcome of the game
    outcome_height = 7 * window.get_font_height()
    y_space = window.get_height() - outcome_height
    location[1] = y_space // 2        
    for outcome_line in outcome:
        x_space = window.get_width() - window.get_string_width(outcome_line)
        location[0] = x_space // 2
        display_line(window, outcome_line, location)

main()
