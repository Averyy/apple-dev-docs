# Universal features

**Framework**: QuickTime File Format

Features that you include in any file that includes a profile atom.

#### Overview

A feature consists of four fields: a reserved field, which is set to zero; a part-ID, which specifies which brand the feature belongs to; a feature code, which identifies the feature; and a value field, which holds the feature value).

The part-ID can be either universal or brand-specific. Universal features have a part-ID of four ASCII spaces (`0x20202020`). Brand-specific features have a part-ID for a particular brand, which is taken from the Compatible_brands field of the file type atom. Brand-specific features of QuickTime files have a part-ID of `'qt  '`. All features listed in this section are universal features; that is, they can be used in any file that includes a profile atom.

It is permissible to use the feature code of `0x00000000` as a placeholder, paired with a feature value of `0x00000000` for one or more features. Readers should simply ignore features having a feature code of zero.

No feature will exist to describe the unit of other features, such as bit rate. The device should consider the magnitude and tailor its display appropriately.

This specification describes only how features are stored in files. It does not require that the values of features be reported (for example, in a user interface) in the same manner as they are stored, or require that they be reported at all.

## Topics

### Setting features
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
- [Video variable frame rate indication](video_variable_frame_rate_indication.md)
- [Audio sample rate for a sample entry](audio_sample_rate_for_a_sample_entry.md)
- [Audio variable bit rate indication](audio_variable_bit_rate_indication.md)
- [Audio channel count](audio_channel_count.md)

## See Also

- [About this appendix](about_this_appendix.md)
- [Profile atom ('prfl')](profile_atom.md)
  An atom that expresses profiles or feature codes for features that occur in the movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/universal_features)*