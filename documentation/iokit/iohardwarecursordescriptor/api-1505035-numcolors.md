# numColors

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Number of colors for indexed pixel types.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
UInt32 numColors;
```

## See Also

### Fields
- [majorVersion](./api-1505436-majorversion.md)
  Set to kHardwareCursorDescriptorMajorVersion.
- [minorVersion](./api-1505743-minorversion.md)
  Set to kHardwareCursorDescriptorMinorVersion.
- [height](./api-1506025-height.md)
  Maximum size of the cursor.
- [width](./api-1505052-width.md)
  Maximum size of the cursor.
- [bitDepth](./api-1505720-bitdepth.md)
  Number bits per pixel, or a QD/QT pixel type, for example kIO8IndexedPixelFormat, kIO32ARGBPixelFormat.
- [maskBitDepth](./api-1505546-maskbitdepth.md)
  Unused.
- [colorEncodings](./api-1505587-colorencodings.md)
  An array pointer specifying the pixel values corresponding to the indices into the color table, for indexed pixel types.
- [flags](./api-1505608-flags.md)
  None defined, set to zero.
- [supportedSpecialEncodings](./api-1506135-supportedspecialencodings.md)
  Mask of supported special pixel values, eg. kTransparentEncodedPixel, kInvertingEncodedPixel.
- [specialEncodings](./api-1505679-specialencodings.md)
  Array of pixel values for each supported special encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohardwarecursordescriptor/1505035-numcolors)*