# Text sample description

**Framework**: QuickTime File Format  
**Kind**: class

An atom that defines how to interpret text media data.

#### Overview

The text sample description contains information that defines how to interpret text media data. This sample description is based on the standard sample description header, as described in [`Sample description atom ('stsd')`](sample_description_atom.md).

The data format field in the sample description is always set to `'text'`.

The text media handler also adds some of its own fields to the sample description.

## Topics

### Data fields
- [Display flags](text_sample_description/display_flags.md)
  A 32-bit integer containing flags that describe how the text should be drawn.
- [Text justification](text_sample_description/text_justification.md)
  A 32-bit integer that indicates how the text should be aligned.
- [Background color](text_sample_description/background_color.md)
  A 48-bit RGB color that specifies the text’s background color.
- [Default text box](text_sample_description/default_text_box.md)
  A 64-bit rectangle that specifies an area to receive text (top, left, bottom, right).
- [Reserved](text_sample_description/reserved.md)
  A 64-bit value.
- [Font number](text_sample_description/font_number.md)
  A 16-bit value.
- [Font face](text_sample_description/font_face.md)
  A 16-bit integer that indicates the font’s style.
- [Reserved](text_sample_description/reserved2.md)
  An 8-bit value.
- [Reserved](text_sample_description/reserved3.md)
  A 16-bit value.
- [Foreground color](text_sample_description/foreground_color.md)
  A 48-bit RGB color that specifies the text’s foreground color.
- [Text name](text_sample_description/text_name.md)
  A Pascal string specifying the name of the font to use to display the text.

## See Also

- [Text media information atom ('text')](text_media_information_atom.md)
  An atom that contains information about text media.
- [Text sample data](text_sample_data.md)
  An atom that contains text data.
- [Hypertext and wired text](hypertext_and_wired_text.md)
  Store hypertext in a text track sample atom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/text_sample_description)*