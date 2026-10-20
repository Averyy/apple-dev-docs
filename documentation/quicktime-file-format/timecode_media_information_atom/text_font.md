# Text font

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A 16-bit integer that indicates the font to use.

#### Overview

Set this field to `0` to use the system font. If the font name field contains a valid name, ignore this field.

## See Also

### Data fields
- [Size](./size.md)
  A 32-bit integer that specifies the number of bytes in this time code media information atom.
- [Type](./type.md)
  A 32-bit integer that identifies the atom type.
- [Version](./version.md)
  A 1-byte specification of the version of this timecode media information atom.
- [Flags](./flags.md)
  A 3-byte space for timecode media information flags.
- [Text face](./text_face.md)
  A 16-bit integer that indicates the font’s style.
- [Text size](./text_size.md)
  A 16-bit integer that specifies the point size of the time code text.
- [Reserved](./reserved.md)
  A 16-bit integer that is reserved for use by Apple.
- [Text color](./text_color.md)
  A 48-bit RGB color value for the timecode text.
- [Background color](./background_color.md)
  A 48-bit RGB background color for the timecode text.
- [Font name](./font_name.md)
  A Pascal string specifying the name of the timecode text’s font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/timecode_media_information_atom/text_font)*