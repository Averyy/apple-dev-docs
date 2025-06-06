# Wide atom ('wide')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that designates reserved space in the movie data file.

#### Overview

A `wide` atom typically precedes a movie data atom. The `wide` atom consists only of a `type` and `size` field. This occupies 8 bytes—enough space to add an extended size field to the header of the atom that follows, without displacing the contents of that atom. If an atom grows to exceed 2^32 bytes in size, and it is preceded by a `wide` atom, you may create a new atom header containing an extended size field by overwriting the existing atom header and the preceding `wide` atom.

## Topics

### Data fields
- [Size](wide_atom/size.md)
  A 32-bit integer that specifies the number of bytes in the atom.
- [Type](wide_atom/type.md)
  A 32-bit integer that identifies the atom type.

## See Also

- [Free space atom ('free')](free_space_atom.md)
  An atom that designates unused space in the movie data file.
- [Skip atom ('skip')](skip_atom.md)
  An atom that designates unused space in the movie data file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/wide_atom)*