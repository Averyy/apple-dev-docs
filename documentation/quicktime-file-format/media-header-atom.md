# Media header atom ('mdhd')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies the characteristics of a media, including time scale and duration.

#### Overview

The media header atom specifies the characteristics of a media, including time scale and duration. The media header atom has an atom type of `'mdhd'`.

The layout of a media header atom is as follows.

| Media header atom | Bytes |
| --- | --- |
| [`Size`](media_header_atom/size.md) | 4 |
| [`Type`](media_header_atom/type.md) | 4 |
| [`Version`](media_header_atom/version.md) | 1 |
| [`Flags`](media_header_atom/flags.md) | 3 |
| [`Creation time`](media_header_atom/creation_time.md) | 4 |
| [`Modification time`](media_header_atom/modification_time.md) | 4 |
| [`Time scale`](media_header_atom/time_scale.md) | 4 |
| [`Duration`](media_header_atom/duration.md) | 4 |
| [`Language`](media_header_atom/language.md) | 2 |
| [`Quality`](media_header_atom/quality.md) | 2 |

## Topics

### Data fields
- [Size](media_header_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this media header atom.
- [Type](media_header_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](media_header_atom/version.md)
  One byte that specifies the version of this header atom.
- [Flags](media_header_atom/flags.md)
  Three bytes of space for media header flags.
- [Creation time](media_header_atom/creation_time.md)
  A 32-bit integer that specifies the creation date for the media atom.
- [Modification time](media_header_atom/modification_time.md)
  A 32-bit integer that specifies the last modification date for the media atom.
- [Time scale](media_header_atom/time_scale.md)
  A time value that indicates the time scale for this media.
- [Duration](media_header_atom/duration.md)
  The duration of this media in units of its time scale.
- [Language](media_header_atom/language.md)
  A 16-bit integer that specifies the language code for this media.
- [Quality](media_header_atom/quality.md)
  A 16-bit integer that specifies the media’s playback quality.

## See Also

- [Media atom ('mdia')](media_atom.md)
  An atom that describes and defines a track’s media type and sample data.
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
- [Base media info atom ('gmin')](base_media_info_atom.md)
  An atom that defines the media’s control information, including graphics mode and balance information.
- [Data information atom ('dinf')](data_information_atom.md)
  An atom that specifies the data handler component that provides access to the media data.
- [Media data reference atom ('dref')](media_data_reference_atom.md)
  An atom that contains tabular data that instructs the data handler component how to access the media’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/media_header_atom)*