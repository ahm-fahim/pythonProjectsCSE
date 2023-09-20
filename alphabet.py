import tkinter as tk
import random
import pygame

# Initialize pygame for playing sounds
pygame.mixer.init()

# Define the alphabet letters, corresponding colors, and sounds
alphabet_data = {
    'A': {'color': 'red', 'sound': 'a.mp3'},
    'B': {'color': 'blue', 'sound': 'b.mp3'},
    'C': {'color': 'green', 'sound': 'c.mp3'},
    # Add more letters and their data here
}

# Create a function to start the game
def start_game():
    global alphabet_data
    # Shuffle the alphabet keys to randomize the order
    alphabet_keys = list(alphabet_data.keys())
    random.shuffle(alphabet_keys)
    
    # Get the next letter from the shuffled list
    current_letter = alphabet_keys[0]
    
    # Update the GUI elements
    letter_label.config(text=current_letter)
    color_label.config(bg=alphabet_data[current_letter]['color'])
    
    # Play the sound for the current letter
    sound_file = alphabet_data[current_letter]['sound']
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

# Create the main window
root = tk.Tk()
root.title("Alphabet Learning Game")

# Create a label to display the alphabet letter
letter_label = tk.Label(root, text="", font=("Arial", 48))
letter_label.pack(pady=20)

# Create a label to display the color
color_label = tk.Label(root, text="", font=("Arial", 36), width=15, height=2)
color_label.pack(pady=10)

# Create a button to start the game
start_button = tk.Button(root, text="Start", command=start_game)
start_button.pack()

# Start the game when the application is launched
start_game()

# Run the main loop
root.mainloop()

