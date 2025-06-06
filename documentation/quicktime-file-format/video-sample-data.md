# Video sample data

**Framework**: Quicktime File Format

Store video sample data in different formats, depending on the type of compression you use.

#### Overview

The format of the data stored in video samples is completely dependent on the type of the compression used, as indicated in the video sample description. The following sections discuss some of the video encoding schemes supported by QuickTime.

#### Uncompressed Rgb

Uncompressed RGB data is stored in a variety of different formats. The format used depends on the depth field of the video sample description. For all depths, the image data is padded on each scan line to ensure that each scan line begins on an even byte boundary.

- For depths of 1, 2, 4, and 8, the values stored are indexes into the color table specified in the color table ID field.
- For a depth of 16, the pixels are stored as 5-5-5 RGB values with the high bit of each 16-bit integer set to `0`.
- For a depth of 24, the pixels are stored packed together in RGB order.
- For a depth of 32, the pixels are stored with an 8-bit alpha channel, followed by 8-bit RGB components.

RGB data can be stored in composite or planar format. Composite format stores the RGB data for each pixel contiguously, while planar format stores the R, G, and B data separately, so the RGB information for a given pixel is found using the same offset into multiple tables. For example, the data for two pixels could be represented in composite format as RGB-RGB or in planar format as RR-GG-BB.

#### Uncompressed Y%c2%b4cbcr Including Yuv2

The Y´CbCr color space is widely used for digital video. In this data format, luminance is stored as a single value (Y), and chrominance information is stored as two color-difference components (Cb and Cr). Cb is the difference between the blue component and a reference value; Cr is the difference between the red component and a reference value.

This is commonly referred to as “YUV” format, with “U” standing-in for Cb and “V” standing-in for Cr. This usage is not strictly correct, as YUV, YIC, and Y´CbCr are distinct color models for PAL, NTSC, and digital video, but most Y´CbCr data formats and codecs are described or even named as some variant of “YUV.”

The values of Y, Cb, and Cr can be represented using a variety of bit depths, trading off accuracy for file size. Similarly, the chrominance values can be subsampled, recording only one pixel’s color value out of two, for example, or averaging the color value of adjacent pixels. This subsampling is a form of compression, but if no additional lossy compression is performed on the sampled video, it is still referred to as “uncompressed” Y´CbCr video. In addition, a fourth component can be added to Y´CbCr video to record an alpha channel.

The number of components (Y´CbCr with or without alpha) and any subsampling are denoted using ratios of three or four numbers, such as 4:2:2 to indicate 4 bits of Y to 2 bits each of Cb and Cr (chroma subsampling), or 4:4:4 for equal storage of Y, Cb, and Cr (no subsampling), or 4:4:4:4 for Y´CbCr plus alpha with no subsampling. The ratios do not typically denote actual bit depths.

Uncompressed Y´CbCr video data is typically stored as follows:

- Y´, Cb, and Cr components of each line are stored spatially left to right and temporally from earliest to latest.
- The lines of a field or frame are stored spatially top to bottom and temporally earliest to latest.
- Y´ is an unsigned integer. Cb and Cr are twos-complement signed integers.

The yuv2 stream, for example, is encoded in a series of 4-byte packets. Each packet represents two adjacent pixels on the same scan line. The bytes within each packet are ordered as follows:

```None
y0 u y1 v
```

`y0` is the luminance value for the left pixel; `y1` the luminance for the right pixel. `u` and `v` are chromatic values that are shared by both pixels.

Accurate conversion between RGB and Y´CbCr color spaces requires a computation for each component of each pixel. An example conversion from yuv2 into RGB is represented by the following equations:

```None
r = 1.402 * v + y + .5

g = y - .7143 * v - .3437 * u + .5

b = 1.77 * u + y + .5
```

The `r`, `g`, and `b` values range from `0` to `255`.

The coefficients in these equations are derived from matrix operations and depend on the reference values used for the primary colors and for white. QuickTime uses canonical values for these reference coefficients based on published standards. The sample description extension for Y´CbCr formats includes a `'colr'` atom, which contains indexes into a table of canonical references. This provides support for multiple video standards without opening the door to data entry errors for stored coefficient values. Refer to the published standards for the formulas and methods used to derive conversion coefficients from the table entries.

#### Jpeg

QuickTime stores JPEG images according to the rules described in the ISO JPEG specification, document number DIS 10918-1.

#### Mpeg 4 Video

MPEG-4 video uses the `'mp4v'` data format. The sample description requires the elementary stream descriptor (‘esds’) extension to the standard video sample description. If non-square pixels are used, the pixel aspect ratio (`'pasp'`) extension is also required. For details on these extensions, see [`Pixel aspect ratio ('pasp')`](pixel_aspect_ratio.md) and [`MPEG-4 elementary stream descriptor atom ('esds')`](mpeg-4_elementary_stream_descriptor_atom.md).

MPEG-4 video conforms to ISO/IEC documents 14496-1/2000(E) and 14496-2:1999/Amd.1:2000(E).

#### Motion Jpeg

Motion-JPEG (M-JPEG) is a variant of the ISO JPEG specification for use with digital video streams. Instead of compressing an entire image into a single bitstream, Motion-JPEG compresses each video field separately, returning the resulting JPEG bitstreams consecutively in a single frame.

There are two flavors of Motion-JPEG currently in use. These two formats differ based on their use of markers. Motion-JPEG format A supports markers; Motion-JPEG format B does not. The following paragraphs describe how QuickTime stores Motion-JPEG sample data.

Each field of Motion-JPEG format A fully complies with the ISO JPEG specification, and therefore supports application markers. QuickTime uses the APP1 marker to store control information, as follows (all of the fields are 32-bit integers):

> **Note**: The last two fields have been added since the original Motion-JPEG specification, and so they may be missing from some Motion-JPEG A files. You should check the length of the APP1 marker before using the start of scan offset and start of data offset fields.

Motion-JPEG format B does not support markers. In place of the marker, therefore, QuickTime inserts a header at the beginning of the bitstream. Again, all of the fields are 32-bit integers.

> **Note**: The last two fields were “reserved, must be set to zero” in the original Motion-JPEG specification.

The Motion-JPEG format B header must be a multiple of 16 in size. When you add pad bytes to the header, set them to `0`.

Because Motion-JPEG format B does not support markers, the JPEG bitstream does not have `NULL` bytes (`0x00`) inserted after data bytes that are set to `0xFF`.

## See Also

- [Video sample description ('stsd')](video_sample_description.md)
  An atom that contains information that defines how to interpret video media data.
- [Video sample description extensions](video_sample_description_extensions.md)
  Extend video sample descriptions by appending other atoms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/video_sample_data)*