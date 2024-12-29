# rubiks-py

Python simulation of a 3x3x3 Rubik's Cube.

Each side is represented by a 3x3 matrix. Various pre-determined operations can be applied to a side:

1. Set a column to the colour (anti)clockwise from the side.
2. Set a row to the colour (anti)clockwise from the side.
3. Rotate the whole side (anti)clockwise.

These operations can be applied to any of the six sides. A side is uniquely defined by its colour (Green, Red, Yellow, 
Orange, White, or Blue) and which of the overall Cube operations is attached to each of the operations.

In standard Rubik's notation, each colour side has a letter, corresponding to its position on the cube.
The default rotation of a face is clockwise by 90 degrees (a quarter turn), 
e.g. the operation L rotates the Left face - Orange - by a quarter turn clockwise.

However, in this library, we consider the effect that this L operation would have on all relevant sides.
It would cause changes to the first columns on the White, Green, and Yellow sides,
and to the third column on the Blue side. Meanwhile, the L operation also causes the Orange side to rotate by a quarter
turn (by definition).
