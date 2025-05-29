# Snake Game with Pygame

A classic Snake game implemented in Python using Pygame, designed with Object-Oriented Programming principles and clean code. This project features a retro-style brown and green checkerboard background, smooth gameplay, and an intuitive interface with pause/start and restart after game over.

---

## Features

- Classic Snake gameplay.
- Object-Oriented design for maintainability.
- Clean, well-documented code with English docstrings.
- Retro-style brown checkerboard background with green borders.
- Snake and food cells smaller than background squares for a neat contour effect.
- Game starts after a key press.
- Displays "Game Over" message without closing the window.
- Option to restart the game after losing.
- Responsive controls and smooth animations.

---

## Requirements

- Python 3.7 or newer
- [Pygame](https://www.pygame.org/news)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/snake-pygame.git
cd snake-pygame

2. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install pygame
```

---

## Project Structure

```
snake-pygame/
│
├── game.py          # Main game script to run the game
├── snake.py         # Snake class and related logic
├── food.py          # Food class and related logic
├── settings.py      # Settings to run snake game
├── main.py          # Run game code
└── README.md        # This file
```

---

## How to Run

Run the main game script:

```bash
python main.py
```

* The game will start with a black screen and the message:

  > *Press any key to start*

* Use arrow keys or WASD to control the snake.

* Eat the white food to grow.

* Avoid hitting walls or the snake’s own body.

* When the game ends, a *Game Over* message appears.

* Press **R** to restart.

---

## Contribution

Feel free to fork the repository, open issues or submit pull requests to improve the game!

---

## License

This project is open source and available under the MIT License.

---

Enjoy playing the classic Snake game!
