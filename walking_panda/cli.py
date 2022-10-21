
from . import panda

import argparse

def cli():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate",help="Suppress Rotation",
                        action="store_true")
    parser.add_argument("--color", help="Change color",
                        action="store_true")
    parser.add_argument("--Audio", help="Change Audio",
                        action="store_true")
    parser.add_argument("--scale", help="Change scale",
                        action="store_true")
    parser.add_argument("--no_environment", help="Change environment",
                        action="store_true")
    parser.add_argument("--speed_change", help="Change speed",
                        action="store_true")
    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()