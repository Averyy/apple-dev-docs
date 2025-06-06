# Sound sample description version 0 ('stsd')

**Framework**: QuickTime File Format  
**Kind**: class

A sound sample description that supports only uncompressed audio in raw or twos-complement format.

#### Overview

There are currently three versions of the sound sample description, versions 0, 1 and 2. Version 0 supports only uncompressed audio in raw (`'raw '`) or twos-complement (`'twos'`) format, although these are sometimes incorrectly specified as either `'NONE'` or `0x00000000`.

Version 0 of the sound description format assumes uncompressed audio in `'raw '` or `'twos'` format, 1 or 2 channels, 8 or 16 bits per sample, and a compression ID of `0`.

## Topics

### Data fields
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
- [Sample rate](sound_sample_description_version_0/sample_rate.md)
  A 32-bit unsigned fixed-point number (16.16) that indicates the rate at which the sound samples were obtained.

## See Also

- [Sound sample description version 1 ('stsd')](sound_sample_description_version_1.md)
  An extended sound sample description that supports compressed audio, and includes the ability to add atoms to the sound description.
- [Sound sample description version 2 ('stsd')](sound_sample_description_version_2.md)
  An updated sound sample description that adds high resolution audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sound_sample_description_version_0)*