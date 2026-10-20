# Object ID atom ('obid')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that identifies an object, such as a sprite within a sprite track, in a track input atom.

#### Overview

If the input is operating on an object within the track (for example, a sprite within a sprite track), an object ID atom must be included in the track input atom to identify the object.

## Topics

### Data fields
- [Size](object_id_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this object ID atom.
- [Type](object_id_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Object ID](object_id_atom/object_id.md)
  A 32-bit integer identifying the object.

## See Also

- [Track input map atom ('imap')](track_input_map_atom.md)
  An atom that defines how data being sent to this track from its nonprimary sources is to be interpreted.
- [Track input atom ('  in')](track_input_atom.md)
  An atom that specifies how to use the input data.
- [Input type atom ('  ty')](input_type_atom.md)
  An atom that specifies how to interpret track input data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/object_id_atom)*