# Check type

**Framework**: QuickTime File Format  
**Kind**: property

The type of check to perform, expressed as 16-bit integer.

#### Overview

Set to `0` for a minimum version check, set to `1` for a required value after a binary `AND` of the Gestalt bitfield and the mask.

## See Also

- [Size](version_check_atom/size.md)
  The number of bytes in this version check atom.
- [Type](version_check_atom/type.md)
  The type of this atom.
- [Flags](version_check_atom/flags.md)
  A 32-bit integer.
- [Software package](version_check_atom/software_package.md)
  A 32-bit Gestalt type specifying the software package to check for.
- [Version](version_check_atom/version.md)
  An unsigned 32-bit integer containing either the minimum required version or the required value after a binary `AND` operation.
- [Mask](version_check_atom/mask.md)
  The mask for a binary `AND` operation on the Gestalt bitfield.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/version_check_atom/check_type)*