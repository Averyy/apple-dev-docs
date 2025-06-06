# Table data

**Framework**: QuickTime File Format  
**Kind**: property

A table of sample count and group description index pairs.

## Mentions

- [Representing encoder delay explicitly](example_representing_encoder_delay_explicitly.md)

#### Overview

The layout of the table data is as follows:

| Data field | Bytes |
| --- | --- |
| Sample count | 4 |
| Group description index | 4 |

## See Also

- [Size](sample-to-group_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this sample-to-group atom.
- [Type](sample-to-group_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](sample-to-group_atom/version.md)
  A 1-byte specification of the version of this sample-to-group atom.
- [Flags](sample-to-group_atom/flags.md)
  A 3-byte reserved space.
- [Grouping type](sample-to-group_atom/grouping_type.md)
  A 32-bit integer identifying the grouping type.
- [Default length](sample-to-group_atom/default_length.md)
  A 32-bit integer indicating the length of the group entry in the payload data.
- [Entry count](sample-to-group_atom/entry_count.md)
  A 32-bit integer giving the number of entries in the table data that follows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sample-to-group_atom/table_data)*