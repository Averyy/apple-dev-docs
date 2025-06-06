# Text box

**Framework**: QuickTime File Format  
**Kind**: property

A 64-bit rectangle that specifies an area to receive text (each 16 bits indicate top, left, bottom, and right, respectively) within the subtitle track.

#### Overview

This rectangle must fill the track width dimensions exactly. The top and bottom coordinates can vary because they are used to place and size the subtitle text vertically. The top is used to place the text; the height is determined by the bottom minus the top. Neither the top nor the bottom should be outside the subtitle track dimensions. See [`Subtitle track header size and placement`](subtitle_track_header_size_and_placement.md).

## See Also

- [Size](text_box_atom/size.md)
  An unsigned 32-bit integer holding the size of the subtitle style atom.
- [Type](text_box_atom/type.md)
  An unsigned 32-bit field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/text_box_atom/text_box)*