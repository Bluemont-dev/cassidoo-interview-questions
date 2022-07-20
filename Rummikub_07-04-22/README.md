# Rummikub Optimizer

I created this app in response to a challenge from [Cassidoo's July 4, 2022 Interview Question of the Week](https://buttondown.email/cassidoo/archive/choose-people-who-lift-you-up-michelle-obama/).

## The Challenge

From Cassidoo's newsletter:

> The game Rummikub has 106 tiles: 8 sets numbered 1-13, colored red, blue, black, and yellow, and two (2) “wildcard” tiles.
Write two functions: one that creates a new player’s tray of 14 tiles (repetitions allowed), and one that returns the valid sets from a given tray. A set can be either 3 or 4 tiles of the same number (but all different colors), or it can be a “run” (which is three or more consecutive numbers all in the same color).

To simplify the code, I changed the requirement slightly, to return the *best* sets. For example, if you could return a group of three 7's or a group of four 7's, you would return the group of 4 because it has a higher value in the game. Same for runs -- my version returns the longest run that can be built for each color. If two runs of equal length can be made from the same color, my solution returns the one with the higher tile values.

## Unit testing

I also used this challenge as an opportunity to practice unit testing in Python using Pytest. For each of the two Python files that contain the functions (create_tray.py and list_sets.py), you'll find a corresponding test file with the prefix "test_" in the filename.