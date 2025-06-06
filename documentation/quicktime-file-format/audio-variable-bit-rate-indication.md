# Audio variable bit rate indication

**Framework**: QuickTime File Format

#### Overview

#### Feature Values

The feature value holds one of the following two values: `0` if the audio is constant bit rate, or `1` if the audio is variable bit rate.

#### Writer Responsibilities

A writer of the Audio Variable Bit Rate Indication feature should determine if the audio frames are constant or variable bit rate in nature and record either `0` or `1`, respectively.

#### Feature Value Algorithm

Consult the audio sample descriptions. If the `compressionID` field in the sample descriptions is `0` or `-1`, then the audio is constant bit rate. If the field is `-2`, then the same algorithm as for video applies: if all the samples have both constant duration and constant size, then the audio is constant bit rate; otherwise it is variable.

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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/audio_variable_bit_rate_indication)*