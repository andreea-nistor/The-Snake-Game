# Plan: Play Snake on the Git Portfolio

## Goal

Keep this Python Turtle game as the desktop version, and add a browser version that runs inside a 600×600 square on the Git portfolio page. Anyone who opens the site can click the square and play. Anyone who does not want to play can scroll past it.

## What exists today

The desktop game is about 200 lines across five modules:

| File | Role |
| --- | --- |
| `main.py` | 600×600 black window, game loop, arrow keys, Escape to stop |
| `constants.py` | Grid size, speed, directions |
| `snake.py` | Rainbow segments, one turn per tick, no instant reverse, wall and tail hits |
| `food.py` | White food placed on a free cell |
| `scoreboard.py` | Score text and a high score saved in `data.txt` |

Rules worth preserving:

- Board is 600×600. Each step is 20 pixels. Walls are at 280.
- The snake starts at three segments, moving right, and ticks every 0.1 seconds.
- Arrow keys queue one turn per tick. A second key in the same tick cannot reverse the snake.
- Eating food grows the snake by one segment and adds 1 to the score. Food never appears on the snake.
- Hitting a wall or the tail resets the snake, refreshes the food, and updates the high score.
- Escape stops the game.

## Why the Python game cannot run on the portfolio as it is

A Git portfolio site (GitHub Pages or a similar static host) only serves HTML, CSS, and JavaScript. It does not run Python and it has no Turtle window. The browser page also cannot write `data.txt` next to the script.

The browser copy is a separate page that follows the same rules. The Python project stays unchanged.

## Browser version

Add a `web/` folder in this repo with three files:

- `web/index.html` — page section with one 600×600 canvas, a short line of instructions, and the script tag.
- `web/style.css` — black canvas, centered square, readable score text.
- `web/game.js` — the game.

`game.js` should keep the same numbers as `constants.py`:

- `SCREEN_WIDTH` and `SCREEN_HEIGHT`: 600
- `STEP`: 20
- `WALL_LIMIT`: 280
- `TICK_SECONDS`: 0.1
- Starting positions: `(0, 0)`, `(-20, 0)`, `(-40, 0)`
- Rainbow segment colors and white food on a black background

Map each desktop piece to the browser:

| Desktop | Browser |
| --- | --- |
| `Screen` and `Turtle` shapes | Draw squares and the food circle on a `<canvas>` |
| `while` loop and `time.sleep` | `requestAnimationFrame`, advancing one step every 0.1 seconds |
| `screen.onkey` | `keydown` on the canvas after it is clicked |
| `data.txt` | `localStorage` key such as `snake-high-score` |
| Score drawn inside the window | Same text drawn at the top of the canvas |

Behavior to match on purpose:

- One queued turn per tick, and no reversal into the opposite direction.
- Food chooses a random free cell on the 20-pixel grid.
- Wall or tail collision resets the round and saves the high score when the current score is higher.
- Escape stops the loop.

Behavior that will differ:

- The high score belongs to that browser, not to every visitor of the site. A new browser starts at 0.
- The page cannot quit the way a Turtle window can. Escape only stops the snake.

## Embedding the 600×600 square

The score is already drawn inside the 600×600 window, so the portfolio section only needs one canvas of that size.

On the portfolio page:

1. Add a section, for example "Snake", with a one-line note: click the board, then use the arrow keys. Escape stops the game.
2. Place the 600×600 canvas in that section, or load `web/index.html` in an iframe of the same size plus a little room for the instruction line.
3. Link the game script. If the game lives in this repo and the portfolio is a different repo, copy `web/` into the portfolio (for example `snake/`) or point the iframe at the deployed game URL.

Arrow keys also scroll a long page. While the canvas is focused, Up and Down must call `preventDefault` so the page stays still.

Phones have no arrow keys. The first version can be keyboard-only. On-screen direction buttons can be a follow-up if phone visitors should play too.

## Order of work

1. Create `web/index.html`, `web/style.css`, and `web/game.js` in this repo.
2. Play it locally by opening the HTML file, and check movement, growth, food placement, wall reset, tail reset, high score, and Escape.
3. Confirm the high score survives a refresh and that a lower score does not replace it.
4. Copy or link that page from the Git portfolio into a 600×600 section.
5. Deploy the portfolio and play the live page once with the keyboard, including the case where the rest of the page should not scroll.

## Out of scope for the first version

- Changing the Python Turtle game.
- A shared online high-score list.
- Touch controls.
- Accounts, a backend, or a Python server.
