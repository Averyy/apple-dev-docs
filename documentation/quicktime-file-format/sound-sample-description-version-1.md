# Sound sample description version 1 ('stsd')

**Framework**: QuickTime File Format  
**Kind**: class

An extended sound sample description that supports compressed audio, and includes the ability to add atoms to the sound description.

#### Overview

The version field in the sample description is set to `1` for this version of the sound description structure. In version 1 of the sound description, introduced in QuickTime 3, the sound description record is extended by 4 fields, each 4 bytes long, and includes the ability to add atoms to the sound description.

These added fields are used to support out-of-band configuration settings for decompression and to allow some parsing of compressed QuickTime sound tracks without requiring the services of a decompressor.

These fields introduce the idea of a . For uncompressed audio, a packet is a sample from a single channel. For compressed audio, this field has no real meaning; by convention, it is treated as 1/number-of-channels.

These fields also introduce the idea of a . For uncompressed audio, a frame is one sample from each channel. For compressed audio, a frame is a compressed group of samples whose format is dependent on the compressor.

> ❗ **Important**: The value of all these fields has different meaning for compressed and uncompressed audio. The meaning may not be easily deducible from the field name.

The value of all these fields has different meaning for compressed and uncompressed audio. The meaning may not be easily deducible from the field name.

The four new fields are:

- [`Samples per packet`](sound_sample_description_version_1/samples_per_packet.md)
- [`Bytes per packet`](sound_sample_description_version_1/bytes_per_packet.md)
- [`Bytes per frame`](sound_sample_description_version_1/bytes_per_frame.md)
- [`Bytes per sample`](sound_sample_description_version_1/bytes_per_sample.md)

When capturing or compressing audio using the QuickTime API, the value of these fields can be obtained by calling the Apple Sound Manager’s `GetCompression` function. Historically, the value returned for the bytes per frame field was not always reliable, however, so this field was set by multiplying bytes per packet by the number of channels.

To facilitate playback on devices that support only one or two channels of audio in `'raw '` or `'twos'` format (such as most early Macintosh and Windows computers), all other uncompressed audio formats are treated as compressed formats, allowing a simple “decompressor” component to perform the necessary format conversion during playback. The audio samples are treated as opaque compressed frames for these data types, and the fields for sample size and bytes per sample are not meaningful.

The new fields correspond to the `CompressionInfo` structure used by the Macintosh Sound Manager (which uses 16-bit values) to describe the compression ratio of fixed ratio audio compression algorithms. If these fields are not used, they are set to `0`. File readers only need to check to see if `samplesPerPacket` is `0`.

#### Redefined Sample Tables

If the compression ID in the sample description is set to `–2`, the sound track uses redefined sample tables optimized for compressed audio.

Unlike video media, the data structures for QuickTime sound media were originally designed for uncompressed samples. The extended version 1 sound description structure provides a great deal of support for compressed audio, but it does not deal directly with the sample table atoms that point to the media data.

The ordinary sample tables do not point to compressed frames, which are the fundamental units of compressed audio data. Instead, they appear to point to individual uncompressed audio samples, each one byte in size, within the compressed frames. When used with the QuickTime API, QuickTime compensates for this fiction in a largely transparent manner, but attempting to parse the sound samples using the original sample tables alone can be quite complicated.

With the introduction of support for the playback of variable bit-rate (VBR) audio in QuickTime 4.1, the contents of a number of these fields were redefined, so that a frame of compressed audio is treated as a single media sample. The sample-to-chunk and chunk offset atoms point to compressed frames, and the sample size table documents the size of the frames. The size is constant for CBR audio, but can vary for VBR.

The time-to-sample table documents the duration of the frames. If the time scale is set to the sampling rate, which is typical, the duration equals the number of uncompressed samples in each frame, which is usually constant even for VBR (it is common to use a fixed frame duration). If a different media timescale is used, it is necessary to convert from timescale units to sampling rate units to calculate the number of samples.

This change in the meaning of the sample tables allows you to use the tables accurately to find compressed frames.

To indicate that this new meaning is used, a version 1 sound description is used and the compression ID field is set to `–2`. The `samplesPerPacket` field and the `bytesPerSample` field are not necessarily meaningful for variable bit rate audio, but these fields should be set correctly in cases where the values are constant; the other two new fields (`bytesPerPacket` and `bytesPerFrame`) are reserved and should be set to `0`.

If the compression ID field is set to zero, the sample tables describe uncompressed audio samples and cannot be used directly to find and manipulate compressed audio frames. QuickTime has built-in support that allows programmers to act as if these sample tables pointed to uncompressed 1-byte audio samples.

## Topics

### Data fields
- [Sample description size](sound_sample_description_version_1/sample_description_size.md)
  A 32-bit integer indicating the number of bytes in the sample description.
- [Data format](sound_sample_description_version_1/data_format.md)
  A 32-bit integer indicating the format of the stored data.
- [Reserved](sound_sample_description_version_1/reserved.md)
  Six bytes.
- [Data reference index](sound_sample_description_version_1/data_reference_index.md)
  A 16-bit integer that contains the index of the data reference to use to retrieve data associated with samples that use this sample description.
- [Version](sound_sample_description_version_1/version.md)
  A 16-bit integer that holds the sample description version.
- [Revision level](sound_sample_description_version_1/revision_level.md)
  A 16-bit integer.
- [Vendor](sound_sample_description_version_1/vendor.md)
  A 32-bit integer.
- [Number of channels](sound_sample_description_version_1/number_of_channels.md)
  A 16-bit integer that indicates the number of sound channels used by the sound sample.
- [Sample size](sound_sample_description_version_1/sample_size.md)
  A 16-bit integer that specifies the number of bits in each uncompressed sound sample.
- [Compression ID](sound_sample_description_version_1/compression_id.md)
  A 16-bit integer.
- [Packet size](sound_sample_description_version_1/packet_size.md)
  A 16-bit integer.
- [Sample rate](sound_sample_description_version_1/sample_rate.md)
  A 32-bit unsigned fixed-point number (16.16) that indicates the rate at which the sound samples were obtained.
- [Samples per packet](sound_sample_description_version_1/samples_per_packet.md)
  The number of uncompressed frames generated by a compressed frame, where an uncompressed frame is one sample from each channel.
- [Bytes per packet](sound_sample_description_version_1/bytes_per_packet.md)
  For uncompressed audio, the number of bytes in a sample for a single channel.
- [Bytes per frame](sound_sample_description_version_1/bytes_per_frame.md)
  The number of bytes in a frame.
- [Bytes per sample](sound_sample_description_version_1/bytes_per_sample.md)
  The size of an uncompressed sample in bytes.

## See Also

- [Sound sample description version 0 ('stsd')](sound_sample_description_version_0.md)
  A sound sample description that supports only uncompressed audio in raw or twos-complement format.
- [Sound sample description version 2 ('stsd')](sound_sample_description_version_2.md)
  An updated sound sample description that adds high resolution audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/sound_sample_description_version_1)*