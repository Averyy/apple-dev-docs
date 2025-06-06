# Maximum video frame rate in a single track

**Framework**: QuickTime File Format

#### Overview

#### Feature Values

This is an unsigned fixed-point (16.16) number holding the maximum video frame rate. The integer portion of the number can range from `0` to `65535`.

Examples: 25 fps = `0x00190000`; 24 fps = `0x00180000`; 29.97 = `0x001DF853` (close approximation of a 30000/1001 ratio). The value may be rounded up to the nearest integer.

#### Writer Responsibilities

A writer of the Maximum Video Frame Rate feature should record a 16.16 fixed-point value that is equal to or greater than the current video frame rate. A writer (such as a CE device) may choose to record a constant for the feature based on its current recording mode, even if the actual frame rate is less.

A writer of a new video track (such as a CE device recorder) may set the maximum frame rate feature value to a value set during video encoder initialization, so long as this frame rate is never exceeded.

If the current calculated frame rate is fractional (such as 22.3 fps), a writer may choose to round the value up to the nearest integer value (such as 23.0 fps for 22.3 fps).

A writer calculating the video frame rate using the video track’s sample table should not consider the first or the last sample duration if they differ from the other sample durations. The reason for this is that captured movie files often have longer or shorter first and last sample durations. By not considering them in the calculation, a more accurate calculation is achieved.

#### Feature Value Algorithm

This feature value may be calculated as the inverse of the smallest sample duration in the video track or tracks.

If the value is written for a newly recorded video track it may be a value established during initialization of the video encoder, so long as the frame rate is not exceeded.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value with its own video frame rate limits. It should not expect exact values.

The reader should not interpret the value of this feature as the current frame rate. To determine the current frame rate, the reader should use the video track’s sample table.

#### Comments

A writer may choose to round up any fractional value of the fixed-point number to the nearest 16-bit integer leaving the lower 16 bits of the Fixed value set to `0`. So, in the case of the 29.97 approximation of `0x001DF853`, the writer could round this up to `0x001E0000` (which equals 30).

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
- [Average video frame rate in a single track](average_video_frame_rate_in_a_single_track.md)
- [Video variable frame rate indication](video_variable_frame_rate_indication.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/maximum_video_frame_rate_in_a_single_track)*