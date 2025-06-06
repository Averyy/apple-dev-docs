# Type

**Framework**: QuickTime File Format  
**Kind**: property

A 32-bit integer that identifies the atom type.

#### Overview

This field must be set to `' in'` (note that the two leading bytes must be set to `0x00`).

## See Also

- [Size](track_input_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this track input atom.
- [Atom ID](track_input_atom/atom_id.md)
  A 32-bit integer relating this track input atom to its secondary input.
- [Reserved](track_input_atom/reserved.md)
  A 16-bit integer.
- [Child count](track_input_atom/child_count.md)
  A 16-bit integer specifying the number of child atoms in this atom.
- [Reserved](track_input_atom/reserved_2.md)
  A 32-bit integer.
- [Input type atom](track_input_atom/input_type_atom.md)
  An atom that specifies how to interpret track input data.
- [Object ID atom](track_input_atom/object_id_atom.md)
  An atom that identifies an object, such as a sprite within a sprite track, in a track input atom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_input_atom/type)*