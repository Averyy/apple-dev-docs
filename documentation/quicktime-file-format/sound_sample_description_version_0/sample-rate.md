# Sample rate

**Framework**: QuickTime File Format  
**Kind**: property

A 32-bit unsigned fixed-point number (16.16) that indicates the rate at which the sound samples were obtained.

#### Overview

The integer portion of this number should match the media’s time scale. Many older version 0 files have values of `22254.5454` or `11127.2727`, but most files have integer values, such as `44100`. Sample rates greater than 2^16 are not supported.

## See Also

- [Sample description size](sound_sample_description_version_0/sample_description_size.md)
  A 32-bit integer indicating the number of bytes in the sample description.
- [Data format](sound_sample_description_version_0/data_format.md)
  A 32-bit integer indicating the format of the stored data.
- [Reserved](sound_sample_description_version_0/reserved.md)
  Six bytes.
- [Data reference index](sound_sample_description_version_0/data_reference_index.md)
  A 16-bit integer that contains the index of the data reference to use to retrieve data associated with samples that use this sample description.
- [Version](sound_sample_description_version_0/version.md)
  A 16-bit integer that holds the sample description version.
- [Revision level](sound_sample_description_version_0/revision_level.md)
  A 16-bit integer.
- [Vendor](sound_sample_description_version_0/vendor.md)
  A 32-bit integer.
- [Number of channels](sound_sample_description_version_0/number_of_channels.md)
  A 16-bit integer that indicates the number of sound channels used by the sound sample.
- [Sample size](sound_sample_description_version_0/sample_size.md)
  A 16-bit integer that specifies the number of bits in each uncompressed sound sample.
- [Compression ID](sound_sample_description_version_0/compression_id.md)
  A 16-bit integer.
- [Packet size](sound_sample_description_version_0/packet_size.md)
  A 16-bit integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sound_sample_description_version_0/sample_rate)*