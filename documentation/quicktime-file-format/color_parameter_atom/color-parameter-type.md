# Color parameter type

**Framework**: QuickTime File Format  
**Kind**: property

A 32-bit field containing a four-character code for the color parameter type.

#### Overview

The currently defined types are `'nclc'` for video, and `'prof'` for print. The color parameter type distinguishes between print and video mappings. If the color parameter type is `'prof'`, then this field is followed by an ICC profile. This is the color model used by Apple’s ColorSync. The contents of this type are not defined in this documentation. Contact Apple for more information on the `'prof'` type `'colr'` extension. If the color parameter type is `'nclc'` then this atom contains the following fields:

- [`Primaries index`](color_parameter_atom/primaries_index.md)
- [`Transfer function index`](color_parameter_atom/transfer_function_index.md)
- [`Matrix index`](color_parameter_atom/matrix_index.md)

## See Also

- [Size](color_parameter_atom/size.md)
  An unsigned 32-bit integer holding the size of the color parameter atom.
- [Type](color_parameter_atom/type.md)
  An unsigned 32-bit field.
- [Primaries index](color_parameter_atom/primaries_index.md)
  A 16-bit unsigned integer containing an index into a table specifying the CIE 1931 xy chromaticity coordinates of the white point and the red, green, and blue primaries.
- [Transfer function index](color_parameter_atom/transfer_function_index.md)
  A 16-bit unsigned integer containing an index into a table specifying the nonlinear transfer function coefficients used to translate between RGB color space values and Y´CbCr values.
- [Matrix index](color_parameter_atom/matrix_index.md)
  A 16-bit unsigned integer containing an index into a table specifying the transformation matrix coefficients used to translate between RGB color space values and Y´CbCr values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/color_parameter_atom/color_parameter_type)*