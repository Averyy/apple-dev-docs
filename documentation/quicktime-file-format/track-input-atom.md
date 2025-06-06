# Track input atom ('  in')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies how to use the input data.

#### Overview

The track input atom may contain two other types of atoms: input type atoms and object ID atoms. The input type atom is required; it specifies how the data is to be interpreted.

The track input atom layout is as follows:

| Track input atom | Bytes |
| --- | --- |
| [`Size`](track_input_atom/size.md) | 4 |
| [`Type`](track_input_atom/type.md) = `' in'` | 4 |
| [`Atom ID`](track_input_atom/atom_id.md) | 4 |
| [`Reserved`](track_input_atom/reserved.md) | 2 |
| [`Child count`](track_input_atom/child_count.md) | 2 |
| [`Reserved`](track_input_atom/reserved_2.md) | 4 |
| [`Input type atom`](track_input_atom/input_type_atom.md)‡ | 12 |
| [`Object ID atom`](track_input_atom/object_id_atom.md) | 12 |

‡ Required atom.

## Topics

### Data fields
- [Size](track_input_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this track input atom.
- [Type](track_input_atom/type.md)
  A 32-bit integer that identifies the atom type.
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

## See Also

- [Track input map atom ('imap')](track_input_map_atom.md)
  An atom that defines how data being sent to this track from its nonprimary sources is to be interpreted.
- [Input type atom ('  ty')](input_type_atom.md)
  An atom that specifies how to interpret track input data.
- [Object ID atom ('obid')](object_id_atom.md)
  An atom that identifies an object, such as a sprite within a sprite track, in a track input atom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/track_input_atom)*