# Text box atom ('tbox')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that defines a text box for a subtitle sample.

#### Overview

This optional extension defines a text box for a subtitle sample, to be used as described in [`Sample extensions`](subtitle_sample_data/sample_extensions.md). If present, this overrides the default text box in the associated sample description. If the subtitle sample description’s Display flags do not include the Vertical Placement flag (`0x20000000`), the Text Box atom should not be included in any sample of the subtitle track.

## Topics

### Data fields
- [Size](text_box_atom/size.md)
  An unsigned 32-bit integer holding the size of the subtitle style atom.
- [Type](text_box_atom/type.md)
  An unsigned 32-bit field.
- [Text box](text_box_atom/text_box.md)
  A 64-bit rectangle that specifies an area to receive text (each 16 bits indicate top, left, bottom, and right, respectively) within the subtitle track.

## See Also

- [Subtitle sample description](subtitle_sample_description.md)
  An atom that defines how to interpret subtitle media data.
- [Font table atom ('ftab')](font_table_atom.md)
  An atom that specifies the font used to display the subtitle.
- [Subtitle sample data](subtitle_sample_data.md)
  An atom that contains subtitle sample data.
- [Subtitle style atom ('styl')](subtitle_style_atom.md)
  An atom that specifies changes to the appearance of a subtitle.
- [Subtitle track header size and placement](subtitle_track_header_size_and_placement.md)
  Specify the size and placement of subtitles.
- [Referencing a related forced subtitle track](referencing_a_related_forced_subtitle_track.md)
  Prevent overlapping a timed subtitle track with a forced subtitle track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/text_box_atom)*