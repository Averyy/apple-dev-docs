# Text sample data

**Framework**: QuickTime File Format

An atom that contains text data.

#### Overview

The format of the text data is a 16-bit length word followed by the actual text. The length word specifies the number of bytes of text, not including the length word itself. Following the text, there may be one or more atoms containing additional information for drawing and searching the text.

The following table lists the currently defined text sample extensions.

| Text sample extension | Description |
| --- | --- |
| `'styl'` | Style information for the text. Allows you to override the default style in the sample description or to define more than one style for a sample. The data is a TextEdit style scrap. |
| `'ftab'` | Table of font names. Each table entry contains a font number (stored in a 16-bit integer) and a font name (stored in a Pascal string).This atom is required if the `'styl'` atom is present. |
| `'hlit'` | Highlight information. The atom data consists of two 32-bit integers. The first contains the starting offset for the highlighted text, and the second has the ending offset. A highlight sample can be in a key frame or in a differenced frame. When it’s used in a differenced frame, the sample should contain a zero-length piece of text. |
| `'hclr'` | Highlight color. This atom specifies the 48-bit RGB color to use for highlighting. |
| `'drpo'` | Drop shadow offset. When the display flags indicate drop shadow style, this atom can be used to override the default drop shadow placement. The data consists of two 16-bit integers. The first indicates the horizontal displacement of the drop shadow, in pixels; the second, the vertical displacement. |
| `'drpt'` | Drop shadow transparency. The data is a 16-bit integer between `0` and `256` indicating the degree of transparency of the drop shadow. A value of `256` makes the drop shadow completely opaque. |
| `'imag'` | Image font data. This atom contains two more atoms. An `'idat'` atom contains compressed image data to be used to draw the text when the required fonts are not available. An `'idsc'` atom contains a video sample description describing the format of the compressed image data. |
| `'metr'` | Image font highlighting. This atom contains metric information that governs highlighting when an `'imag'` atom is used for drawing. |

## See Also

- [Text sample description](text_sample_description.md)
  An atom that defines how to interpret text media data.
- [Text media information atom ('text')](text_media_information_atom.md)
  An atom that contains information about text media.
- [Hypertext and wired text](hypertext_and_wired_text.md)
  Store hypertext in a text track sample atom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/text_sample_data)*