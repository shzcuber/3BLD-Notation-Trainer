#!/usr/bin/env python3

from termcolor import colored
import time
import random
import copy

U_FACE = [['A', 'A', 'B'],
          ['D', ' ', 'B'],
          ['D', 'C', 'C']]

L_FACE = [['E', 'E', 'F'],
          ['H', ' ', 'F'],
          ['H', 'G', 'G']]

F_FACE = [['I', 'I', 'J'],
          ['L', ' ', 'J'],
          ['L', 'K', 'K']]

R_FACE = [['M', 'M', 'N'],
          ['P', ' ', 'N'],
          ['P', 'O', 'O']]

B_FACE = [['S', 'S', 'T'],
          ['R', ' ', 'T'],
          ['R', 'Q', 'Q']]

D_FACE = [['U', 'U', 'V'],
          ['X', ' ', 'V'],
          ['X', 'W', 'W']]


NULL_FACE = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

def create_empty_face(letter):
    return  [['0', '0', '0'],
             ['0', letter, '0'],
             ['0', '0', '0']]

DISPLAY_CUBE = [
    [NULL_FACE, create_empty_face(colored('B', 'blue', attrs=['bold']))],
    [NULL_FACE, create_empty_face(colored('U', 'yellow'))],
    [create_empty_face(colored('L', 'red')), create_empty_face(colored('F', 'green')), create_empty_face(colored('R', 'yellow', attrs=['bold']))],
    [NULL_FACE, create_empty_face(colored('D', 'white'))],
]

DISPLAY_CUBE_FACE_OPTIONS = {
    (0, 1): B_FACE,
    (1, 1): U_FACE,
    (2, 0): L_FACE,
    (2, 1): F_FACE,
    (2, 2): R_FACE,
    (3, 1): D_FACE
}

CORNER_LOCATIONS = [(0, 0), (0, 2), (2, 0), (2, 2)]
EDGE_LOCATIONS   = [(0, 1), (1, 0), (2, 1), (1, 2)]

# face choice: any of the keys in DISPLAY_CUBE_FACE_OPTIONS
# face location: any tuple representing locations on the face
def print_cube(face_choice, face_location):
    MODIFIED_DISPLAY_CUBE = copy.deepcopy(DISPLAY_CUBE)
    MODIFIED_DISPLAY_CUBE[face_choice[0]][face_choice[1]][face_location[0]][face_location[1]] = colored('*', 'red')
    for face_array in MODIFIED_DISPLAY_CUBE:
        for row in range(0, 3):
            for face in face_array:
                for col in range(0, 3):
                    print(face[row][col], end=" ")
                print(end=" ")
            print()
        print()

def main():
    print("Do you want to practice corners (c), edges (e), or both (b)?")
    correct_answers = 0
    incorrect_answers = 0

    # loop until we get c e or b as input
    while True:
        mode = input()
        if(mode=='c' or mode=='e' or mode=='b'): break

    # game loop
    while True:
        answer_face = random.choice(list(DISPLAY_CUBE_FACE_OPTIONS.keys()))
        answer_location = None
        # pick either c or e randomly if mode is both
        current_mode = mode if mode!='b' else random.choice(['c', 'e'])
        if current_mode=='c':
            answer_location = random.choice(CORNER_LOCATIONS)
        elif current_mode=='e':
            answer_location = random.choice(EDGE_LOCATIONS)

        start_time = time.time()
        print_cube(answer_face, answer_location)

        answer = DISPLAY_CUBE_FACE_OPTIONS[answer_face][answer_location[0]][answer_location[1]]
        letter_guess = input("input your guess, type exit to exit, or type switch to switch to a different mode\n")
        if letter_guess.lower()==answer.lower():
            print(colored("yessir", "green"))
            correct_answers+=1
        elif letter_guess=="exit":
            break
        elif letter_guess=="switch":
            main()
        else:
            print(colored("no ur wrong the answer is", "red"), colored(answer, "cyan"))
            incorrect_answers+=1

        print("correct answers:", colored(correct_answers, "green"))
        print("incorrect answers:", colored(incorrect_answers, "red"))
        print("time elapsed:", f'{time.time()-start_time:.1f} seconds')
        time.sleep(0.75)

if __name__ == '__main__':
    main()
