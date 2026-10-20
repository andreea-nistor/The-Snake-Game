# Snake Game

A snake game on a black 600×600 board. The snake moves on a 20-pixel grid, eats white food, and grows by one segment for each bite. Hitting a wall or its own tail ends the round and starts a new one.

There are two ways to play. The Python version opens a desktop window. The browser version runs in a page with Start and Stop buttons.

## How a round works

The snake starts as three segments in the middle of the board, facing right. It steps forward every 0.1 seconds.

- **Arrow keys** turn the snake up, down, left, or right.
- The snake cannot reverse into the direction it is already moving.
- The white food appears on an empty grid cell. It never lands on the snake.
- Eating the food adds 1 to the score and adds one segment at the tail.
- Segment colors cycle through red, orange, yellow, green, blue, indigo, and violet.
- If the head goes past the wall, or touches any part of the tail, the round resets. The score returns to 0, the snake shrinks back to three segments, and new food appears.
- When a round ends with a score higher than the saved high score, that score becomes the new high score.

The score line at the top of the board reads `SCORE = …   High score = …`.

## Desktop game

The desktop files are `main.py`, `snake.py`, `food.py`, `scoreboard.py`, `constants.py`, and `data.txt` in `__pycache__/scripts`.

From that folder, run:

```bash
python main.py
```

The window opens and the snake starts moving. Escape stops the game. Click the window to close it.

The high score is stored in `data.txt` next to the scripts. It stays on this computer between runs.

## Browser game

The browser files are `index.html`, `style.css`, and `game.js` in `web`.

Open `index.html` in a browser.

- **Start game** begins the round. The snake stays still until you press it.
- Click the board, then use the arrow keys.
- **Stop game** pauses the round and leaves the snake where it is.
- **Start game** again continues from that spot.
- Escape also pauses the game while the board is selected.

The high score is saved in that browser only. Another computer, or another browser, starts from 0.
