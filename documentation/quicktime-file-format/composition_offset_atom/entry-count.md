# Entry count

**Framework**: QuickTime File Format  
**Kind**: property

A 32-bit unsigned integer that specifies the number of sample numbers in the array that follows.

#### Overview

Following the entry count is a composition-offset table. The layout of the composition-offset table is as follows.

| Field | Bytes |
| --- | --- |
| sampleCount | 4 |
| compositionOffset | 4 |

## See Also

- [Size](composition_offset_atom/size.md)
  A 32-bit integer that specifies the number of bytes in the composition offset atom.
- [Type](composition_offset_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](composition_offset_atom/version.md)
  A 1-byte specification of the version of this atom.
- [Flags](composition_offset_atom/flags.md)
  A 3-byte space reserved for offset flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/composition_offset_atom/entry_count)*