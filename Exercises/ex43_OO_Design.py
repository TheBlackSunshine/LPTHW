# OO analysis & design walkthrough w/ text adventure game example

# 1.) Write about the problem
#   - Think up everything you can about it
#   - Draw a diagram/map or two
#   - Write yourself a series of e-mails describing the problem
# 2.) Extract key concepts
#   - List all nouns (class names) & associated verbs (function names) from #1
#   - Research the functionality you don't know
# 3.) Create a class heirarchy & object map
#   - Take your list of classes and check similarities, to identify parent class
#   - Check for duplicate functionality in classes
#   - Associate functions & add them to the tree
# 4.) Write skeleton code
#   - Classes, functions & no logic
#   - Write little test to check code works (e.g. object instantiates), more code, more tests
# 5.) Repeat & refine

# e.g. From a short story, nouns identified:
# Alien, player, Ship, Maze, Room, Scene, Gothon, Escape Pod, Planet, Map, Engine, Death, Central Corridor, Laser Weapon Armory, The Bridge

# ... generates this class heirarchy after parent/duplicate analysis
# *Map
#  - next_scene
#  - opening_scene
# *Engine
#  - play
# *Scene
#  - enter
#  *Death
#  *Central Corridor
#  *Laser Weapon Armory
#  *The Bridge
#  *Escape Pod

# ... generates this skeleton code
class Scene(object):
    
    def enter(self):
        pass
    
class Engine(object):
    
    def __init__(self, scene_map):
        pass
    
    def play(self):
        pass
    
class Death(Scene):
    
    def enter(self):
        pass
    
class CentralCorridor(Scene):
    
    def enter(self):
        pass
    
class LaserWeaponArmory(Scene):
    
    def enter(self):
        pass
    
class TheBridge(Scene):
    
    def enter(self):
        pass
    
class EscapePod(Scene):
    
    def enter(self):
        pass
    
class Map(object):
    
    def __init__(self, start_scene):
        pass
    
    def next_scene(self, scene_name):
        pass
    
    def opening_scene(self):
        pass
    
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play