# imports. Renpy need to be specifically told to use python import statements
init python:
    import random

# Global Constants
define FISH = ["bass", "swordfish", "mackeral", "salmon", "tuna", "cod"] #array of fish

# This file contains the events that will be part of the game. 
# I may neeed to expand this to multiple files. I will decide
# the best way to do this once the file size exceeds 500 lines.


# Define characters
init:
    $ narrator = Character(' ')
    

init:
    # Simple events that will run if no more important events are available
    $ event("row", "act == 'row'", event.only(), priority=200)
    $ event("oar", "act == 'cast'", event.only(), event.random(0.1), priority=190) #receive an oar 1 in 10 times
    $ event("fish", "act == 'cast'", event.only(), priority=200)

# Character moves with no new events
label row:
    "I row forward."
    return

# Character receives an oar
label oar:
    "I've got an oar."
    $ oar += 1
    return

# Character catches a fish
label fish:
    $ caught_fish = random.sample(FISH, 1)
    "I caught a [caught_fish!q]"
    $ fish += 1
    return

    
