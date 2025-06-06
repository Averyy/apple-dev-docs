# Balance

**Framework**: QuickTime File Format

Represent balance values with 16-bit fixed-point numbers.

#### Overview

Represent balance values as 16-bit, fixed-point numbers that range from `-1.0` to `+1.0`. The high-order 8 bits contain the integer portion of the value; the low-order 8 bits contain the fractional part. Negative values weight the balance toward the left speaker; positive values emphasize the right channel. Setting the balance to `0` corresponds to a neutral setting.

## See Also

- [Matrices](matrices.md)
  QuickTime files use matrices to describe spatial information about many objects, such as tracks within a movie.
- [Graphics modes](graphics_modes.md)
  QuickTime files use graphics modes to describe how one video or graphics layer should be combined with the layers beneath it.
- [RGB colors](rgb_colors.md)
  Colors stored as three consecutive unsigned 16-bit integers in the following order: red, green, blue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/balance)*