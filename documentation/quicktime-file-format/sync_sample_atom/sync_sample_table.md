# Sync sample table

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A table of sample numbers.

## Overview

Each sample number corresponds to a key frame.

The layout of a sync sample table is as follows.

| Entry number | Sample |
| --- | --- |
| Number | Sample 1 |
| Number | Sample 2 |
| Number | Sample 3 |
| Number | Sample 4 |
| Number | Sample 5 |

## See Also

### Data fields
- [Size](./size.md)
  A 32-bit integer that specifies the number of bytes in this sync sample atom.
- [Type](./type.md)
  A 32-bit integer that identifies the atom type.
- [Version](./version.md)
  A 1-byte specification of the version of this sync sample atom.
- [Flags](./flags.md)
  A 3-byte space for sync sample flags.
- [Number of entries](./number_of_entries.md)
  A 32-bit integer containing the count of entries in the sync sample table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sync_sample_atom/sync_sample_table)*