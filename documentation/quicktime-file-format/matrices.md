# Matrices

**Framework**: QuickTime File Format

QuickTime files use matrices to describe spatial information about many objects, such as tracks within a movie.

#### Overview

A transformation matrix defines how to map points from one coordinate space into another coordinate space. By modifying the contents of a transformation matrix, you can perform several standard graphics display operations, including translation, rotation, and scaling. The matrix used to accomplish two-dimensional transformations is described mathematically by a 3-by-3 matrix.

All values in the matrix are 32-bit fixed-point numbers divided as `16.16`, except for the `{u, v, w}` column, which contains 32-bit fixed-point numbers divided as `2.30`. The following figure illustrates the matrix formula QuickTime uses to transform displayed objects.

![An image that shows the matrix formula QuickTime uses to map points from one coordinate space to another. The formula shows a one row, three column matrix with the values x, y, and 1, multiplied by a three row, three column matrix, with the values a, b, and u in the first row, c, d, and v in the second row, and t subscript x, t subscript y, and w in the third row, is equal to a one row, three column matrix with the values x’, y’, and 1.](https://docs-assets.developer.apple.com/published/1bd76ba53b19faeedf2d4176439d17e4/basic-data-type-matrix%402x.png)

When you specify a matrix in a movie header atom for a movie atom, QuickTime applies the transformation from the matrix to the atoms included in the movie atom, such as a clipping atom, one or more track atoms, a user data atom, and a color table atom.

## See Also

- [Graphics modes](graphics_modes.md)
  QuickTime files use graphics modes to describe how one video or graphics layer should be combined with the layers beneath it.
- [RGB colors](rgb_colors.md)
  Colors stored as three consecutive unsigned 16-bit integers in the following order: red, green, blue.
- [Balance](balance.md)
  Represent balance values with 16-bit fixed-point numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/matrices)*