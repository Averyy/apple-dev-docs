# Subtitle style atom ('styl')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies changes to the appearance of a subtitle.

#### Overview

This extension specifies changes to the appearance of a subtitle. The style information in the subtitle sample description provides the default style for the subtitle text. This extension allows you to override the default style for different parts, or all, of the subtitle text.

## Topics

### Data fields
- [Size](subtitle_style_atom/size.md)
  An unsigned 32-bit integer holding the size of the subtitle style atom.
- [Type](subtitle_style_atom/type.md)
  An unsigned 32-bit field.
- [Entry count](subtitle_style_atom/entry_count.md)
  An unsigned 16-bit integer specifying how many subtitle text style records follow this entry count.
- [Subtitle text style record](subtitle_style_atom/subtitle_text_style_record.md)
  One or more records that provide details about the subtitle’s style.

## See Also

- [Subtitle sample description](subtitle_sample_description.md)
  An atom that defines how to interpret subtitle media data.
- [Font table atom ('ftab')](font_table_atom.md)
  An atom that specifies the font used to display the subtitle.
- [Subtitle sample data](subtitle_sample_data.md)
  An atom that contains subtitle sample data.
- [Text box atom ('tbox')](text_box_atom.md)
  An atom that defines a text box for a subtitle sample.
- [Subtitle track header size and placement](subtitle_track_header_size_and_placement.md)
  Specify the size and placement of subtitles.
- [Referencing a related forced subtitle track](referencing_a_related_forced_subtitle_track.md)
  Prevent overlapping a timed subtitle track with a forced subtitle track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/subtitle_style_atom)*