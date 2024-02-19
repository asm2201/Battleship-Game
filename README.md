# Battleship-Game <br />
A simple 'Space Invader' game recreated using pygame. <br />
Here are a few components in the game: <br />
  1. The player or the battleship <br />
  2. The enemies (max count is 6) <br />
  3. The bullets <br />
Programming logic explanation: <br />
  1. The battleship can move in only 'x direction'. Whenever it crosses the border of the screen, redraw the battleship image at the border.
  2. The battleship can shoot only one bullet at a time. The bullet must cross the top border of the pygame window to get reloaded or it must hit an enemy.
  3. There are 6 enemies that keep on getting regenerated after every collision and can move in both 'x' and 'y' direction.
  4. For every collision, the score is incremented by 10 points
  5. Collision is detected using mathematical formula for distance. (d = \sqrt{(x_2 - x_1)^2 + (y_2-y_1)^2})
  6. The game ends as soon as the enemies reach half the window's height.
