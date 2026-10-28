# Hint track version

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A 16-bit unsigned integer indicating the version of the hint track specification.

## Overview

This is currently set to `1`.

## See Also

### Data fields
- [Size](./size.md)
  A 32-bit integer specifying the size of this sample description in bytes.
- [Data format](./data_format.md)
  A four-character code indicating the data format of the hint track samples.
- [Reserved](./reserved.md)
  Six bytes.
- [Data reference index](./data_reference_index.md)
  A field that indirectly specifies where to find the hint track sample data.
- [Last compatible hint track version](./last_compatible_hint_track_version.md)
  A 16-bit unsigned integer indicating the oldest hint track version with which this hint track is backward-compatible.
- [Max packet size](./max_packet_size.md)
  A 32-bit integer indicating the packet size limit, in bytes, used when creating this hint track.
- [Additional data table](./additional_data_table.md)
  A table of variable length containing additional information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/hint_track_sample_description/hint_track_version)*