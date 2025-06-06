# Component subtype

**Framework**: QuickTime File Format  
**Kind**: property

A four-character code that identifies the type of the media handler or data handler.

#### Overview

For media handlers, this field defines the type of data — for example, `'vide'` for video data, `'soun'` for sound data or `‘subt’` for subtitles. See [`Media data atom types`](media_data_atom_types.md) for information about defined media data types.

For data handlers, this field defines the data reference type; for example, a component subtype value of `'alis'` identifies a file alias.

## See Also

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
- [Component manufacturer](handler_reference_atom/component_manufacturer.md)
  Reserved.
- [Component flags](handler_reference_atom/component_flags.md)
  Reserved.
- [Component flags mask](handler_reference_atom/component_flags_mask.md)
  Reserved.
- [Component name](handler_reference_atom/component_name.md)
  A counted string that specifies the name of the component — that is, the media handler used when this media was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/handler_reference_atom/component_subtype)*