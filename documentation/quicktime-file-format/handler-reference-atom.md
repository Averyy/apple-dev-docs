# Handler reference atom ('hdlr')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies the media handler component that is to be used to interpret the media’s data.

#### Overview

The handler reference atom has an atom type value of `'hdlr'`.

Historically, the handler reference atom was also used for data references. However, this isn’t the case anymore.

The handler atom within a media atom declares the process by which the media data in the stream may be presented, and thus, the nature of the media in a stream. For example, a video handler would handle a video track.

The layout of a handler reference atom is as follows.

| Handler reference atom | Bytes |
| --- | --- |
| [`Size`](handler_reference_atom/size.md) | 4 |
| [`Type`](handler_reference_atom/type.md) | 4 |
| [`Version`](handler_reference_atom/version.md) | 1 |
| [`Flags`](handler_reference_atom/flags.md) | 3 |
| [`Component type`](handler_reference_atom/component_type.md) | 4 |
| [`Component subtype`](handler_reference_atom/component_subtype.md) | 4 |
| [`Component manufacturer`](handler_reference_atom/component_manufacturer.md) | 4 |
| [`Component flags`](handler_reference_atom/component_flags.md) | 4 |
| [`Component flags mask`](handler_reference_atom/component_flags_mask.md) | 4 |
| [`Component name`](handler_reference_atom/component_name.md) | Variable |

## Topics

### Data fields
- [Size](handler_reference_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this handler reference atom.
- [Type](handler_reference_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](handler_reference_atom/version.md)
  A 1-byte specification of the version of this handler information.
- [Flags](handler_reference_atom/flags.md)
  A 3-byte space for handler information flags.
- [Component type](handler_reference_atom/component_type.md)
  A four-character code that identifies the type of the handler.
- [Component subtype](handler_reference_atom/component_subtype.md)
  A four-character code that identifies the type of the media handler or data handler.
- [Component manufacturer](handler_reference_atom/component_manufacturer.md)
  Reserved.
- [Component flags](handler_reference_atom/component_flags.md)
  Reserved.
- [Component flags mask](handler_reference_atom/component_flags_mask.md)
  Reserved.
- [Component name](handler_reference_atom/component_name.md)
  A counted string that specifies the name of the component — that is, the media handler used when this media was created.

## See Also

- [Media atom ('mdia')](media_atom.md)
  An atom that describes and defines a track’s media type and sample data.
- [Media header atom ('mdhd')](media_header_atom.md)
  An atom that specifies the characteristics of a media, including time scale and duration.
- [Extended language tag atom ('elng')](extended_language_tag_atom.md)
  An atom that represents media language information.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/handler_reference_atom)*