# Pixel aspect ratio ('pasp')

**Framework**: QuickTime File Format  
**Kind**: class

An extension that specifies the height-to-width ratio of pixels found in the video sample.

## Mentions

- [QuickTime File Format change log](revision_history.md)
- [Video sample data](video_sample_data.md)

#### Overview

This is a required extension for MPEG-4 and uncompressed Y´CbCr video formats when non-square pixels are used. It is optional when square pixels are used.

The units of measure for the `hSpacing` and `vSpacing` parameters are not specified, as only the ratio matters. The units of measure for height and width must be the same, however.

The following table shows some common pixel aspect ratios.

| Description | hSpacing | vSpacing |
| --- | --- | --- |
| 4:3 square pixels (composite NTSC or PAL) | `1` | `1` |
| 4:3 non-square 525 (NTSC) | `10` | `11` |
| 4:3 non-square 625 (PAL) | `59` | `54` |
| 16:9 analog (composite NTSC or PAL) | `4` | `3` |
| 16:9 digital 525 (NTSC) | `40` | `33` |
| 16:9 digital 625 (PAL) | `118` | `81` |
| 1920x1035 HDTV (per SMPTE 260M-1992) | `113` | `118` |
| 1920x1035 HDTV (per SMPTE RP 187-1995) | `1018` | `1062` |
| 1920x1080 HDTV or 1280x720 HDTV | `1` | `1` |

## Topics

### Data fields
- [Size](pixel_aspect_ratio/size.md)
  An unsigned 32-bit integer holding the size of the pixel aspect ratio atom.
- [Type](pixel_aspect_ratio/type.md)
  An unsigned 32-bit field.
- [hSpacing](pixel_aspect_ratio/hspacing.md)
  An unsigned 32-bit integer specifying the horizontal spacing of pixels, such as luma sampling instants for Y´CbCr or YUV video.
- [vSpacing](pixel_aspect_ratio/vspacing.md)
  An unsigned 32-bit integer specifying the vertical spacing of pixels, such as video picture lines.

## See Also

- [MPEG-4 elementary stream descriptor atom ('esds')](mpeg-4_elementary_stream_descriptor_atom.md)
  A required extension to the video sample description for MPEG-4 video.
- [AVC decoder configuration atom ('avcC')](avc_decoder_configuration_atom.md)
  A required extension to the video sample description for H.264 video.
- [Color parameter atom ('colr')](color_parameter_atom.md)
  A required extension for uncompressed Y´CbCr data formats.
- [Clean aperture ('clap')](clean_aperture.md)
  An extension that defines the relationship between the pixels in a stored image and a canonical rectangular region of a video system from which it was captured or to which it will be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/pixel_aspect_ratio)*