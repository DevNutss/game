# Dodgeball Game

## Description

The **Dodgeball Game** is a multiplayer game where two players face off in an arena, attempting to eliminate each other by shooting balls at each other. Each player can shoot, move, and rotate their paddle-like character to avoid incoming balls and strategically attack their opponent with the 4 walls.

The game is built using **Pygame**, and it includes features such as wall rebounds, ball limits, and collision detection.

This game was coded as a part of a python course assignment, so only the minimum of this game has been done.
---

## Features

- **Two-Player Mode**: 
  - Player 1 and Player 2 compete head-to-head in the same arena.
- **Ball Mechanics**:
  - Balls rebound off the walls of the arena.
  rebounding off their own paddles.
- **Dynamic Player Movement**:
  - Players can rotate their paddles to adjust the shooting angle.
  - Movement is restricted within the arena.
- **Collision System**:
  - Balls can hit opponents to reduce their lives.
  - Players lose if their lives reach zero.
- **Lives System**:
  - Players have 3 lives represented by heart icons.
  - Game over for a player triggers a game over screen and menu options.
- **Main Menu**:
  - A menu system with "Start" and "Quit" options.

---

## Controls

### Player 1
- **Move Up**: `W`
- **Move Down**: `S`
- **Rotate Left**: `A`
- **Rotate Right**: `D`
- **Shoot**: `Space`

### Player 2
- **Move Up**: `Up Arrow`
- **Move Down**: `Down Arrow`
- **Rotate Left**: `Left Arrow`
- **Rotate Right**: `Right Arrow`
- **Shoot**: `Enter`

---

## Installation and Running

1. Install **Python** (v3.8 or higher) and ensure `pip` is installed.
2. Install **Pygame**:
   ```bash
   pip install pygame

## Issues and improvements
- Players can shoot up to an unlimited amount of balls, making the game too easy - to improve
- if the ball belong to the owner it is just passing through the player rect, what could be better is making a rebound on the player
- if time a mode with multiplayer online or a training mode can be developed
- maybe if the player can move itself through the entire arena the game would be more interesting ?
