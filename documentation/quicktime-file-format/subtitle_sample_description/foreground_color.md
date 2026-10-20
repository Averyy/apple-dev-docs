# Foreground color

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A 32-bit RGBA color that specifies the text’s color, 8 bits each for red, green, blue, and alpha (transparency).

#### Overview

For example, this would be `(0,0,0,255)` for opaque black or `(255,255,255,255)` for opaque white. Dark colors are not recommended, as the text could be placed onto a dark background.

## See Also

### Data fields
- [Display flags](./display_flags.md)
  A 32-bit integer containing flags that describe how the subtitle text should be drawn.
- [Reserved](./reserved.md)
  An 8-bit integer.
- [Reserved](./reserved2.md)
  An 8-bit integer.
- [Reserved](./reserved3.md)
  A 32-bit integer.
- [Default text box](./default_text_box.md)
  A 64-bit rectangle that specifies an area to receive text (each 16 bits indicate top, left, bottom, and right, respectively) within the subtitle track.
- [Reserved](./reserved4.md)
  A 32-bit value.
- [Font identifier](./font_identifier.md)
  A 16-bit value that must be set to the same font identifier as in the font table.
- [Font face](./font_face.md)
  An 8-bit integer that indicates the font’s style.
- [Font size](./font_size.md)
  An 8-bit value for the font size, expressed in points.
- [Font table](./font_table.md)
  An atom that identifies the font to use to display the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/subtitle_sample_description/foreground_color)*