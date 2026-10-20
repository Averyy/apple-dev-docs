# Atom ID

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A 32-bit integer relating this track input atom to its secondary input.

#### Overview

The value of this field corresponds to the index of the secondary input in the track reference atom. That is, the first secondary input corresponds to the track input atom with an atom ID value of `1`; the second to the track input atom with an atom ID of `2`, and so on.

## See Also

### Data fields
- [Size](./size.md)
  A 32-bit integer that specifies the number of bytes in this track input atom.
- [Type](./type.md)
  A 32-bit integer that identifies the atom type.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_input_atom/atom_id)*