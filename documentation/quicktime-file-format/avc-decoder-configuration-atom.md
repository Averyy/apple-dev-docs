# AVC decoder configuration atom ('avcC')

**Framework**: Quicktime File Format  
**Kind**: class

A required extension to the video sample description for H.264 video.

#### Overview

This atom contains an MPEG-4 decoder configuration atom. This is a required extension to the video sample description for H.264 video. This extension appears in video sample descriptions only when the codec type is `‘avc1’`.

> **Note**: The decoder configuration record that this atom contains is defined in the MPEG-4 specification ISO/IEC FDIS 14496-15.

## Topics

### Data fields
- [Size](avc_decoder_configuration_atom/size.md)
  An unsigned 32-bit integer holding the size of the AVC decoder configuration atom.
- [Type](avc_decoder_configuration_atom/type.md)
  An unsigned 32-bit field.
- [AVC decoder configuration record](avc_decoder_configuration_atom/avc_decoder_configuration_record.md)
  A record that configures the AVC decoder.

## See Also

- [Pixel aspect ratio ('pasp')](pixel_aspect_ratio.md)
  An extension that specifies the height-to-width ratio of pixels found in the video sample.
- [MPEG-4 elementary stream descriptor atom ('esds')](mpeg-4_elementary_stream_descriptor_atom.md)
  A required extension to the video sample description for MPEG-4 video.
- [Color parameter atom ('colr')](color_parameter_atom.md)
  A required extension for uncompressed Y´CbCr data formats.
- [Clean aperture ('clap')](clean_aperture.md)
  An extension that defines the relationship between the pixels in a stored image and a canonical rectangular region of a video system from which it was captured or to which it will be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/avc_decoder_configuration_atom)*