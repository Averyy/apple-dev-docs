# Type

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

The type of this atom.

#### Overview

This field must be set to `'rmvc'`.

## See Also

### Data fields
- [Size](./size.md)
  The number of bytes in this version check atom.
- [Flags](./flags.md)
  A 32-bit integer.
- [Software package](./software_package.md)
  A 32-bit Gestalt type specifying the software package to check for.
- [Version](./version.md)
  An unsigned 32-bit integer containing either the minimum required version or the required value after a binary `AND` operation.
- [Mask](./mask.md)
  The mask for a binary `AND` operation on the Gestalt bitfield.
- [Check type](./check_type.md)
  The type of check to perform, expressed as 16-bit integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/version_check_atom/type)*