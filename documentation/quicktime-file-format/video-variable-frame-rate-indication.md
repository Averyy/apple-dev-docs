# Video variable frame rate indication

**Framework**: QuickTime File Format

#### Overview

#### Feature Values

The feature value holds one of the following two values: `0` if all video samples have the same display duration, or `1` if any video samples vary in duration.

#### Writer Responsibilities

A writer of the Video Variable Frame Rate Indication feature should compare the video track sample durations. If all considered durations have the same value, the value `0` indicating constant frame rate should be recorded. If any durations differ, the value `1` should be recorded for the feature. No other value should be recorded.

#### Feature Value Algorithm

If the Time to Sample table records a constant duration for all samples, then record `0`, else record `1`.

#### Reader Responsibilities

A reader of this feature code should only expect the values `0` or `1`.

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
- [MPEG-4 audio codec](mpeg-4_audio_codec.md)
- [Maximum video size in a movie](maximum_video_size_in_a_movie.md)
- [Maximum video size in a track](maximum_video_size_in_a_track.md)
- [Maximum video frame rate in a single track](maximum_video_frame_rate_in_a_single_track.md)
- [Average video frame rate in a single track](average_video_frame_rate_in_a_single_track.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/video_variable_frame_rate_indication)*