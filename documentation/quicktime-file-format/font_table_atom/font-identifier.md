# Font identifier

**Framework**: QuickTime File Format  
**Kind**: property

An unsigned 16-bit integer that identifies the font.

#### Overview

This can be any number to uniquely identify this font in this table, but it must match the font number specified in the subtitle sample description and in any per-sample style records (`'styl'`).

## See Also

- [Size](font_table_atom/size.md)
  An unsigned 32-bit integer holding the size of the font table atom.
- [Type](font_table_atom/type.md)
  An unsigned 32-bit field.
- [Count](font_table_atom/count.md)
  An unsigned 16-bit integer specifying how many fonts are described in this table.
- [Font name length](font_table_atom/font_name_length.md)
  An unsigned 8-bit integer specifying the length of the font name in bytes.
- [Font name](font_table_atom/font_name.md)
  Must be either “Serif” or “Sans-Serif”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/font_table_atom/font_identifier)*