# Font face

**Framework**: QuickTime File Format  
**Kind**: property

An 8-bit integer that indicates the font’s style.

#### Overview

Set this field to `0` for normal text. You can enable other style options by using one or more of the bit masks listed in the following table.

| Value | Meaning |
| --- | --- |
| `0x0001` | Bold |
| `0x0002` | Italic |
| `0x0004` | Underline |

## See Also

- [Display flags](subtitle_sample_description/display_flags.md)
  A 32-bit integer containing flags that describe how the subtitle text should be drawn.
- [Reserved](subtitle_sample_description/reserved.md)
  An 8-bit integer.
- [Reserved](subtitle_sample_description/reserved2.md)
  An 8-bit integer.
- [Reserved](subtitle_sample_description/reserved3.md)
  A 32-bit integer.
- [Default text box](subtitle_sample_description/default_text_box.md)
  A 64-bit rectangle that specifies an area to receive text (each 16 bits indicate top, left, bottom, and right, respectively) within the subtitle track.
- [Reserved](subtitle_sample_description/reserved4.md)
  A 32-bit value.
- [Font identifier](subtitle_sample_description/font_identifier.md)
  A 16-bit value that must be set to the same font identifier as in the font table.
- [Font size](subtitle_sample_description/font_size.md)
  An 8-bit value for the font size, expressed in points.
- [Foreground color](subtitle_sample_description/foreground_color.md)
  A 32-bit RGBA color that specifies the text’s color, 8 bits each for red, green, blue, and alpha (transparency).
- [Font table](subtitle_sample_description/font_table.md)
  An atom that identifies the font to use to display the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/subtitle_sample_description/font_face)*