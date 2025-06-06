# MPEG-4 video object type

**Framework**: Quicktime File Format

#### Overview

#### Feature Values

The value is a video object type constant that indicates a set of video tools. The list of video object type constants is defined in specification ISO/IEC 14496-2, subclause 6.3.3. The least significant 8 bits hold the value. The most significant 24 bits should be set to `0`.

Example: The Simple Object Type video object is indicated by the value `1`.

#### Writer Responsibilities

A writer of the MPEG-4 Video Object Type feature should record the 8 bits corresponding to the `video_object_type_indication` found in the `VideoObjectLayer` within the `ES_descriptor`’s video `DecoderSpecificConfig`. The most significant 24 bits of the value should be set to `0`. This feature should be written only for MPEG-4 video of video object type `1` (Video ID). If the MPEG-4 video does not use Video ID (`1`) for `visual_object_type`, the esds will have no `VideoObjectLayer` and consequently no `video_object_type_indication`. In this case, no MPEG-4 Video Object Type feature should be written.

> **Note**: A writer that records the MPEG-4 Video Object Type feature for encoded video using the Video ID visual object type is encouraged to write the MPEG-4 Video Codec and MPEG-4 Video Profile features as well.

#### Feature Value Algorithm

The MPEG-4 video object type is the least significant 8 bits of the `video_object_type_indication` found in the `VideoObjectLayer`. See ISO/IEC 14496-2, subclause 6.2.3. The `VideoObjectLayer` is found in the MPEG-4 Elementary Stream Descriptor Atom within the `'esds'` sample description atom of the video sample description for the QuickTime video codec of type `'mp4v'`.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value with the set of MPEG-4 video tools supported by the reader.

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
- [MPEG-4 audio codec](mpeg-4_audio_codec.md)
- [Maximum video size in a movie](maximum_video_size_in_a_movie.md)
- [Maximum video size in a track](maximum_video_size_in_a_track.md)
- [Maximum video frame rate in a single track](maximum_video_frame_rate_in_a_single_track.md)
- [Average video frame rate in a single track](average_video_frame_rate_in_a_single_track.md)
- [Video variable frame rate indication](video_variable_frame_rate_indication.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/mpeg-4_video_object_type)*