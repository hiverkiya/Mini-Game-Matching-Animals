#Each animal object would be initiated two times as we need them as pairs
import os
import game_config as gc
import random
from pygame import image,transform

animals_count = dict{ (a,0) for a in gc.ASSET_FILES}

def available_animals():
    return [a for a,c in animals_count.items() if c<2]

class Animal:
    def __init__(self,index):
        