# Graphics modes

**Framework**: QuickTime File Format

QuickTime files use graphics modes to describe how one video or graphics layer should be combined with the layers beneath it.

#### Overview

Graphics modes are also known as transfer modes. Some graphics modes require a color to be specified for certain operations, such as blending to determine the blend level. QuickTime uses the graphics modes defined by Apple’s QuickDraw.

The most common graphics modes are and `ditherCopy`, which simply indicate that the image should not blend with the image behind it, but overwrite it. QuickTime also defines several additional graphics modes.

The following table lists the additional graphics modes supported by QuickTime.

| Mode | Uses opcolor | Code | Description |
| --- | --- | --- | --- |
| Copy |  | `0x0` | Copy the source image over the destination. |
| Dither copy |  | `0x40` | Dither the image (if needed), otherwise do a copy. |
| Blend | yes | `0x20` | Replaces destination pixel with a blend of the source and destination pixel colors, with the proportion for each channel controlled by that channel in the opcolor. |
| Transparent | yes | `0x24` | Replaces the destination pixel with the source pixel if the source pixel isn’t equal to the opcolor. |
| Straight alpha |  | `0x100` | Replaces the destination pixel with a blend of the source and destination pixels, with the proportion controlled by the alpha channel. |
| Premul white alpha |  | `0x101` | Premultiplied with white means that the color components of each pixel have already been blended with a white pixel, based on their alpha channel value. Effectively, this means that the image has already been combined with a white background. First, remove the white from each pixel and then blend the image with the actual background pixels. |
| Premul black alpha |  | `0x102` | Premultiplied with black is the same as pre-multiplied with white, except the background color that the image has been blended with is black instead of white. |
| Straight alpha blend | yes | `0x104` | Similar to straight alpha, but the alpha value used for each channel is the combination of the alpha channel and that channel in the opcolor. |
| Composition (dither copy) |  | `0x103` | (Tracks only) The track is drawn offscreen, and then composed onto the screen using dither copy. |

## See Also

- [Matrices](matrices.md)
  QuickTime files use matrices to describe spatial information about many objects, such as tracks within a movie.
- [RGB colors](rgb_colors.md)
  Colors stored as three consecutive unsigned 16-bit integers in the following order: red, green, blue.
- [Balance](balance.md)
  Represent balance values with 16-bit fixed-point numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/graphics_modes)*