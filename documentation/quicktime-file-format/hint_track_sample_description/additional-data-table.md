# Additional data table

**Framework**: QuickTime File Format  
**Kind**: property

A table of variable length containing additional information.

#### Overview

Additional information is formatted as a series of tagged entries.

This field always contains a tagged entry indicating the RTP time scale for RTP data. All other tagged entries are optional.

Three data tags are currently defined for RTP data. One tag is defined for use with any type of data. You can create additional tags. Tags are identified using four-character codes. Tags using all lowercase letters are reserved by Apple. Ignore any tagged data you do not understand.

Table entries are structured like atoms. The structure of table entries is shown in the following table.

| Field | Format | Bytes |
| --- | --- | --- |
| Entry length | 32-bit integer | 4 |
| Data tag | 4-char code | 4 |
| Data | Variable | Entry length - 8 |

Tagged entries for the ’rtp ’ data format are defined as follows:

## See Also

- [Size](hint_track_sample_description/size.md)
  A 32-bit integer specifying the size of this sample description in bytes.
- [Data format](hint_track_sample_description/data_format.md)
  A four-character code indicating the data format of the hint track samples.
- [Reserved](hint_track_sample_description/reserved.md)
  Six bytes.
- [Data reference index](hint_track_sample_description/data_reference_index.md)
  A field that indirectly specifies where to find the hint track sample data.
- [Hint track version](hint_track_sample_description/hint_track_version.md)
  A 16-bit unsigned integer indicating the version of the hint track specification.
- [Last compatible hint track version](hint_track_sample_description/last_compatible_hint_track_version.md)
  A 16-bit unsigned integer indicating the oldest hint track version with which this hint track is backward-compatible.
- [Max packet size](hint_track_sample_description/max_packet_size.md)
  A 32-bit integer indicating the packet size limit, in bytes, used when creating this hint track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/hint_track_sample_description/additional_data_table)*