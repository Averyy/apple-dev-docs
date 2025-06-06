# Closed captioning sample data ('cdat')

**Framework**: QuickTime File Format  
**Kind**: class

A sequence of one or more atoms that store closed captioning sample data.

#### Overview

The format of the closed captioning sample data is a sequence of one or more atoms, one of which must be a `'cdat'` atom. Unrecognized atoms should be ignored.

## Topics

### Data fields
- [Size](closed_captioning_sample_data/size.md)
  A 32-bit integer that specifies the number of bytes in this closed captioning media data atom.
- [Type](closed_captioning_sample_data/type.md)
  A 32-bit integer that identifies the atom type.
- [Sample data](closed_captioning_sample_data/sample_data.md)
  An array of one or more byte pairs for data channel 1/field 1 (“CC1”) of a CEA-608 data stream, each byte pair corresponding to a video frame.

## See Also

- [Closed captioning sample description](closed_captioning_sample_description.md)
  An atom that defines how to interpret closed captioning media data.
- [Including multiple closed-caption tracks](including_multiple_closed-caption_tracks.md)
  Include multiple closed-caption tracks in a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/closed_captioning_sample_data)*