# Base media info atom ('gmin')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that defines the media’s control information, including graphics mode and balance information.

#### Overview

The base media info atom, contained in the base media information header atom (`'gmhd'`), defines the media’s control information, including graphics mode and balance information.

The layout of the base media info atom is as follows.

| Base media info atom | Bytes |
| --- | --- |
| [`Size`](base_media_info_atom/size.md) | 4 |
| [`Type`](base_media_info_atom/type.md) | 4 |
| [`Version`](base_media_info_atom/version.md) | 1 |
| [`Flags`](base_media_info_atom/flags.md) | 3 |
| [`Graphics mode`](base_media_info_atom/graphics_mode.md) | 2 |
| [`Opcolor`](base_media_info_atom/opcolor.md) | 6 |
| [`Balance`](base_media_info_atom/balance.md) | 2 |
| [`Reserved`](base_media_info_atom/reserved.md) | 2 |

## Topics

### Data fields
- [Size](base_media_info_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this base media info atom.
- [Type](base_media_info_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](base_media_info_atom/version.md)
  A 1-byte specification of the version of this base media information header atom.
- [Flags](base_media_info_atom/flags.md)
  A 3-byte space for base media information flags.
- [Graphics mode](base_media_info_atom/graphics_mode.md)
  A 16-bit integer that specifies the transfer mode.
- [Opcolor](base_media_info_atom/opcolor.md)
  Three 16-bit values that specify the red, green, and blue colors for the transfer mode operation indicated in the graphics mode field.
- [Balance](base_media_info_atom/balance.md)
  A 16-bit integer that specifies the sound balance of this media.
- [Reserved](base_media_info_atom/reserved.md)
  Reserved for use by Apple.

## See Also

- [Media atom ('mdia')](media_atom.md)
  An atom that describes and defines a track’s media type and sample data.
- [Media header atom ('mdhd')](media_header_atom.md)
  An atom that specifies the characteristics of a media, including time scale and duration.
- [Extended language tag atom ('elng')](extended_language_tag_atom.md)
  An atom that represents media language information.
- [Handler reference atom ('hdlr')](handler_reference_atom.md)
  An atom that specifies the media handler component that is to be used to interpret the media’s data.
- [Media information atoms](media_information_atoms.md)
  An atom that contains a number of other atoms that define specific characteristics of the video media data.
- [Video media information atom ('minf')](video_media_information_atom.md)
  An atom that contains a number of other atoms that define specific characteristics of the video media data.
- [Video media information header atom ('vmhd')](video_media_information_header_atom.md)
  An atom that defines specific color and graphics mode information.
- [Sound media information atom ('minf')](sound_media_information_atom.md)
  An atom that contains a number of other atoms that define specific characteristics of the sound media data.
- [Sound media information header atom ('smhd')](sound_media_information_header_atom.md)
  An atom that stores the sound media’s control information, such as balance.
- [Base media information atom ('minf')](base_media_information_atom.md)
  An atom that stores the media information for media types such as timed metadata, text, MPEG, time code, and music.
- [Base media information header atom ('gmhd')](base_media_information_header_atom.md)
  An atom that indicates that this media information atom pertains to a base media.
- [Data information atom ('dinf')](data_information_atom.md)
  An atom that specifies the data handler component that provides access to the media data.
- [Media data reference atom ('dref')](media_data_reference_atom.md)
  An atom that contains tabular data that instructs the data handler component how to access the media’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/base_media_info_atom)*