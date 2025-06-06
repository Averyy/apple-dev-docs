# Subtitle sample data

**Framework**: QuickTime File Format  
**Kind**: class

An atom that contains subtitle sample data.

## Mentions

- [Preparing sound and subtitle alternate groups for use with Apple devices](preparing_sound_and_subtitle_alternate_groups_for_use_with_apple_devices.md)

#### Overview

Subtitle sample data consists of a 16-bit word that specifies the length (number of bytes) of the subtitle text, followed by the subtitle text and then by optional sample extensions. The subtitle text is Unicode text, encoded either as UTF-8 text or UTF-16 text beginning with a UTF-16 BYTE ORDER MARK (`'\uFEFF'`) in big or little endian order. There is no null termination for the text.

Following the subtitle text, there may be one or more atoms containing additional information for selecting and drawing the subtitle.

## Topics

### Data fields
- [Text size](subtitle_sample_data/text_size.md)
  A 16-bit word that specifies the length (number of bytes) of the subtitle text.
- [Text](subtitle_sample_data/text.md)
  The subtitle text.
- [Sample extensions](subtitle_sample_data/sample_extensions.md)
  One or more atoms containing additional information for selecting and drawing the subtitle.

## See Also

- [Subtitle sample description](subtitle_sample_description.md)
  An atom that defines how to interpret subtitle media data.
- [Font table atom ('ftab')](font_table_atom.md)
  An atom that specifies the font used to display the subtitle.
- [Subtitle style atom ('styl')](subtitle_style_atom.md)
  An atom that specifies changes to the appearance of a subtitle.
- [Text box atom ('tbox')](text_box_atom.md)
  An atom that defines a text box for a subtitle sample.
- [Subtitle track header size and placement](subtitle_track_header_size_and_placement.md)
  Specify the size and placement of subtitles.
- [Referencing a related forced subtitle track](referencing_a_related_forced_subtitle_track.md)
  Prevent overlapping a timed subtitle track with a forced subtitle track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/subtitle_sample_data)*