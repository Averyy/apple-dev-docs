# Maximum video size in a movie

**Framework**: QuickTime File Format

#### Overview

#### Feature Values

A packed structure in a 32-bit value:

```c
struct {
    unsigned integer(16) width;
    unsigned integer(16) height;
};
```

In big-endian order, the top 16 bits correspond to the width. The lower 16 bits correspond to the height.

#### Writer Responsibilities

A writer of the Maximum Movie Video Size feature should record a value that is equal to or greater than the display size needed by the movie—the actual width and height needed to display the movie at its normal size, taking into account all matrices (all track matrices and the movie matrix).

A writer (such as a CE device) may choose to record a constant size based upon its current recording mode even if the actual size recorded in the movie is smaller.

#### Feature Value Algorithm

This value is calculated by examining the dimensions of all visual tracks and computing the maximum combined dimensions, including the effect of track matrices and the movie matrix. For example, if two video tracks play side-by-side in the movie, and the tracks and movie all use the identity matrix, this value will be the largest of the two tracks’ heights and their combined width.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value with its own video size limits.

The reader should not interpret the value of this feature as the current video size. To determine the current video size, the reader should use the dimensions of all currently displaying video tracks, their matrices, and the movie matrix.

#### Comments

The width and height correspond to the maximum visual area needed to display the movie.

The summarized width and height should take into account all components of all track matrices and the movie matrix. The goal is to understand the maximum contribution of all tracks to the movie’s bounds.

For the case where there is a single video track with an identity track matrix, the movie’s maximum video size feature would typically have the same value as the track’s maximum video size feature.

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
- [Maximum video size in a track](maximum_video_size_in_a_track.md)
- [Maximum video frame rate in a single track](maximum_video_frame_rate_in_a_single_track.md)
- [Average video frame rate in a single track](average_video_frame_rate_in_a_single_track.md)
- [Video variable frame rate indication](video_variable_frame_rate_indication.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/maximum_video_size_in_a_movie)*