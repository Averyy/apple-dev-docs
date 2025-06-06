# Font size

**Framework**: QuickTime File Format  
**Kind**: property

An 8-bit value for the font size, expressed in points.

#### Overview

The value should always be `0.05` multiplied by the video track header height. For example, if the video track header is 720 points in height, this should be `36` (points). This size should be used in the default style record and in any per-sample style records. If a subtitle does not fit in the text box, the subtitle media handler may choose to shrink the font size so that the subtitle fits.

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
- [Font face](subtitle_sample_description/font_face.md)
  An 8-bit integer that indicates the font’s style.
- [Foreground color](subtitle_sample_description/foreground_color.md)
  A 32-bit RGBA color that specifies the text’s color, 8 bits each for red, green, blue, and alpha (transparency).
- [Font table](subtitle_sample_description/font_table.md)
  An atom that identifies the font to use to display the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/subtitle_sample_description/font_size)*