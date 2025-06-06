# MPEG-4 video codec

**Framework**: QuickTime File Format

#### Overview

#### Feature Values

The least significant 4 bits hold the value. The most significant 28 bits of the feature value should be set to `0`.

The list of visual object type constants is defined in specification ISO/IEC 14496-2, subclause 6.3.2.

Example: Video ID is indicated by the value `1`.

#### Writer Responsibilities

A writer of the MPEG-4 Video Codec feature should record the 4 bits corresponding to the `visual_object_type` found in the `VisualObject` within the `ES_descriptor`’s video `DecoderSpecificConfig`. The most significant 28 bits of the value should be set to `0`.

> **Note**: A writer that records the MPEG-4 Video Codec feature is encouraged also to write the QuickTime Video Codec Type feature.

A writer that records the MPEG-4 Video Codec feature is encouraged also to write the QuickTime Video Codec Type feature.

#### Feature Value Algorithm

The MPEG-4 video codec is the 4 bits of the `visual_object_type` found in the `VisualObject`. See ISO/IEC 14496-2, subclause 6.2.2. The VisualObject is found in the MPEG-4 Elementary Stream Descriptor Atom within the `'esds'` sample description atom of the video sample description for the QuickTime video codec of type `'mp4v'`.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value with the set of MPEG-4 video decoders supported by the reader.

#### Comments

Because the QuickTime `'mp4v'` codec may implement multiple video decoders defined in specification ISO/IEC 14496 in the future, this feature allows the reader to determine the specific video decoder needed to interpret the video bit-stream.

## See Also

- [Table of features](table_of_features.md)
- [Maximum video bit rate](maximum_video_bit_rate.md)
- [Average video bit rate](average_video_bit_rate.md)
- [Maximum audio bit rate](maximum_audio_bit_rate.md)
- [Average audio bit rate](average_audio_bit_rate.md)
- [QuickTime video codec type](quicktime_video_codec_type.md)
- [QuickTime audio codec type](quicktime_audio_codec_type.md)
- [MPEG-4 video profile](mpeg-4_video_profile.md)
- [MPEG-4 video object type](mpeg-4_video_object_type.md)
- [MPEG-4 audio codec](mpeg-4_audio_codec.md)
- [Maximum video size in a movie](maximum_video_size_in_a_movie.md)
- [Maximum video size in a track](maximum_video_size_in_a_track.md)
- [Maximum video frame rate in a single track](maximum_video_frame_rate_in_a_single_track.md)
- [Average video frame rate in a single track](average_video_frame_rate_in_a_single_track.md)
- [Video variable frame rate indication](video_variable_frame_rate_indication.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/mpeg-4_video_codec)*