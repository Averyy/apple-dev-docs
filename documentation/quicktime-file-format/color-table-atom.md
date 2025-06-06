# Color table atom ('ctab')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that defines a list of preferred colors for displaying the movie on devices that support only 256 colors.

#### Overview

Color table atoms define a list of preferred colors for displaying the movie on devices that support only 256 colors. The list may contain up to 256 colors. These optional atoms have a type value of `'ctab'`. The color table atom contains a Macintosh color table data structure.

The layout of a color table atom is as follows.

| Data field | Bytes |
| --- | --- |
| [`Size`](color_table_atom/size.md) | 4 |
| [`Type`](color_table_atom/type.md) | 4 |
| [`Color table seed`](color_table_atom/color_table_seed.md) | 4 |
| [`Color table flags`](color_table_atom/color_table_flags.md) | 2 |
| [`Color table size`](color_table_atom/color_table_size.md) | 2 |
| [`Color array`](color_table_atom/color_array.md) | Variable |

## Topics

### Data fields
- [Size](color_table_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this color table atom.
- [Type](color_table_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Color table seed](color_table_atom/color_table_seed.md)
  A 32-bit integer.
- [Color table flags](color_table_atom/color_table_flags.md)
  A 16-bit integer.
- [Color table size](color_table_atom/color_table_size.md)
  A 16-bit integer that indicates the number of colors in the following color array.
- [Color array](color_table_atom/color_array.md)
  An array of colors.

## See Also

- [Movie atom ('moov')](movie_atom.md)
  An atom that specifies the information that defines a movie.
- [Movie header atom ('mvhd')](movie_header_atom.md)
  An atom that specifies the characteristics of an entire QuickTime movie.
- [User data atoms](user_data_atoms.md)
  Atoms you use to define and store data associated with a QuickTime object.
- [Interleaving movie data](interleaving_movie_data.md)
  Interleave data in your movie for optimal playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/color_table_atom)*