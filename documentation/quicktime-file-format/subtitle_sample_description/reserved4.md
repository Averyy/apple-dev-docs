# Reserved

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A 32-bit value.

#### Overview

This must be set to `0`.

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
- [Font identifier](./font_identifier.md)
  A 16-bit value that must be set to the same font identifier as in the font table.
- [Font face](./font_face.md)
  An 8-bit integer that indicates the font’s style.
- [Font size](./font_size.md)
  An 8-bit value for the font size, expressed in points.
- [Foreground color](./foreground_color.md)
  A 32-bit RGBA color that specifies the text’s color, 8 bits each for red, green, blue, and alpha (transparency).
- [Font table](./font_table.md)
  An atom that identifies the font to use to display the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/subtitle_sample_description/reserved4)*