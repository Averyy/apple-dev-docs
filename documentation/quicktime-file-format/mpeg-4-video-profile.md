# MPEG-4 video profile

**Framework**: QuickTime File Format

#### Overview

#### Feature Values

The least significant 8 bits hold the value. The most significant 24 bits of the feature value should be set to `0`.

#### Writer Responsibilities

A writer of the MPEG-4 video profile feature should record the 8 bits corresponding to the `profile_and_level_indication` from the `visual_object_sequence`, as defined in specification ISO/IEC 14496-2, found in the video parameters encoded in the esds of the MPEG-4 video codec sample description (with QuickTime codec type `'mp4v'`).

> **Note**: A writer that records the MPEG-4 video profile feature is encouraged also to write the QuickTime Video Codec Type feature.

#### Feature Value Algorithm

The feature value is the `profile_and_level_indication` from the `visual_object_sequence`, as defined in specification ISO/IEC 14496-2, retrieved from the video parameters for the MPEG-4 video codec description.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value with the set of profiles and levels supported by the reader.

#### Comments

This feature may be present only if MPEG-4 video is used. Normally, the video codec type profile entry will also record that MPEG-4 video is present, unless no codec types are present (when, for example, an exhaustive list cannot be formed).

## See Also

- [Table of features](table_of_features.md)
- [Maximum video bit rate](maximum_video_bit_rate.md)
- [Average video bit rate](average_video_bit_rate.md)
- [Maximum audio bit rate](maximum_audio_bit_rate.md)
- [Average audio bit rate](average_audio_bit_rate.md)
- [QuickTime video codec type](quicktime_video_codec_type.md)
- [QuickTime audio codec type](quicktime_audio_codec_type.md)
- [MPEG-4 video codec](mpeg-4_video_codec.md)
- [MPEG-4 video object type](mpeg-4_video_object_type.md)
- [MPEG-4 audio codec](mpeg-4_audio_codec.md)
- [Maximum video size in a movie](maximum_video_size_in_a_movie.md)
- [Maximum video size in a track](maximum_video_size_in_a_track.md)
- [Maximum video frame rate in a single track](maximum_video_frame_rate_in_a_single_track.md)
- [Average video frame rate in a single track](average_video_frame_rate_in_a_single_track.md)
- [Video variable frame rate indication](video_variable_frame_rate_indication.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/mpeg-4_video_profile)*