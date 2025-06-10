# MPEG-4 audio codec

**Framework**: QuickTime File Format

#### Overview

#### Feature Values

The least significant 5 bits hold the value. The most significant 27 bits of the feature value should be set to `0`.

The list of audio object type constants is defined in specification ISO/IEC 14496-3, subclause 1.5.1.1.

Examples: AAC LC is indicated by the value `2`, CELP is indicated by the value `8`.

#### Writer Responsibilities

A writer of the MPEG-4 Audio Codec feature should record the 5 bits corresponding to the `AudioObjectType` found in the `ES_descriptor`’s audio `DecoderSpecificConfig`. The most significant 27 bits of the value should be set to `0`.

> **Note**: A writer that records the MPEG-4 Audio Codec feature is encouraged also to write the QuickTime Audio Codec Type feature.

#### Feature Value Algorithm

The MPEG-4 audio codec value is the 5 bits of the `AudioObjectType` found in the `AudioSpecificInfo` (a `DecoderSpecificInfo`). See specification ISO/IEC 14496, subclause 1.6. The `AudioSpecificInfo` is found in the MPEG-4 Elementary Stream Descriptor Atom within the `siDecompressionParam` atom of the audio sample description for the QuickTime audio codec of type `'mp4a'`.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value with the set of MPEG-4 audio decoders supported by the reader.

#### Comments

Because the QuickTime `'mp4a'` codec may implement multiple audio decoders defined in specification ISO/IEC 14496 in the future, this feature allows the reader to determine the specific audio decoder needed to interpret the audio bit stream. The MPEG-4 Audio Codec feature should be present only if the `'mp4a'` audio codec is used in a sound track.

## See Also

- [Table of features](table_of_features.md)
- [Maximum video bit rate](maximum_video_bit_rate.md)
- [Average video bit rate](average_video_bit_rate.md)
- [Maximum audio bit rate](maximum_audio_bit_rate.md)
- [Average audio bit rate](average_audio_bit_rate.md)
- [QuickTime video codec type](quicktime_video_codec_type.md)
- [QuickTime audio codec type](quicktime_audio_codec_type.md)
- [MPEG-4 video profile](mpeg-4_video_profile.md)
- [MPEG-4 video codec](mpeg-4_video_codec.md)
- [MPEG-4 video object type](mpeg-4_video_object_type.md)
- [Maximum video size in a movie](maximum_video_size_in_a_movie.md)
- [Maximum video size in a track](maximum_video_size_in_a_track.md)
- [Maximum video frame rate in a single track](maximum_video_frame_rate_in_a_single_track.md)
- [Average video frame rate in a single track](average_video_frame_rate_in_a_single_track.md)
- [Video variable frame rate indication](video_variable_frame_rate_indication.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/mpeg-4_audio_codec)*