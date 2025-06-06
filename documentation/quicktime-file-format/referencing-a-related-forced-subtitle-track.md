# Referencing a related forced subtitle track

**Framework**: Quicktime File Format

Prevent overlapping a timed subtitle track with a forced subtitle track.

#### Overview

A subtitle track can contain a track reference of type `'forc'` to a paired subtitle track that contains only forced subtitles.

Pairing two subtitle tracks might be necessary if the timing of forced subtitle samples (see `'frcd'`) differs from the regular subtitle text, such as when a forced subtitle display would overlap in time with the display of the regular subtitle. If timings are the same, a single subtitle track should be used.

To pair two tracks, one subtitle track can contain any combination of forced and non-forced (regular) subtitle samples and the other track must contain only forced subtitles. The tracks must be in the same alternate group and be tagged with the same extended language tag and language code. The first, regular track then uses a track reference of type `'forc'` to reference the second, forced-only track. (Mixing extended language tags or codes for the same language in the same alternate group is undefined.)

> **Note**: The regular track in a pair provides a complete transcription of the audio as subtitle text. This allows a user to listen in one language but to read subtitled dialogue in another language.

See [`Preparing sound and subtitle alternate groups for use with Apple devices`](preparing_sound_and_subtitle_alternate_groups_for_use_with_apple_devices.md) and [`Track reference atom ('tref')`](track_reference_atom.md) for more information.

## See Also

- [Subtitle sample description](subtitle_sample_description.md)
  An atom that defines how to interpret subtitle media data.
- [Font table atom ('ftab')](font_table_atom.md)
  An atom that specifies the font used to display the subtitle.
- [Subtitle sample data](subtitle_sample_data.md)
  An atom that contains subtitle sample data.
- [Subtitle style atom ('styl')](subtitle_style_atom.md)
  An atom that specifies changes to the appearance of a subtitle.
- [Text box atom ('tbox')](text_box_atom.md)
  An atom that defines a text box for a subtitle sample.
- [Subtitle track header size and placement](subtitle_track_header_size_and_placement.md)
  Specify the size and placement of subtitles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/referencing_a_related_forced_subtitle_track)*