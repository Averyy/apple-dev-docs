# Subtitle sample description

**Framework**: QuickTime File Format  
**Kind**: class

An atom that defines how to interpret subtitle media data.

#### Overview

The subtitle sample description contains information that defines how to interpret subtitle media data. This sample description is based on the standard sample description header, as described in [`Sample description atom ('stsd')`](sample_description_atom.md).

> **Note**: Only one sample description is permitted in a `'sbtl'` track.

Only one sample description is permitted in a `'sbtl'` track.

The data format field in the sample description is currently always set to `'tx3g'`. Unrecognized data formats should be ignored. The text media described here is based on the text box defined in the 3GPP Timed Text specification but provides a different track type and media handler designed specifically for subtitles.

The subtitle media handler adds some of its own fields to the sample description.

## Topics

### Data fields
- [Display flags](subtitle_sample_description/display_flags.md)
  A 32-bit integer containing flags that describe how the subtitle text should be drawn.
- [Reserved](subtitle_sample_description/reserved.md)
  An 8-bit integer.
- [Reserved](subtitle_sample_description/reserved2.md)
  An 8-bit integer.
- [Reserved](subtitle_sample_description/reserved3.md)
  A 32-bit integer.
- [Default text box](subtitle_sample_description/default_text_box.md)
  A 64-bit rectangle that specifies an area to receive text (each 16 bits indicate top, left, bottom, and right, respectively) within the subtitle track.
- [Reserved](subtitle_sample_description/reserved4.md)
  A 32-bit value.
- [Font identifier](subtitle_sample_description/font_identifier.md)
  A 16-bit value that must be set to the same font identifier as in the font table.
- [Font face](subtitle_sample_description/font_face.md)
  An 8-bit integer that indicates the font’s style.
- [Font size](subtitle_sample_description/font_size.md)
  An 8-bit value for the font size, expressed in points.
- [Foreground color](subtitle_sample_description/foreground_color.md)
  A 32-bit RGBA color that specifies the text’s color, 8 bits each for red, green, blue, and alpha (transparency).
- [Font table](subtitle_sample_description/font_table.md)
  An atom that identifies the font to use to display the text.

## See Also

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
- [Referencing a related forced subtitle track](referencing_a_related_forced_subtitle_track.md)
  Prevent overlapping a timed subtitle track with a forced subtitle track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/subtitle_sample_description)*