import numpy as np
import matplotlib.pyplot as plt

'''
# Chess Board
check = np.zeros((8, 8))

# Set alternating elements to 1
check[::2, 1::2] = 1
check[1::2, ::2] = 1

# Show plot
plt.title("Chess")
plt.imshow(check, cmap='gray', interpolation='nearest')
plt.show()'''

'''
# Game of The Generals Board
gotg = np.zeros((8, 8))

# Set top-half of array to 1
gotg[:4:, :] = 1

# Create a Silver colored grid
plt.grid(color='silver', linewidth=1.5)

# Show plot
plt.imshow(gotg, cmap='gray', extent=[0, 8, 0, 8])
plt.title("Game of The Generals")
plt.show()'''

# Scrabble Board
scrabble = np.zeros((15, 15))

# Triple word score
triple_word_scores = [(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7), (14, 14)]
for (i, j) in triple_word_scores:
    scrabble[i, j] = 1

# Double word score
double_word_scores = [(1, 1), (2, 2), (3, 3), (4, 4), (7, 7), (10, 10), (11, 11), (12, 12), (13, 13),
                      (1, 13), (2, 12), (3, 11), (4, 10), (10, 4), (11, 3), (12, 2), (13, 1)]
for (i, j) in double_word_scores:
    scrabble[i, j] = 3.2

# Triple letter score
triple_letter_scores = [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)]
for (i, j) in triple_letter_scores:
    scrabble[i, j] = 1.8

# Double letter score
double_letter_scores = [(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11),
                        (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11)]
for (i, j) in double_letter_scores:
    scrabble[i, j] = 4

# Set text depending on score multiplier
for i in range(15):
    for j in range(15):
        if scrabble[i, j] == 1:
            plt.text(j, i, "TW", va='center', ha='center', c='whitesmoke', fontsize='small', fontweight='bold')
        elif scrabble[i, j] == 3.2:
            plt.text(j, i, "DW", va='center', ha='center', fontsize='small', fontweight='bold')
        elif scrabble[i, j] == 1.8:
            plt.text(j, i, "TL", va='center', ha='center', fontsize='small', fontweight='bold')
        elif scrabble[i, j] == 4:
            plt.text(j, i, "DL", va='center', ha='center', fontsize='small', fontweight='bold')
        elif scrabble[i ,j] == 0:
            scrabble[i ,j] = 2.5

# Make x-axis ticks letters and show plot
xticksLabel = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
plt.imshow(scrabble, cmap='nipy_spectral', interpolation='nearest')
plt.xticks(range(0,15), xticksLabel)
plt.yticks(range(0,15))
plt.title("Scrabble")
plt.show()