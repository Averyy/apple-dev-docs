# Text media information atom ('text')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that contains information about text media.

## Mentions

- [QuickTime File Format change log](revision_history.md)

#### Overview

The text media also requires a text media information atom. This media information atom is stored in a base media information atom (`'minf'`) in the base media information header atom (`'gmhd'`) (see [`Base media information atom ('minf')`](base_media_information_atom.md)). The type of the text media information atom is `'text'`.

## Topics

### Data fields
- [Size](text_media_information_atom/size.md)
  A 32-bit integer that specifies the number of bytes in this text media information atom.
- [Type](text_media_information_atom/type.md)
  A 32-bit integer that identifies the atom type.
- [Matrix structure](text_media_information_atom/matrix_structure.md)
  A matrix structure associated with this text media.

## See Also

- [Text sample description](text_sample_description.md)
  An atom that defines how to interpret text media data.
- [Text sample data](text_sample_data.md)
  An atom that contains text data.
- [Hypertext and wired text](hypertext_and_wired_text.md)
  Store hypertext in a text track sample atom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/text_media_information_atom)*