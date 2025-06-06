# Name

**Framework**: QuickTime File Format  
**Kind**: property

A string with a human-readable name for a metadata type.

#### Overview

The name is a NULL-terminated string in UTF-8 characters which gives a human-readable name for a metadata type, for debugging and inspection purposes.

The string may be empty or a single byte containing `0`.

## See Also

- [Size](metadata_handler_atom/size.md)
  A 32-bit unsigned integer that indicates the size in bytes of the atom structure.
- [Type](metadata_handler_atom/type.md)
  A 32-bit unsigned integer value.
- [Version](metadata_handler_atom/version.md)
  One byte.
- [Flags](metadata_handler_atom/flags.md)
  Three bytes.
- [Predefined](metadata_handler_atom/predefined.md)
  A 32-bit integer.
- [Handler type](metadata_handler_atom/handler_type.md)
  A 32-bit integer that indicates the structure used in the metadata atom.
- [Reserved](metadata_handler_atom/reserved.md)
  An array of 3 const unsigned 32-bit integers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/metadata_handler_atom/name)*