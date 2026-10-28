# Depth

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A 16-bit integer that indicates the pixel depth of the compressed image.

## Overview

Values of 1, 2, 4, 8 ,16, 24, and 32 indicate the depth of color images. The value 32 should be used only if the image contains an alpha channel. Values of 34, 36, and 40 indicate 2-, 4-, and 8-bit grayscale, respectively, for grayscale images.

## See Also

### Data fields
- [Sample description size](./sample_description_size.md)
  A 32-bit integer indicating the number of bytes in the sample description.
- [Data format](./data_format.md)
  A 32-bit integer indicating the format of the stored data.
- [Reserved](./reserved.md)
  Six bytes.
- [Data reference index](./data_reference_index.md)
  A 16-bit integer that contains the index of the data reference to use to retrieve data associated with samples that use this sample description.
- [Version](./version.md)
  A 16-bit integer indicating the version number of the compressed data.
- [Revision level](./revision_level.md)
  A 16-bit integer.
- [Vendor](./vendor.md)
  A 32-bit integer that specifies the developer of the compressor that generated the compressed data.
- [Temporal quality](./temporal_quality.md)
  A 32-bit integer that indicates the degree of temporal compression.
- [Spatial quality](./spatial_quality.md)
  A 32-bit integer that indicates the degree of spatial compression.
- [Width](./width.md)
  A 16-bit integer that specifies the width of the source image in pixels.
- [Height](./height.md)
  A 16-bit integer that specifies the height of the source image in pixels.
- [Horizontal resolution](./horizontal_resolution.md)
  A 32-bit fixed-point number containing the horizontal resolution of the image in pixels per inch.
- [Vertical resolution](./vertical_resolution.md)
  A 32-bit fixed-point number containing the vertical resolution of the image in pixels per inch.
- [Data size](./data_size.md)
  A 32-bit integer.
- [Frame count](./frame_count.md)
  A 16-bit integer that indicates how many frames of compressed data are stored in each sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/video_sample_description/depth)*