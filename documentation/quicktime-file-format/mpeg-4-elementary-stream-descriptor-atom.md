# MPEG-4 elementary stream descriptor atom ('esds')

**Framework**: QuickTime File Format  
**Kind**: class

A required extension to the video sample description for MPEG-4 video.

## Mentions

- [Video sample data](video_sample_data.md)
- [QuickTime File Format change log](revision_history.md)

#### Overview

This atom contains an MPEG-4 elementary stream descriptor atom. This is a required extension to the video sample description for MPEG-4 video. This extension appears in video sample descriptions only when the codec type is `'mp4v'`.

> **Note**: The elementary stream descriptor which this atom contains is defined in the MPEG-4 specification ISO/IEC FDIS 14496-1.

The elementary stream descriptor which this atom contains is defined in the MPEG-4 specification ISO/IEC FDIS 14496-1.

## Topics

### Data fields
- [Size](mpeg-4_elementary_stream_descriptor_atom/size.md)
  An unsigned 32-bit integer holding the size of the elementary stream descriptor atom.
- [Type](mpeg-4_elementary_stream_descriptor_atom/type.md)
  An unsigned 32-bit field.
- [Version](mpeg-4_elementary_stream_descriptor_atom/version.md)
  An unsigned 8-bit integer set to zero.
- [Flags](mpeg-4_elementary_stream_descriptor_atom/flags.md)
  A 24-bit field reserved for flags, currently set to zero.
- [Elementary stream descriptor](mpeg-4_elementary_stream_descriptor_atom/elementary_stream_descriptor.md)
  An elementary stream descriptor for MPEG-4 video.

## See Also

- [Pixel aspect ratio ('pasp')](pixel_aspect_ratio.md)
  An extension that specifies the height-to-width ratio of pixels found in the video sample.
- [AVC decoder configuration atom ('avcC')](avc_decoder_configuration_atom.md)
  A required extension to the video sample description for H.264 video.
- [Color parameter atom ('colr')](color_parameter_atom.md)
  A required extension for uncompressed Y´CbCr data formats.
- [Clean aperture ('clap')](clean_aperture.md)
  An extension that defines the relationship between the pixels in a stored image and a canonical rectangular region of a video system from which it was captured or to which it will be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/mpeg-4_elementary_stream_descriptor_atom)*