# Time-to-sample table

**Framework**: QuickTime File Format  
**Kind**: property

A table that defines the duration of each sample in the media.

#### Overview

Each table entry contains a count field and a duration field. The structure of the time-to-sample table is as follows.

| Field | Bytes |
| --- | --- |
| Sample count | 4 |
| Sample duration | 4 |

You define a time-to-sample table entry by specifying these fields:

Entries in the table describe samples according to their order in the media and their duration. If consecutive samples have the same duration, a single table entry can be used to define more than one sample. In these cases, the count field indicates the number of consecutive samples that have the same duration. For example, if a video media has a constant frame rate, this table would have one entry and the count would be equal to the number of samples.

An example of a time-to-sample table is as follows.

| Sample count | Sample duration |
| --- | --- |
| 4 | 3 |
| 2 | 1 |
| 3 | 2 |

The data stream contains a total of nine samples that correspond in count and duration to the entries of the table shown here. Even though samples 4, 5, and 6 are in the same chunk, sample 4 has a duration of 3, and samples 5 and 6 have a duration of 2.

## See Also

- [Size](time-to-sample_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this time-to-sample atom.
- [Type](time-to-sample_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Version](time-to-sample_atom/version.md)
  A 1-byte specification of the version of this time-to-sample atom.
- [Flags](time-to-sample_atom/flags.md)
  A 3-byte space for time-to-sample flags.
- [Number of entries](time-to-sample_atom/number_of_entries.md)
  A 32-bit integer containing the count of entries in the time-to-sample table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/time-to-sample_atom/time-to-sample_table)*