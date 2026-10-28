# Flags

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A 3-byte space for video media information flags.

## Overview

There is one defined flag.

- **No lean ahead**: This is a compatibility flag that allows QuickTime to distinguish between movies created with QuickTime 1.0 and newer movies. Always set this flag to `1`, unless you are creating a movie intended for playback using version 1.0 of QuickTime. This flag’s value is `0x0001`.

## See Also

### Data fields
- [Size](./size.md)
  A 32-bit integer that specifies the number of bytes in this video media information header atom.
- [Type](./type.md)
  A 32-bit integer that identifies the atom type.
- [Version](./version.md)
  A 1-byte specification of the version of this video media information header atom.
- [Graphics mode](./graphics_mode.md)
  A 16-bit integer that specifies the transfer mode.
- [Opcolor](./opcolor.md)
  Three 16-bit values that specify the red, green, and blue colors for the transfer mode operation indicated in the graphics mode field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/video_media_information_header_atom/flags)*