# Audio channel count

**Framework**: QuickTime File Format

#### Overview

#### Feature Values

The feature value is an unsigned 32-bit integer holding the number of audio channels encoded by a Sound Track in the movie. For monaural, the value would be `1`. For stereo, the value would be `2`. Note that the audio channel count is a standard field in the sound sample description.

#### Writer Responsibilities

A writer of the Audio Channel Count feature should determine the number of audio channels encoded in the sound track or tracks of the movie.

#### Feature Value Algorithm

Consult the audio sample descriptions.

#### Reader Responsibilities

The reader should be prepared to either play the specified number of channels or to map the audio to the number of channels the reader supports (for example, mixing down stereo sound for a monaural speaker).

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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/audio_channel_count)*