# MPEG-1 media

**Framework**: QuickTime File Format

Store MPEG-1 video streams, MPEG-1, layer 2 audio streams, and multiplexed MPEG-1 audio and video streams in QuickTime movies.

#### Overview

MPEG-1 media is used to store MPEG-1 video streams, MPEG-1, layer 2 audio streams, and multiplexed MPEG-1 audio and video streams in QuickTime movies. It has a media type of `'MPEG'`.

#### Mpeg 1 Sample Description

The MPEG-1 sample description uses the standard sample description header, as described in [`Sample description atom ('stsd')`](sample_description_atom.md).

The data format field in the sample description is always set to `'MPEG'`. The MPEG-1 media handler adds no additional fields to the sample description.

> **Note**: This data format is not used for MPEG-1, layer 3 audio, however (see MPEG-1 Layer 3 (MP3) Codecs in [`Sound sample data`](sound_sample_data.md)).

This data format is not used for MPEG-1, layer 3 audio, however (see MPEG-1 Layer 3 (MP3) Codecs in [`Sound sample data`](sound_sample_data.md)).

#### Mpeg 1 Sample Data

Each sample in an MPEG-1 media is an entire MPEG-1 stream. This means that a single MPEG-1 sample may be several hundred megabytes in size. The MPEG-1 encoding used by QuickTime corresponds to the ISO standard, as described in ISO document CD 11172.

## See Also

- [Video media](video_media.md)
  Store compressed and uncompressed image data in QuickTime movies.
- [Sound media](sound_media.md)
  Store compressed and uncompressed audio data in QuickTime movies.
- [Music media](music_media.md)
  Store note-based audio data, such as MIDI data, in QuickTime movies.
- [Movie media](movie_media.md)
  Movie media is used to encapsulate embedded movies within QuickTime movies.
- [Defining media data layouts](appendix_b_defining_media_data_layouts.md)
  Use efficient media layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/mpeg-1_media)*