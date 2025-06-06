# Maximum video bit rate

**Framework**: QuickTime File Format

#### Overview

#### Feature Values

The value is an unsigned 32-bit integer indicating the maximum video bit rate in bits per second. The value may be larger than the actual video bit rate, so it should not be interpreted as a bit rate that will actually occur.

Example: 1 Mbps = 1000000.

#### Writer Responsibilities

A writer of the maximum video bit rate should record a value that is equal to or greater than the actual bit rate for the video track. A writer (such as a CE device) may choose to record a constant value so long as that value is greater than or equal to the bit rate that may be encoded. It is also permitted to record a value set by the video encoder during initialization, so long as the value is never exceeded.

#### Feature Value Algorithm

Apple recommends a sliding average over 1 second calculated from the sample tables.

If the feature is written for a newly encoded track (as by a CE device), it is permitted to record a value used to initialize the video encoder so long as the value is never exceeded. If the video track is edited and the maximum video bit rate recalculated, it may be calculated as a sliding average over 1 second, based on the sample table.

This can be calculated in the following manner:

1. For each sample, calculate the average 1-second bit rate; choose the shortest run of samples, including the candidate sample, that comprise 1 second or more of video, then divide the total data size of those samples by their total duration.
2. Choose the maximum value from the list of calculated 1-second averages.

#### Reader Responsibilities

A reader of the maximum video bit rate feature value should compare the recorded value with its own limits to determine if the content can be played. The reader should not perform an equality comparison (=) but instead a relative comparison (<, <=, >, or >=).

The recorded value may be larger than the actual maximum video bit rate. Since this value may be an over-estimate, the reader should not use it as a basis for refusing to play the file, though a warning may be appropriate. To determine the actual bit rate, the reader may need to perform an inspection of the video track’s sample table.

#### Comments

The value of this feature should be deducible from information found in the sample table. Track edits must be considered in its calculation; if the track is edited, this value must be recalculated. Even though this value may exceed the actual maximum video bit rate, writers should attempt to minimize any over-estimation.

## See Also

- [Table of features](table_of_features.md)
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
- [Video variable frame rate indication](video_variable_frame_rate_indication.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/maximum_video_bit_rate)*