# QuickTime audio codec type

**Framework**: QuickTime File Format

#### Overview

#### Feature Values

This is the four-character-code found in a sound sample description.

Examples: `'mp4a'`, `'twos'`.

#### Writer Responsibilities

A writer of the QuickTime audio codec type feature should record the four-character-code corresponding to the QuickTime audio format type or types also recorded in the sound track’s sample descriptions.

> **Note**: A writer that records the QuickTime Audio Codec type for the `'mp4a'` codec is encouraged also to write the MPEG-4 Audio Codec feature.

#### Feature Value Algorithm

The feature value is the audio codec type read from a `SoundDescription` structure’s `dataFormat` field. If there are multiple sample descriptions with different audio codec types, either all QuickTime Audio Codec Type features must be recorded in the profile atom or none must be recorded.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value by an equality comparison (using =) with the format codes supported by the reader.

## See Also

- [Table of features](table_of_features.md)
- [Maximum video bit rate](maximum_video_bit_rate.md)
- [Average video bit rate](average_video_bit_rate.md)
- [Maximum audio bit rate](maximum_audio_bit_rate.md)
- [Average audio bit rate](average_audio_bit_rate.md)
- [QuickTime video codec type](quicktime_video_codec_type.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/quicktime_audio_codec_type)*