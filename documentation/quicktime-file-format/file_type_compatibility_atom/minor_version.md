# Minor version

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A 32-bit field that indicates the file format specification version.

## Overview

For QuickTime movie files, this takes the form of four binary-coded decimal values, indicating the century, year, and month of the *QuickTime File Format Specification*, followed by a binary coded decimal zero. For example, for the June 2004 minor version, this field is set to the BCD values `20 04 06 00`.

## See Also

### Data fields
- [Size](./size.md)
  A 32-bit integer that specifies the number of bytes in the atom.
- [Type](./type.md)
  A 32-bit unsigned integer that identifies the atom type, typically represented as a four-character code.
- [Major brand](./major_brand.md)
  A 32-bit unsigned integer that represents a file format code.
- [Compatible brands](./compatible_brands.md)
  A series of unsigned 32-bit integers listing compatible file formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/file_type_compatibility_atom/minor_version)*