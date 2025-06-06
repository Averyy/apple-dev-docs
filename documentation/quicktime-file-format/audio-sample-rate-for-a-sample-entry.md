# Audio sample rate for a sample entry

**Framework**: QuickTime File Format

#### Overview

#### Feature Values

This feature value is an unsigned 32-bit integer holding the audio sample rate in units per seconds (cycles per second). The value should be rounded up to the nearest integer if it has a fractional portion.

Examples: 24 kHz = `24000`, 44.1 kHz = `44100`.

#### Writer Responsibilities

A writer of the Audio Sample Rate feature should record the integer portion (rounded up if there is a fractional portion) of the audio sample rate found in a sound track’s `SoundDescription` structure.

If multiple audio sample rates are used in the movie, then either all must recorded in the profile atom, or none must be recorded.

#### Feature Value Algorithm

This is the integer portion of the sample rate from a QuickTime audio sample description (rounded up if there is a fractional portion). If the sample rate is greater than 64 kHz, the integer portion can be recorded here.

If a sample rate has a fractional portion, the writer should round up to the nearest integer. So, the `22254.54545` value that may occur in QuickTime audio as a Fixed value represented as `0x56EE8BA3` can be recorded as `22255`.

#### Reader Responsibilities

A reader of this feature code should compare the recorded value with its own audio sample rate limits. If the reader only supports discrete values (such as `44100`), it can perform equality comparisons (`=`). If the reader supports ranges of audio sample rates (such as all rates less than or equal to `32000`), the reader can perform relative comparisons (`<`, `<=`, `>`, or `>=`).

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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/audio_sample_rate_for_a_sample_entry)*