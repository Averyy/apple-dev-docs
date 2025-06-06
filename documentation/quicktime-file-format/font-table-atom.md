# Font table atom ('ftab')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies the font used to display the subtitle.

## Topics

### Data fields
- [Size](font_table_atom/size.md)
  An unsigned 32-bit integer holding the size of the font table atom.
- [Type](font_table_atom/type.md)
  An unsigned 32-bit field.
- [Count](font_table_atom/count.md)
  An unsigned 16-bit integer specifying how many fonts are described in this table.
- [Font identifier](font_table_atom/font_identifier.md)
  An unsigned 16-bit integer that identifies the font.
- [Font name length](font_table_atom/font_name_length.md)
  An unsigned 8-bit integer specifying the length of the font name in bytes.
- [Font name](font_table_atom/font_name.md)
  Must be either “Serif” or “Sans-Serif”.

## See Also

- [Subtitle sample description](subtitle_sample_description.md)
  An atom that defines how to interpret subtitle media data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/font_table_atom)*