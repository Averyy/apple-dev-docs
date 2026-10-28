# Type

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A 32-bit integer that identifies the atom type.

## Mentions

- [Representing encoder delay explicitly](../example_representing_encoder_delay_explicitly.md)

## Overview

This field must be set to `'elst'`.

## See Also

### Data fields
- [Size](./size.md)
  A 32-bit integer that specifies the number of bytes in this edit list atom.
- [Version](./version.md)
  A 1-byte specification of the version of this edit list atom.
- [Flags](./flags.md)
  Three bytes of space for flags.
- [Number of entries](./number_of_entries.md)
  A 32-bit integer that specifies the number of entries in the edit list atom.
- [Edit list table](./edit_list_table.md)
  An array of 32-bit values, grouped into entries containing 3 values each.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/edit_list_atom/type)*