# Alien Invasion Game

This project is a 2D space shooter game built using the Pygame library in Python. The player controls a spaceship, trying to shoot down waves of UFOs (aliens) that descend from the top of the screen. The game tracks the player's score and includes features such as multiple lives, increasing difficulty, and a high score system.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Game Features](#game-features)
4. [How to Play](#how-to-play)
5. [Code Structure](#code-structure)
6. [Results](#results)

## Project Overview
Alien Invasion is a classic arcade-style game where you, as the player, must defend Earth from waves of UFOs. Your objective is to shoot down all the UFOs before they reach the bottom of the screen or collide with your ship. The game includes score tracking, multiple levels, and a high score feature.


## Installation 
1. Install the required Libraries:
   
   pip install pygame

2. Run the game:

   python aliean_invasion.py

## Game Features 

- Spaceship Control: Move your spaceship left or right and shoot bullets to destroy the UFOs.
- UFO Waves: Multiple waves of UFOs with increasing difficulty.
- Scoring: Earn points by shooting down UFOs, with a scoreboard to track your score.
- Lives: The player has a limited number of lives (ships). The game ends when all lives are lost.
- High Score: The game keeps track of the highest score achieved in a session.

## How to Play
- Movement: Use the left and right arrow keys to move the spaceship.
- Shooting: Press the spacebar to fire bullets.
- Start/Restart Game: Click the "Play" button with the mouse to start or restart the game.

## Code Structure

- alien_invasion.py: The main file that initializes the game and contains the main game loop.
- settings.py: Contains settings for the game such as screen size, bullet speed, and ship speed.
- gamestats.py: Tracks statistics for the game, like score, level, and number of ships left.
- scoreboard.py: Manages the display of the score, high score, and other game information.
- button.py: Handles the Play button functionality.
- ship.py: Contains the class for the player's ship, including movement and drawing it on the screen.
- bullet.py: Manages bullet behavior including firing and removing off-screen bullets.
- ufo.py: Handles the creation and movement of the UFOs, as well as checking for collisions with the ship or bullets.

## Results

The game provides an engaging experience where players can improve their scores over time. The high score feature adds a competitive element, encouraging players to beat their previous records. The game successfully combines various aspects of game development, including animation, user input handling, and collision detection, providing a fun and educational project for learning Pygame.

