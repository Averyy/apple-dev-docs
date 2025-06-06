# Media data atom types

**Framework**: QuickTime File Format

Store different types of media data, including video, sound, subtitles, and more.

#### Overview

QuickTime uses atoms of different types to store different types of media data—video media atoms for video data, sound media atoms for audio data, and so on. Review the following topics to understand the fundamentals of how QuickTime uses atoms for storage of different types of media data.

## Topics

### Video and sound
- [Video media](video_media.md)
  Store compressed and uncompressed image data in QuickTime movies.
- [Sound media](sound_media.md)
  Store compressed and uncompressed audio data in QuickTime movies.
- [Music media](music_media.md)
  Store note-based audio data, such as MIDI data, in QuickTime movies.
- [MPEG-1 media](mpeg-1_media.md)
  Store MPEG-1 video streams, MPEG-1, layer 2 audio streams, and multiplexed MPEG-1 audio and video streams in QuickTime movies.
- [Movie media](movie_media.md)
  Movie media is used to encapsulate embedded movies within QuickTime movies.
- [Defining media data layouts](appendix_b_defining_media_data_layouts.md)
  Use efficient media layouts.
### Time-specific media
- [Timed metadata media](timed_metadata_media.md)
  Store timed metadata in QuickTime movies with a track structure.
- [Timecode media](timecode_media.md)
  Store time code data in QuickTime movies with timecode media.
### Text, captions, and subtitles
- [Text media](text_media.md)
  Store text data in QuickTime movies.
- [Closed captioning media](closed_captioning_media.md)
  Store closed captioning for QuickTime movies.
- [Subtitle media](subtitle_media.md)
  Store text data used for subtitles in QuickTime movies.
### Track features
- [Modifier tracks](modifier_tracks.md)
  Create dynamic movies with modifier tracks that send data to another track.
- [Creating movies with modifier tracks](creating_movies_with_modifier_tracks.md)
  Send data to another media handler instead of presenting media directly.
- [Track references](track_references.md)
  Relate a movie’s tracks to one another with track references.
- [Chapter lists](chapter_lists.md)
  A chapter list provides a set of named entry points into a movie.
- [Streaming media](streaming_media.md)
  Store streaming data in a streaming media track for QuickTime movies.
### Hint media
- [Hint media](hint_media.md)
  Provide information about data units to stream in hint tracks.
- [Finding an original media track from a hint track](finding_an_original_media_track_from_a_hint_track.md)
  Use track reference atoms from hint tracks to locate the original media track.
- [RTP hint tracks](rtp_hint_tracks.md)
  Allow a streaming server to create RTP streams from a QuickTime movie.
- [Hint track sample description](hint_track_sample_description.md)
  An atom that specifies the data format and location of the hint track sample data.
- [Packetization hint sample data](packetization_hint_sample_data.md)
  An atom that describes the sample data for data using the Real-Time Transport Protocol (RTP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/media_data_atom_types)*