# Average audio bit rate

**Framework**: QuickTime File Format

#### Overview

#### Feature Values

The value is an unsigned 32-bit integer indicating the average audio bit rate in bits per second.

Example: 128 kbps = 128000.

#### Writer Responsibilities

A writer of the average audio bit rate feature should record a value that is equal to or greater than the average bit rate for the sound track, measured across all media samples. A writer (such as a CE device) may choose to record a constant value so long as that value is greater than or equal to the average bit rate that may be encoded. It is also permitted to record a value set by the audio encoder during initialization so long as the value is never exceeded on average.

#### Feature Value Algorithm

Normally, the long-term average: total sample sizes divided by total sample durations.

If the feature is written for a newly encoded track (as by a CE device), it is permitted to record a value used to initialize the audio encoder. If the sound track is edited and the average video bit rate recalculated, it may be calculated as an overall average based on the sample table.

#### Reader Responsibilities

A reader of the average audio bit rate feature value should compare the recorded value with its own limits to determine if the content can be played. The reader should not perform an equality comparison (=) but instead a relative comparison (<, <=, >, or >=).

#### Comments

The value of this feature should be deducible from information found in the sample table. Track edits normally need not be considered in the calculation for constant bit rate audio, but must be considered for variable bit rate audio or when track or movie segments containing constant bit rate audio are edited to alter their duration.

## See Also

- [Table of features](table_of_features.md)
- [Maximum video bit rate](maximum_video_bit_rate.md)
- [Average video bit rate](average_video_bit_rate.md)
- [Maximum audio bit rate](maximum_audio_bit_rate.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/average_audio_bit_rate)*