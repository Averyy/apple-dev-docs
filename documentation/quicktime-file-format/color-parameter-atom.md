# Color parameter atom ('colr')

**Framework**: QuickTime File Format  
**Kind**: class

A required extension for uncompressed Y´CbCr data formats.

## Mentions

- [QuickTime File Format change log](revision_history.md)

#### Overview

This atom is a required extension for uncompressed Y´CbCr data formats. The `'colr'` extension is used to map the numerical values of pixels in the file to a common representation of color in which images can be correctly compared, combined, and displayed. The common representation is the CIE XYZ tristimulus values (defined in Publication CIE No. 15.2).

Use of a common representation also allows you to correctly map between Y´CbCr and RGB color spaces and to correctly compensate for gamma on different systems.

The `'colr'` extension supersedes the previously defined `'gama'` Image Description extension. Writers of QuickTime files should never write both into an Image Description, and readers of QuickTime files should ignore `'gama'` if `'colr'` is present.

The `'colr'` extension is designed to work for multiple imaging applications such as video and print. Each application, driven by its own set of historical and economic realities, has its own set of parameters needed to map from pixel values to CIE XYZ.

The CIE XYZ representation is mapped to various stored Y´CbCr formats using a common set of transfer functions and matrixes. The transfer function coefficients and matrix values are stored as indexes into a table of canonical references. This provides support for multiple video systems while limiting the scope of possible values to a set of recognized standards.

The `'colr'` atom contains four fields: a color parameter type and three indexes. The indexes are to a table of primaries, a table of transfer function coefficients, and a table of matrixes.

The following table shows the layout of this atom.

| Data field | Bytes |
| --- | --- |
| [`Size`](color_parameter_atom/size.md) | 4 |
| [`Type`](color_parameter_atom/type.md) = `'colr'` | 4 |
| [`Color parameter type`](color_parameter_atom/color_parameter_type.md) = `'nclc'` | 4 |
| [`Primaries index`](color_parameter_atom/primaries_index.md) = 1 | 2 |
| [`Transfer function index`](color_parameter_atom/transfer_function_index.md) = 1 | 2 |
| [`Matrix index`](color_parameter_atom/matrix_index.md) = 1 | 2 |

QuickTime uses the transfer function and matrix to convert RGB into Y´CbCr and back, as the following diagram shows:

![A diagram that shows the sequence of light measured by camera circuitry, expressed in RGB format, updated by transfer functions into ER’ EG’ EB’ format, then transformed by the matrix into Y´CbCr format for storage in QuickTime files. The diagram also shows the reverse process, where numerically coded data in a QuickTime file is transformed by the inverse matrix into ER’ EG’ EB’ format, then updated by the transfer functions into RGB format for display.](https://docs-assets.developer.apple.com/published/96b24af232eb1d8e25e3746956d07a9b/rgb-ycbcr-color-spaces%402x.png)

The Y´CbCr values stored in a file are normalized to a range of `[0,1]` for Y´ and `[-0.5, +0.5]` for Cb and Cr when performing these operations. The normalized values are then scaled to the proper bit depth for a particular Y´CbCr format before storage in the file as follows:

![An image showing three normalized values. The first says the symbol E, with a subscript Y’, has the range zero to 1. The second says the symbol E, with a subscript Cb, has the range minus zero point five to plus zero point five. The third says the symbol E, with a subscript Cr, has the range minus zero point five to plus zero point five.](https://docs-assets.developer.apple.com/published/e0dcbc301d9be91ce77835a37d0b9f19/color-parameter-atom-normalized%402x.png)

> **Note**: The symbols used for these values are not intended to correspond to the use of these same symbols in other standards. In particular, “E” should not be interpreted as voltage.

These normalized values can be mapped onto the stored integer values of a particular compression type’s Y´, Cb, and Cr components using two different schemes, which we will call Scheme A and Scheme B.

> ⚠️ **Warning**: Other, slightly different encoding/mapping schemes exist in the video industry, and data encoded using these schemes must be converted to one of the QuickTime schemes defined here.

Scheme A uses “Wide-Range” mapping (full scale) with unsigned Y´ and twos-complement Cb and Cr values as the following figure shows:

![An image that shows three equations for stored Y’CbCr values with a bit depth of n in scheme A. The first equation is Y’ is equal to the floor of a parenthetical formula fragment. The fragment contains zero point five plus, in parenthesis, two to the power of n minus 1, then multiplied by E with a subcript Y’. The second equation is Cb is equal to the floor of a parenthetical formula fragment. The fragment contains zero point five plus, in parenthesis, two to the power of n minus 2, then multiplied by E with a subcript Cb. The third equation is Cr is equal to the floor of a parenthetical formula fragment. The fragment contains zero point five plus, in parenthesis, two to the power of n minus 2, then multiplied by E with a subcript Cr.](https://docs-assets.developer.apple.com/published/3ba127f658c5c32bda99fa8ac3bafa45/color-parameter-atom-scheme-a%402x.png)

This maps normalized values to stored values so that, for example, 8-bit unsigned values for Y´ go from `0-255` as the normalized value goes from `0` to `1`, and 8-bit signed valued for Cb and Cr go from `-127` to `+127` as the normalized values go from `-0.5` to `+0.5`.

> ⚠️ **Warning**: In specifications such as ITU-R BT.601-4, JFIF 1.02, and SPIFF (Rec. ITU-T T.84), the symbols Cb and Cr are used to describe offset binary integers, not twos-complement signed integers shown here.

Scheme B uses “Video-Range” mapping with unsigned Y´ and offset binary Cb and Cr values.

> **Note**: Scheme B, shown in the following figure, comes from digital video industry specifications such as Rec. ITU-R BT. 601-4. All standard digital video tape formats (e.g., SMPTE D-1, SMPTE D-5) and all standard digital video links (e.g., SMPTE 259M-1997 serial digital video) use this scheme. Professional video storage and processing equipment from vendors such as Abekas, Accom, and SGI also use this scheme. MPEG-2, DVC and many other codecs specify source Y´CbCr pixels using this scheme.

![An image that shows three equations for stored Y’CbCr values with a bit depth of n in scheme B. The first equation is Y’ is equal to the floor of a parenthetical formula fragment. The fragment contains zero point five plus two to the power of n minus 8, then multiplied by, in parentheses, two hundred nineteen multiplied by E with a subcript Y’ plus sixteen. The second equation is Cb is equal to the floor of a parenthetical formula fragment. The fragment contains zero point five plus two to the power of n minus 8, then multiplied by, in parentheses, two hundred twenty-four multiplied by E with a subcript Cb plus one hundred twenty-eight. The third equation is Cr is equal to the floor of a parenthetical formula fragment. The fragment contains zero point five plus two to the power of n minus 8, then multiplied by, in parentheses, two hundred twenty-four multiplied by E with a subcript Cr plus one hundred twenty-eight.](https://docs-assets.developer.apple.com/published/936ea2964a17d0008a7315f84c1c762d/color-parameter-atom-scheme-b%402x.png)

This maps the normalized values to stored values so that, for example, 8-bit unsigned values for Y´ go from `16` to `235` as the normalized value goes from `0` to `1`, and 8-bit unsigned valued for Cb and Cr go from `16` to `240` as the normalized values go from `-0.5` to `+0.5`.

For 10-bit samples, Y´ has a range of `64` to `940` as the normalized value goes from `0` to `1`, and Cb and Cr have the range of `65–960` as the normalized values go from `–0.5` to `+0.5`.

Y´ is an unsigned integer. Cb and Cr are offset binary integers.

Certain Y´, Cb, and Cr component values v are reserved as synchronization signals and must not appear in a buffer. For n = 8 bits, these are values `0` and `255`. For n = 10 bits, these are values `0`, `1`, `2`, `3`, `1020`, `1021`, `1022`, and `1023`. The writer of a QuickTime image is responsible for omitting these values. The reader of a QuickTime image may assume that they are not present.

The remaining component values that fall outside the mapping for scheme B (`1` to `15` and `241` to `254` for n = 8 bits and `4` to `63` and `961` to `1019` for n = 10 bits) accommodate occasional filter undershoot and overshoot in image processing. In some applications, these values are used to carry other information (e.g., transparency). The writer of a QuickTime image may use these values and the reader of a QuickTime image must expect these values.

The following tables show the primary values, transfer functions, and matrixes indicated by the index entries in the `'colr'` atom.

The R, G, and B values in the following list are tristimulus values (such as candelas/meter^2), whose relationship to CIE XYZ values can be derived from the primaries and white point specified in the table, using the method described in SMPTE RP 177-1993. In this instance, the R, G, and B values are normalized to the range `[0,1]`.

- **Index 0**: Reserved
- **Index 1**: Recommendation ITU-R BT.709 white x = `0.3127` y = `0.3290` (CIE III. D65) red x = `0.640` y = `0.330` green x = `0.300` y = `0.600` blue x = `0.150` y = `0.060`
- **Index 2**: Primary values are unknown
- **Index 3-4**: Reserved
- **Index 5**: Recommendation ITU-R BT.601 (625-line) white x = `0.3127` y = `0.3290` (D65) red x = `0.64` y = `0.33` green x = `0.29` y = `0.60` blue x = `0.15` y = `0.06`
- **Index 6**: Recommendation ITU-R BT.601 (525-line) white x = `0.3127` y = `0.3290` (D65) red x = `0.630` y = `0.340` green x = `0.310` y = `0.595` blue x = `0.155` y = `0.070`
- **Index 7-8**: Reserved
- **Index 9**: Recommendation ITU-R BT.2020 white x = `0.3127` y = `0.3290` (D65) red x = `0.708` y = `0.292` green x = `0.170` y = `0.797` blue x = `0.131` y = `0.046`
- **Index 10**: Reserved
- **Index 11**: SMPTE RP 431-2 (2011) white x = `0.314` y = `0.351` red x = `0.680` y = `0.320` green x = `0.265` y = `0.690` blue x = `0.150` y = `0.060`, also known as DCI P3
- **Index 12**: SMPTE EG 432-1 (2010) white x = `0.3127` y = `0.3290` (D65) red x = `0.680` y = `0.320` green x = `0.265` y = `0.690` blue x = `0.150` y = `0.060`, also known as P3 D65 or Display P3
- **Index 13-65535**: Reserved

The transfer functions listed are used to transfer between RGB and Y’CbCr color spaces.

- **Index 0**: Reserved
- **Index 1**: Recommendation ITU-R BT.709-2, SMPTE 274M-1995, 296M-1997, 293M-1996, 170M-1994 ![An image that shows two formulas for transfer functions for index 1. The first formula is E’ with subscript W is equal to four point five zero zero for zero is less than or equal to W is less than zero point zero one eight. The second formula is E’ with subscript W is equal to one point zero nine nine W raised to the power zero point four five, minus zero point zero nine nine for zero point zero one eight is less than or equal to W is less than or equal to one.](https://docs-assets.developer.apple.com/published/f133af39f9fd97123c8a63a6c9748651/color-parameter-atom-transfer-1%402x.png)
- **Index 2**: Transfer function is unknown
- **Index 3-6**: Reserved
- **Index 7**: Recommendation SMPTE 240M-1995 and 274M-1995 ![An image that shows two formulas for transfer functions for index 7. The first formula is E’ with subscript W is equal to four W for zero is less than or equal to W is less than zero point zero two two eight. The second formula is E’ with subscript W is equal to one point one one one five W raised to the power zero point four five, minus zero point one one five for zero point zero two two eight is less than or equal to W is less than or equal to one.](https://docs-assets.developer.apple.com/published/29ae665d86356f6aa606200cb029b13e/color-parameter-atom-transfer-7%402x.png)
- **Index 8-16**: Reserved
- **Index 17**: SMPTE ST 428-1, for which W equal to 1 for peak white is ordinarily intended to correspond to a display luminance level of 48 candelas per square meter. ![An image that shows the formula for the transfer function for index 17. The formula is E’ with subscript W is equal to, in parentheses forty-eight W divided by fifty-two point 37, raised to the power of, in parentheses one divided by two point six, for zero is less than or equal to W is less than or equal to one.](https://docs-assets.developer.apple.com/published/6735e3072596ac3af2f90c6aa915aa4e/color-parameter-atom-transfer-17%402x.png)
- **Index 18-65535**: Reserved

The MPEG-2 sequence display extension `transfer_characteristics` defines a code 6 whose transfer function is identical to that in code 1. QuickTime writers should map 6 to 1 when converting from `transfer_characteristics` to `transferFunction`.

Recommendation ITU-R BT.470-4 specified an “assumed gamma value of the receiver for which the primary signals are pre-corrected” as 2.2 for NTSC and 2.8 for PAL systems. This information is both incomplete and obsolete. Modern 525- and 625-line digital and NTSC/PAL systems use the transfer function with code 1.

The matrix values are shown in the following list and in Matrix values for index code 1. These figures show a formula for obtaining the normalized value of Y´ in the range `[0,1]`. You can derive the formula for normalized values of Cb and Cr as follows:

If the equation for normalized Y´ has the form:

![An image that shows the normalized formula for Y’. The formula is E’ with subscript Y is equal to K’ with subscript G times E’ with subscript G, plus K’ with subscript B times E’ with subscript B, plus K’ with subscript R times E’ with subscript R.](https://docs-assets.developer.apple.com/published/d1baeba745f41dbab2a6ee2ce10a2617/color-parameter-atom-normalized-y%402x.png)

Then the formulas for normalized Cb and Cr are:

![An image that shows the normalized formulas for Cb and Cr. The first formula is E with subscript Cb is equal to, in parentheses zero point five over, in parenteses one minus K’ with subscript B, times, in parentheses E’ with subscript B minus E’ with subscript Y. The second formula is E with subscript Cr is equal to, in parentheses zero point five over, in parenteses one minus K’ with subscript R, times, in parentheses E’ with subscript R minus E’ with subscript Y.](https://docs-assets.developer.apple.com/published/e4fdd52756078bf46a84e37c092e780d/color-parameter-atom-normalized-cb-cr%402x.png)

- **Index 0**: Reserved
- **Index 1**: Recommendation ITU-R BT.709-2 (1125/60/2:1 only), SMPTE 274M-1995, 296M-1997 ![An image that shows the formula for matrix index 1. The formula is E’ with subscript Y is equal to zero point seven one five two E’ with subscript G, plus zero point zero seven two two E’ with subscript B, plus zero point two one two six E’ with subscript R.](https://docs-assets.developer.apple.com/published/f81413372e720a075548f15b3f41c88d/color-parameter-atom-table-matrix-1%402x.png)
- **Index 2**: Coefficient values are unknown
- **Index 3-5**: Reserved
- **Index 6**: Recommendation ITU-R BT.601-4 and BT.470-4 System B and G, SMPTE 170M-1994, 293M-1996 ![An image that shows the formula for matrix index 6. The formula is E’ with subscript Y is equal to zero point five eight seven E’ with subscript G, plus zero point one one four E’ with subscript B, plus zero point two nine nine E’ with subscript R.](https://docs-assets.developer.apple.com/published/cccb26e5ed778f1e9e7e842f1e514b1c/color-parameter-atom-table-matrix-6%402x.png)
- **Index 7**: SMPTE 240M-1995, 274M-1995 ![An image that shows the formula for matrix index 7. The formula is E’ with subscript Y is equal to zero point seven zero one E’ with subscript G, plus zero point zero eight seven E’ with subscript B, plus zero point two one two E’ with subscript R.](https://docs-assets.developer.apple.com/published/c230a90c2d70eca2bb70189615f96217/color-parameter-atom-table-matrix-7%402x.png)
- **Index 8**: Reserved
- **Index 9**: Recommendation ITU-R BT.2020 (non-constant luminance) ![An image that shows the formula for matrix index 9. The formula is E’ with subscript Y is equal to zero point six seven eight zero E’ with subscript G, plus zero point zero five nine three E’ with subscript B, plus zero point two six two seven E’ with subscript R.](https://docs-assets.developer.apple.com/published/4f9090fce5aa7bb056bbcf63b1128d18/color-parameter-atom-table-matrix-9%402x.png)
- **Index 10-65535**: Reserved

## Topics

### Data fields
- [Size](color_parameter_atom/size.md)
  An unsigned 32-bit integer holding the size of the color parameter atom.
- [Type](color_parameter_atom/type.md)
  An unsigned 32-bit field.
- [Color parameter type](color_parameter_atom/color_parameter_type.md)
  A 32-bit field containing a four-character code for the color parameter type.
- [Primaries index](color_parameter_atom/primaries_index.md)
  A 16-bit unsigned integer containing an index into a table specifying the CIE 1931 xy chromaticity coordinates of the white point and the red, green, and blue primaries.
- [Transfer function index](color_parameter_atom/transfer_function_index.md)
  A 16-bit unsigned integer containing an index into a table specifying the nonlinear transfer function coefficients used to translate between RGB color space values and Y´CbCr values.
- [Matrix index](color_parameter_atom/matrix_index.md)
  A 16-bit unsigned integer containing an index into a table specifying the transformation matrix coefficients used to translate between RGB color space values and Y´CbCr values.

## See Also

- [Pixel aspect ratio ('pasp')](pixel_aspect_ratio.md)
  An extension that specifies the height-to-width ratio of pixels found in the video sample.
- [MPEG-4 elementary stream descriptor atom ('esds')](mpeg-4_elementary_stream_descriptor_atom.md)
  A required extension to the video sample description for MPEG-4 video.
- [AVC decoder configuration atom ('avcC')](avc_decoder_configuration_atom.md)
  A required extension to the video sample description for H.264 video.
- [Clean aperture ('clap')](clean_aperture.md)
  An extension that defines the relationship between the pixels in a stored image and a canonical rectangular region of a video system from which it was captured or to which it will be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/color_parameter_atom)*