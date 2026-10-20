# Type

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A 32-bit integer that identifies the atom type.

#### Overview

This field must be set to `' in'` (note that the two leading bytes must be set to `0x00`).

## See Also

### Data fields
- [Size](./size.md)
  A 32-bit integer that specifies the number of bytes in this track input atom.
- [Atom ID](./atom_id.md)
  A 32-bit integer relating this track input atom to its secondary input.
- [Reserved](./reserved.md)
  A 16-bit integer.
- [Child count](./child_count.md)
  A 16-bit integer specifying the number of child atoms in this atom.
- [Reserved](./reserved_2.md)
  A 32-bit integer.
- [Input type atom](./input_type_atom.md)
  An atom that specifies how to interpret track input data.
- [Object ID atom](./object_id_atom.md)
  An atom that identifies an object, such as a sprite within a sprite track, in a track input atom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_input_atom/type)*