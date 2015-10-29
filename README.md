# Synopsis
In BuildWars, the player first begins constructing the level platforms using four different building blocks. after the player finishes building the level, the game will start and three computer players will also spawn. The objective of the game is to jump on top of other players as often as possible to gain points. Each kill is worth 1 point. The game ends when one of the players reaches 20 points. After the game ends, the player can replay and build a new level platform.

# Code Example
BuildWars is written in Python using the PyGame API.

Some example code:

The main game loop:

```
running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_b:
                new_block = StandardBlock(DARK_GREY,50,50)
                new_block.rect.x = 300
                new_block.rect.y = 300
                standard_block_list.add(new_block)
                all_sprites.add(new_block)
```

# Motivation

What makes this game unique, is not the gameplay, but rather the fact that the player gets to build every level they play on. This allows players to express their creativity in a way that other games do not. There is something unique about designing and constructing the level you are about to play on. Therefor, the most important aspect of BuildWars is the stage building aspect. 

# Installation

In order to run BuildWars, you need to have Python 2.7 or above installed as well as PyGame packages 1.9.1.

Python Download: <a href="https://www.python.org/downloads/">Python Download</a>

PyGame Download: <a href="http://www.pygame.org/download.shtml">PyGame Download</a>

Once those are downloaded on your local machine, you can retrieve the project by opening up your command line and entering:

```git clone "https://github.com/ChapmanCPSC370/BuildWars.git" ```

Now that the project has been cloned to your machine, you can run it by opening the Python IDLE, clicking 'File'->'Open'
and selecting the stagebuilder.py script. A python script should appear and then you can click "Run"->"Run Module" to run the game.

NOTE: This process will be updated and with a more sensical manner of running the program as it is further developed

# Contributors

Garrett Olsen - garrettolsen333@gmail.com

