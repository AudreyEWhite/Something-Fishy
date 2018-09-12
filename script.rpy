# Something Fishy
# A fishing game based on a concept by SquidBiscuit 

init python:
    register_stat("Oar", "oar", 0, 7, True)
    register_stat("Mutation", "mutation", 0, 100, True)
    register_stat("Fish", "fish", 0, 200, False)

    dp_period("What Now?", "next")
    dp_choice("Cast", "cast")
    dp_choice("Row", "row", show="oar > 0") #can only row if oar is available)
    #If you have an oar
    #dp_choice("Row left", "left", show="Oar > 0")
    #dp_choice("Row forward", "forward", show="Oar > 0")
    #dp_choice("Row right", "right", show="Oar > 0")
    

#Start of the game
label start:

    $ turns = 0 #initialize time passed in game

    scene black #makes background black

    jump day
            


label day:
    
    $ next = None
    $ turns += 1 #iterate time passing
    
    call screen day_planner(["What Now?"])
    window auto

    $ period = "What Now?"
    $ act = next

    call events_run_period
    call events_end_day

    jump day
    



