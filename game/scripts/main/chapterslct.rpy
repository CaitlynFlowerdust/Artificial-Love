label start:
    scene black
    with fade
    centered "Welcome to {b}Artificial Love{/b}!"
    centered "Please note: this game is in {b}Alpha Testing{/b}, which means there will be bugs and errors, and incomplete story."
    centered "Please report anything you find to the {a=https://github.com/CaitlynFlowerdust/Artificial-Love}Github{/a}."
    centered "Thank you, and enjoy the game!"
    window hide
    pause 1.0
    centered "First of all, please choose a name."
    $ mc_name = renpy.input("What is your name?")
    $ mc_name = mc_name.strip()
    centered "Thank you. Now let's begin!"
    jump chapter_select
label chapter_select:
    menu chapter_screen:
        "Please select a chapter:"
        "Chapter 1: The Awakening":
            jump chapter1_start