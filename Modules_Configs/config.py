# --- Modules --- #
from PIL import ImageTk, Image
import requests
import os

# --- Define Global Variable --- #
# Retries, Word, Word List, Blank List
retries = 6
gameboard_str = ""
gameboard = []
wordl = []
image_num = 0

# Window Size, Window Placement
winWidth = 600
winHeight = 400
positionx = None
positiony = None

# Windows, Widgets, Buttons List
mwin = None
gamewin = None
retry_label = None
gameboard_label = None
image_label = None
notification_label = None
button_list = []

# Word Lists
animals = ["TIGER", "LION", "GIRAFFE", "BULL", "ELEPHANT", "FOX", "CAT", "DOG", "EAGLE", "MOUSE", "SHARK", "WHALE",
           "CHEETAH", "LEOPARD", "GRASSHOPPER", "SPIDER", "SQUID", "OCTOPUS", "SNAKE", "TURTLE", "TORTOISE", "PIGEON",
           "FALCON", "CHICKEN", "COW", "PIG", "DONKEY", "HORSE"]
countries = ["INDONESIA", "MALAYSIA", "INDIA", "CHINA", "JAPAN", "FRANCE", "AUSTRALIA", "NEW ZEALAND", "CANADA",
             "UNITED STATES OF AMERICA", "ENGLAND", "IRELAND", "SINGAPORE", "THAILAND", "SOUTH KOREA", "EGYPT",
             "GREECE", "ITALY", "ZIMBABWE", "PORTUGAL", "PERU", "NEPAL", "UKRAINE", "MOZAMBIQUE", "TUVALU"]
astronomy = ["MERCURY", "VENUS", "EARTH", "MARS", "JUPITER", "SATURN", "NEPTUNE", "URANUS", "NEBULA", "THE MILKY WAY",
             "ANDROMEDA", "STAR", "MOON", "SOLAR SYSTEM", "GALAXY", "ASTEROID", "COMET", "METEORITE", "METEOR", "ORBIT",
             "OUTER SPACE", "CONSTELLATION", "PLUTO", "SUPERNOVA"]
hard_words = ["MATRIX", "HIEROGLYPHS", "RICKSHAW", "ZEPHYR", "JAZZ", "QUIZZES", "QUINTESSENTIAL", "CRYPT", "SCHIZOPHRENIA",
              "PSYCHIC", "ZIPPER", "ZILCH", "MAGNANIMOUS"]


# topics = [animals, countries, astronomy, hard_words]
topics = {
    'animals': animals, 
    'countries': countries, 
    'astronomy': astronomy, 
    'hard_words': hard_words,
    'random_words': '',
}

def get_random_word():
    response = requests.get('https://random-words-api.vercel.app/word')
    return response.json()[0]['word']

# Images
if not os.getcwd().endswith("Modules_Configs"):
    os.chdir(os.path.join(os.getcwd(), "Modules_Configs"))
else:
    pass

def images_pil():
    image_list = []
    for i in range(7):
        img = Image.open(f"Python-Hangman\\Hangman{i}.jpg").resize((50, 50))
        image_list.append(img)
    image_list.append(Image.open("Python-Hangman\\Hangman_Defeat.jpg").resize((100, 100)))
    image_list.append(Image.open("Python-Hangman\\Hangman_Victory.jpg").resize((100, 100)))
    return image_list

images_load = images_pil()

def images(images_load):
    image_list = []
    for i in images_load:
        imgTk = ImageTk.PhotoImage(i)
        image_list.append(imgTk)

    return image_list

global_img = None