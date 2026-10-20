# Display flags

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A 32-bit integer containing flags that describe how the subtitle text should be drawn.

#### Overview

The following flags are defined:

- **Vertical placement**: Controls vertical placement of the subtitle text. If this flag is set, the subtitle media handler uses the top coordinate of the display bounds of the override `'tbox'` text box to determine the subtitle’s vertical placement as described in [Subtitle track header size and placement](../subtitle_track_header_size_and_placement.md). Otherwise, the subtitle displays at the bottom of the video. This flag’s value is `0x20000000`.
- **Some samples are forced**: Indicates whether any subtitle samples contain forced atoms. If this flag is set, at least one sample contains a forced (`'frcd'`) atom as described in [`Subtitle sample data`](../subtitle_sample_data.md). This flag’s value is `0x40000000`.
- **All samples are forced**: If this flag is set, the subtitle media handler treats all samples as forced subtitles, regardless of the presence or absence of a `'frcd'` atom. This flag’s value is `0x80000000`. If this flag is set, the Some Samples Are Forced flag must also be set (making `0xC0000000`).

## See Also

### Data fields
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
- [Foreground color](./foreground_color.md)
  A 32-bit RGBA color that specifies the text’s color, 8 bits each for red, green, blue, and alpha (transparency).
- [Font table](./font_table.md)
  An atom that identifies the font to use to display the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/subtitle_sample_description/display_flags)*