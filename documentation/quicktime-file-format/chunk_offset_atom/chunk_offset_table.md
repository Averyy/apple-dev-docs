# Chunk offset table

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A chunk offset table consisting of an array of offset values.

#### Overview

There is one table entry for each chunk in the media. The offset contains the byte offset from the beginning of the data stream to the chunk. The table is indexed by chunk number — the first table entry corresponds to the first chunk, the second table entry is for the second chunk, and so on.

An example chunk offset table is as follows.

| Chunk offset | Chunk |
| --- | --- |
| Offset | Chunk 1 |
| Offset | Chunk 2 |
| Offset | Chunk 3 |
| Offset | Chunk 4 |
| Offset | Chunk 5 |

## See Also

### Data fields
- [Size](./size.md)
  A 32-bit integer that specifies the number of bytes in this chunk offset atom.
- [Type](./type.md)
  A 32-bit integer that identifies the atom type.
- [Version](./version.md)
  A 1-byte specification of the version of this chunk offset atom.
- [Flags](./flags.md)
  A 3-byte space for chunk offset flags.
- [Number of entries](./number_of_entries.md)
  A 32-bit integer containing the count of entries in the chunk offset table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/chunk_offset_atom/chunk_offset_table)*