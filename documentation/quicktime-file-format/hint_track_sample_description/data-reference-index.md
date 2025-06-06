# Data reference index

**Framework**: QuickTime File Format  
**Kind**: property

A field that indirectly specifies where to find the hint track sample data.

#### Overview

The data reference is a file or resource specified by the data reference atom (`'dref'`) inside the data information atom (`'dinf'`) of the hint track. The data information atom can contain a table of data references, and the data reference index is a 16-bit integer that tells you which entry in that table should be used. Normally, the hint track has a single data reference, and this index entry is set to `0`.

## See Also

- [Size](hint_track_sample_description/size.md)
  A 32-bit integer specifying the size of this sample description in bytes.
- [Data format](hint_track_sample_description/data_format.md)
  A four-character code indicating the data format of the hint track samples.
- [Reserved](hint_track_sample_description/reserved.md)
  Six bytes.
- [Hint track version](hint_track_sample_description/hint_track_version.md)
  A 16-bit unsigned integer indicating the version of the hint track specification.
- [Last compatible hint track version](hint_track_sample_description/last_compatible_hint_track_version.md)
  A 16-bit unsigned integer indicating the oldest hint track version with which this hint track is backward-compatible.
- [Max packet size](hint_track_sample_description/max_packet_size.md)
  A 32-bit integer indicating the packet size limit, in bytes, used when creating this hint track.
- [Additional data table](hint_track_sample_description/additional_data_table.md)
  A table of variable length containing additional information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/hint_track_sample_description/data_reference_index)*