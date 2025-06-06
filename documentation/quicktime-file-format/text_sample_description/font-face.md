# Font face

**Framework**: QuickTime File Format  
**Kind**: property

A 16-bit integer that indicates the font’s style.

#### Overview

Set this field to `0` for normal text. You can enable other style options by using one or more of the bit masks listed in the following table.

| Value | Meaning |
| --- | --- |
| `0x0001` | Bold |
| `0x0002` | Italic |
| `0x0004` | Underline |
| `0x0008` | Outline |
| `0x0010` | Shadow |
| `0x0020` | Condense |
| `0x0040` | Extend |

## See Also

- [Display flags](text_sample_description/display_flags.md)
  A 32-bit integer containing flags that describe how the text should be drawn.
- [Text justification](text_sample_description/text_justification.md)
  A 32-bit integer that indicates how the text should be aligned.
- [Background color](text_sample_description/background_color.md)
  A 48-bit RGB color that specifies the text’s background color.
- [Default text box](text_sample_description/default_text_box.md)
  A 64-bit rectangle that specifies an area to receive text (top, left, bottom, right).
- [Reserved](text_sample_description/reserved.md)
  A 64-bit value.
- [Font number](text_sample_description/font_number.md)
  A 16-bit value.
- [Reserved](text_sample_description/reserved2.md)
  An 8-bit value.
- [Reserved](text_sample_description/reserved3.md)
  A 16-bit value.
- [Foreground color](text_sample_description/foreground_color.md)
  A 48-bit RGB color that specifies the text’s foreground color.
- [Text name](text_sample_description/text_name.md)
  A Pascal string specifying the name of the font to use to display the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/text_sample_description/font_face)*