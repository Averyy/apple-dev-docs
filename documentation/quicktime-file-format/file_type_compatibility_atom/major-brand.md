# Major brand

**Framework**: QuickTime File Format  
**Kind**: property

A 32-bit unsigned integer that represents a file format code.

#### Overview

A 32-bit unsigned integer that should be set to `'qt  '` (note the two trailing ASCII space characters) for QuickTime movie files. If a file is compatible with multiple brands, all such brands are listed in the [`Compatible brands`](file_type_compatibility_atom/compatible_brands.md) fields, and the Major brand identifies the preferred brand or best use.

## See Also

- [Size](file_type_compatibility_atom/size.md)
  A 32-bit integer that specifies the number of bytes in the atom.
- [Type](file_type_compatibility_atom/type.md)
  A 32-bit unsigned integer that identifies the atom type, typically represented as a four-character code.
- [Minor version](file_type_compatibility_atom/minor_version.md)
  A 32-bit field that indicates the file format specification version.
- [Compatible brands](file_type_compatibility_atom/compatible_brands.md)
  A series of unsigned 32-bit integers listing compatible file formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/file_type_compatibility_atom/major_brand)*