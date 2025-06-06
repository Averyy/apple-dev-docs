# Preview atom ('pnot')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that contains information that allows you to find the preview image associated with a QuickTime movie.

#### Overview

The preview image, or poster, is a representative image suitable for display to the user in, for example, Open dialog boxes.

The preview atom has an atom type value of `'pnot'`.

## Topics

### Atom fields
- [Size](preview_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this preview atom.
- [Type](preview_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Modification date](preview_atom/modification_date.md)
  A 32-bit unsigned integer containing a date that indicates when the preview was last updated.
- [Version number](preview_atom/version_number.md)
  A 16-bit integer
- [Atom type](preview_atom/atom_type.md)
  A 32-bit integer that indicates the type of atom that contains the preview data.
- [Atom index](preview_atom/atom_index.md)
  A 16-bit integer that identifies which atom of the specified type is to be used as the preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/preview_atom)*