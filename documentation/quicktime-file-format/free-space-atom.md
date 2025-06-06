# Free space atom ('free')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that designates unused space in the movie data file.

#### Overview

Both `free` and `skip` atoms designate unused space in the movie data file. These atoms consist of only an atom header (size and type fields), followed by the appropriate number of bytes of free space. When reading a QuickTime movie, your application may safely skip these atoms. When writing or updating a movie, you may reuse the space associated with these atom types.

## Topics

### Data fields
- [Size](free_space_atom/size.md)
  A 32-bit integer that specifies the number of bytes in the atom.
- [Type](free_space_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Free space](free_space_atom/free_space.md)
  Bytes of free space.

## See Also

- [Skip atom ('skip')](skip_atom.md)
  An atom that designates unused space in the movie data file.
- [Wide atom ('wide')](wide_atom.md)
  An atom that designates reserved space in the movie data file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/free_space_atom)*