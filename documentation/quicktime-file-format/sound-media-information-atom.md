# Sound media information atom ('minf')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that contains a number of other atoms that define specific characteristics of the sound media data.

#### Overview

Sound media information atoms are the highest-level atoms in sound media. These atoms contain a number of other atoms that define specific characteristics of the sound media data.

The layout of a media information atom for sound is as follows.

| Sound media information atom | Bytes |
| --- | --- |
| [`Size`](sound_media_information_atom/size.md) | 4 bytes |
| [`Type`](sound_media_information_atom/type.md) = `'minf'` | 4 bytes |
| [`Sound media information header atom`](sound_media_information_atom/sound_media_information_header_atom.md) | `'smhd'`‡ |
| [`Handler reference atom`](sound_media_information_atom/handler_reference_atom.md) | `'hdlr'`‡ |
| [`Data information atom`](sound_media_information_atom/data_information_atom.md) | `'dinf'` |
| [`Sample table atom`](sound_media_information_atom/sample_table_atom.md) | `'stbl'` |

‡ denotes required atom.

## Topics

### Data fields
- [Size](sound_media_information_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this sound media information atom.
- [Type](sound_media_information_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Sound media information header atom](sound_media_information_atom/sound_media_information_header_atom.md)
  An atom that stores the sound media’s control information, such as balance.
- [Handler reference atom](sound_media_information_atom/handler_reference_atom.md)
  An atom that specifies the media handler component that is to be used to interpret the media’s data.
- [Data information atom](sound_media_information_atom/data_information_atom.md)
  An atom that specifies the data handler component that provides access to the media data.
- [Sample table atom](sound_media_information_atom/sample_table_atom.md)
  An atom that contains information for converting from media time to sample number to sample location.

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
- [Sound media information header atom ('smhd')](sound_media_information_header_atom.md)
  An atom that stores the sound media’s control information, such as balance.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sound_media_information_atom)*