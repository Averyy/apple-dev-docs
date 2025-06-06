# Maximum video size in a track

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

A writer of the Maximum Track Video Size feature should record a value that is equal to or greater than the largest height and width of any sample description in the video track. This does not include the effect of any scaling or offset applied by the track matrix and may not be the same as the track height and track width.

A writer (such as a CE device) may choose to record a constant size based upon its current recording mode even if the actual size recorded in the track is smaller.

#### Feature Value Algorithm

Examine all sample descriptions for the track, and use the maximum width and maximum height found in any sample. The maximum width and maximum height may come from independent sample descriptions.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value with its own image buffer limits.

The reader should not interpret the value of this feature as the current video size. To determine the current video size, the reader should use the dimensions of all currently displaying video tracks, their matrices, and the movie matrix.

#### Comments

The width and height correspond to the largest image buffer dimensions needed for a visual track. When present in a movie-level profile, these atoms document the maximum video size found in each of the movie’s tracks.

The summarized width and height do not take into account any scaling or translation caused by the track or movie matrices, and are not necessarily the same as the track height and width.

For the case where there is a single video track with an identity track and matrix and an identity movie matrix, the movie’s maximum video size feature would have the same value as the track’s feature.

> ⚠️ **Warning**: Use of the “clean aperture” sample description extension does not affect the value of the track visual size, as the picture buffer is needed immediately after decoding, prior to any clean aperture clipping.

Use of the “clean aperture” sample description extension does not affect the value of the track visual size, as the picture buffer is needed immediately after decoding, prior to any clean aperture clipping.

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
- [Maximum video frame rate in a single track](maximum_video_frame_rate_in_a_single_track.md)
- [Average video frame rate in a single track](average_video_frame_rate_in_a_single_track.md)
- [Video variable frame rate indication](video_variable_frame_rate_indication.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/maximum_video_size_in_a_track)*