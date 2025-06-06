# Data reference atom

**Framework**: QuickTime File Format  
**Kind**: class

An atom that contains tabular data that instructs the data handler component how to access the media’s data.

## Topics

### Data fields
- [Size](media_data_reference_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this data reference atom.
- [Type](media_data_reference_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](media_data_reference_atom/version.md)
  A 1-byte specification of the version of this data reference atom.
- [Flags](media_data_reference_atom/flags.md)
  A 3-byte space for data reference flags.
- [Number of entries](media_data_reference_atom/number_of_entries.md)
  A 32-bit integer containing the count of data references that follow.
- [Data references](media_data_reference_atom/data_references.md)
  An array of data references.

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
- [Base media info atom ('gmin')](base_media_info_atom.md)
  An atom that defines the media’s control information, including graphics mode and balance information.
- [Data information atom ('dinf')](data_information_atom.md)
  An atom that specifies the data handler component that provides access to the media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/media_data_reference_atom)*