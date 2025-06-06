# Hint sample data format

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies the data format and location of the hint track sample data.

#### Overview

The sample description atom (`'stsd'`) contains information about the hint track samples. It specifies the data format (note that currently only RTP data format is defined) and the data reference to use (if more than one is defined) to locate the hint track sample data. It also contains some general information about this hint track, such as the hint track version number, the maximum packet size allowed by this hint track, and the RTP time scale. It may contain additional information, such as the random offsets to add to the RTP time stamp and sequence number.

The sample description atom can contain a table of sample descriptions to accommodate media that are encoded in multiple formats, but a hint track can be expected to have a single sample description at this time.

The sample description for hint tracks is defined in the following table.

| Data field | Bytes |
| --- | --- |
| [`Size`](hint_track_sample_description/size.md) | 4 |
| [`Data format`](hint_track_sample_description/data_format.md) | 4 |
| [`Reserved`](hint_track_sample_description/reserved.md) | 6 |
| [`Data reference index`](hint_track_sample_description/data_reference_index.md) | 2 |
| [`Hint track version`](hint_track_sample_description/hint_track_version.md) | 2 |
| [`Last compatible hint track version`](hint_track_sample_description/last_compatible_hint_track_version.md) | 2 |
| [`Max packet size`](hint_track_sample_description/max_packet_size.md) | 4 |
| [`Additional data table`](hint_track_sample_description/additional_data_table.md) | variable |

## Topics

### Data fields
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
- [Additional data table](hint_track_sample_description/additional_data_table.md)
  A table of variable length containing additional information.

## See Also

- [Hint media](hint_media.md)
  Provide information about data units to stream in hint tracks.
- [Finding an original media track from a hint track](finding_an_original_media_track_from_a_hint_track.md)
  Use track reference atoms from hint tracks to locate the original media track.
- [RTP hint tracks](rtp_hint_tracks.md)
  Allow a streaming server to create RTP streams from a QuickTime movie.
- [Packetization hint sample data](packetization_hint_sample_data.md)
  An atom that describes the sample data for data using the Real-Time Transport Protocol (RTP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/hint_track_sample_description)*