# Compatible brands

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A series of unsigned 32-bit integers listing compatible file formats.

## Overview

The major brand must appear in the list of compatible brands. One or more “placeholder” entries with value zero are permitted; such entries should be ignored.

## See Also

### Data fields
- [Size](./size.md)
  A 32-bit integer that specifies the number of bytes in the atom.
- [Type](./type.md)
  A 32-bit unsigned integer that identifies the atom type, typically represented as a four-character code.
- [Major brand](./major_brand.md)
  A 32-bit unsigned integer that represents a file format code.
- [Minor version](./minor_version.md)
  A 32-bit field that indicates the file format specification version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/file_type_compatibility_atom/compatible_brands)*