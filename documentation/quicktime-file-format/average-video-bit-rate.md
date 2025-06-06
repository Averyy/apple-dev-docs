# Average video bit rate

**Framework**: QuickTime File Format

#### Overview

#### Feature Values

The value is an unsigned 32-bit integer indicating the average video bit rate in bits per second.

Example: 1 Mbps = 1000000.

#### Writer Responsibilities

A writer of the average video bit rate feature should record a value that is equal to or greater than the average bit rate for the video track, measured across all media samples. A writer (such as a CE device) may choose to record a constant value so long as that value is greater than or equal to the average bit rate that may be encoded. It is also permitted to record a value set by the video encoder during initialization so long as the value equals or exceeds the average calculated from the resulting file.

#### Feature Value Algorithm

Ideally, the long-term average: total sample sizes divided by total sample durations.

If the feature is written for a newly encoded track (as by a CE device), it is permitted to record a value used to initialize the video encoder. If the video track is edited and the average video bit rate recalculated, it may be calculated as an overall average based on the sample table.

#### Reader Responsibilities

A reader of the average video bit rate feature value should compare the recorded value with its own limits to determine if the content can be played. The reader should not perform an equality comparison (=) but instead a relative comparison (<, <=, >, or >=).

Because a writer may record a larger value than the actual video bit rate, a reader should not interpret this as the actual video bit rate. To determine the current or actual bit rate, the reader may need to perform an inspection of the video track’s sample table.

#### Comments

The value of this feature should be deducible from information found in the sample table. Track edits must be considered in its calculation. Note that for highly variable bit rate video, the average rate may not be a typical rate.

## See Also

- [Table of features](table_of_features.md)
- [Maximum video bit rate](maximum_video_bit_rate.md)
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
- [Video variable frame rate indication](video_variable_frame_rate_indication.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/average_video_bit_rate)*