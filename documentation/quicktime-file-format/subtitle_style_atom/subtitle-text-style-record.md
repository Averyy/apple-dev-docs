# Subtitle text style record

**Framework**: QuickTime File Format  
**Kind**: property

One or more records that provide details about the subtitle’s style.

#### Overview

One record consists of the following fields.

- **Start character**: A 16-bit value that is the offset of the first character that is to use the style specified in this record. Zero (`0`) is the first character in the subtitle.
- **End character**: A 16-bit value that is the offset of the character that follows the last character to use this style.
- **Font identifier**: A 16-bit value that must be set to the same font identifier as in the font table (`'ftab'` extension).
- **Font face**: An 8-bit integer that indicates the font’s style. Set this field to `0` for normal text. You can enable other style options by using one or more of the bit masks listed in Text.
- **Font size**: An 8-bit value that specifies the font’s size. See [`Subtitle sample description`](subtitle_sample_description.md) for more information.
- **Foreground color**: A 32-bit RGBA color that specifies the text’s color. See [`Subtitle sample description`](subtitle_sample_description.md) for more information.

## See Also

- [Size](subtitle_style_atom/size.md)
  An unsigned 32-bit integer holding the size of the subtitle style atom.
- [Type](subtitle_style_atom/type.md)
  An unsigned 32-bit field.
- [Entry count](subtitle_style_atom/entry_count.md)
  An unsigned 16-bit integer specifying how many subtitle text style records follow this entry count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/subtitle_style_atom/subtitle_text_style_record)*