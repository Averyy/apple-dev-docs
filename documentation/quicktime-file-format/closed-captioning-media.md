# Closed captioning media

**Framework**: QuickTime File Format

Store closed captioning for QuickTime movies.

#### Overview

A closed caption media track contains text data used for closed captioning in QuickTime movies. It has a media type of `'clcp'`. Closed captions are used to display the audio portions of a movie as text. They transcribe dialog and indicate other sounds.

Other tracks can identify this track as being a related closed captioning track by using the `'clcp'` track reference to refer to this track.

Like other media data tracks, a closed caption track should include a language code and an extended language tag atom.

## Topics

### Storing closed captioning
- [Closed captioning sample description](closed_captioning_sample_description.md)
  An atom that defines how to interpret closed captioning media data.
- [Closed captioning sample data ('cdat')](closed_captioning_sample_data.md)
  A sequence of one or more atoms that store closed captioning sample data.
- [Including multiple closed-caption tracks](including_multiple_closed-caption_tracks.md)
  Include multiple closed-caption tracks in a movie.

## See Also

- [Text media](text_media.md)
  Store text data in QuickTime movies.
- [Subtitle media](subtitle_media.md)
  Store text data used for subtitles in QuickTime movies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/closed_captioning_media)*