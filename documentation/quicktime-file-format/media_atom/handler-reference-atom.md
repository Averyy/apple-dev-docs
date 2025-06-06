# Handler reference atom

**Framework**: QuickTime File Format  
**Kind**: property

This atom identifies the media handler component that is to be used to interpret the media data.

#### Overview

See [`Handler reference atom ('hdlr')`](handler_reference_atom.md) for more information.

Note that the handler reference atom tells you the kind of media this media atom contains—for example, video or sound. The layout of the media information atom is specific to the media handler that is to interpret the media. [`Media information atoms`](media_information_atoms.md) discusses how data may be stored in a media, using the video media format defined by Apple as an example.

## See Also

- [Size](media_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this media atom.
- [Type](media_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Media header atom](media_atom/media_header_atom.md)
  This atom contains the standard media information.
- [Extended language tag atom](media_atom/extended_language_tag_atom.md)
  This atom contains the extended language tag describing the media language.
- [Media information atom](media_atom/media_information_atom.md)
  This atom contains data specific to the media type for use by the media handler component.
- [User data atom](media_atom/user_data_atom.md)
  An atom where you define and store data associated with a QuickTime object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/media_atom/handler_reference_atom)*