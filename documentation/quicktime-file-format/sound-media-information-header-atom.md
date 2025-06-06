# Sound media information header atom ('smhd')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that stores the sound media’s control information, such as balance.

#### Overview

The layout of a sound media information header atom is as follows.

| Sound media information header atom | Bytes |
| --- | --- |
| [`Size`](sound_media_information_header_atom/size.md) | 4 |
| [`Type`](sound_media_information_header_atom/type.md) | 4 |
| [`Version`](sound_media_information_header_atom/version.md) | 1 |
| [`Flags`](sound_media_information_header_atom/flags.md) | 3 |
| [`Balance`](sound_media_information_header_atom/balance.md) | 2 |
| [`Reserved`](sound_media_information_header_atom/reserved.md) | 2 |

## Topics

### Data fields
- [Size](sound_media_information_header_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this sound media information header atom.
- [Type](sound_media_information_header_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](sound_media_information_header_atom/version.md)
  A 1-byte specification of the version of this sound media information header atom.
- [Flags](sound_media_information_header_atom/flags.md)
  A 3-byte space for sound media information flags.
- [Balance](sound_media_information_header_atom/balance.md)
  A 16-bit integer that specifies the sound balance of this sound media.
- [Reserved](sound_media_information_header_atom/reserved.md)
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
- [Base media information atom ('minf')](base_media_information_atom.md)
  An atom that stores the media information for media types such as timed metadata, text, MPEG, time code, and music.
- [Base media information header atom ('gmhd')](base_media_information_header_atom.md)
  An atom that indicates that this media information atom pertains to a base media.
- [Base media info atom ('gmin')](base_media_info_atom.md)
  An atom that defines the media’s control information, including graphics mode and balance information.
- [Data information atom ('dinf')](data_information_atom.md)
  An atom that specifies the data handler component that provides access to the media data.
- [Media data reference atom ('dref')](media_data_reference_atom.md)
  An atom that contains tabular data that instructs the data handler component how to access the media’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sound_media_information_header_atom)*