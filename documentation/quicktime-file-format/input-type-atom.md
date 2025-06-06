# Input type atom ('  ty')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies how to interpret track input data.

#### Overview

The input type atom is required; it specifies how the data is to be interpreted.

## Topics

### Data fields
- [Size](input_type_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this input type atom.
- [Type](input_type_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Input type](input_type_atom/input_type.md)
  A 32-bit integer that specifies the type of data that is to be received from the secondary data source.

## See Also

- [Track input map atom ('imap')](track_input_map_atom.md)
  An atom that defines how data being sent to this track from its nonprimary sources is to be interpreted.
- [Track input atom ('  in')](track_input_atom.md)
  An atom that specifies how to use the input data.
- [Object ID atom ('obid')](object_id_atom.md)
  An atom that identifies an object, such as a sprite within a sprite track, in a track input atom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/input_type_atom)*