# IOHardwareCursorDescriptor

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef struct IOHardwareCursorDescriptor {
    ...
} IOHardwareCursorDescriptor;
```

## Topics

### Instance Properties
- [bitDepth](./iohardwarecursordescriptor/api-1505720-bitdepth.md)
  Number bits per pixel, or a QD/QT pixel type, for example kIO8IndexedPixelFormat, kIO32ARGBPixelFormat.
- [colorEncodings](./iohardwarecursordescriptor/api-1505587-colorencodings.md)
  An array pointer specifying the pixel values corresponding to the indices into the color table, for indexed pixel types.
- [flags](./iohardwarecursordescriptor/api-1505608-flags.md)
  None defined, set to zero.
- [height](./iohardwarecursordescriptor/api-1506025-height.md)
  Maximum size of the cursor.
- [majorVersion](./iohardwarecursordescriptor/api-1505436-majorversion.md)
  Set to kHardwareCursorDescriptorMajorVersion.
- [maskBitDepth](./iohardwarecursordescriptor/api-1505546-maskbitdepth.md)
  Unused.
- [minorVersion](./iohardwarecursordescriptor/api-1505743-minorversion.md)
  Set to kHardwareCursorDescriptorMinorVersion.
- [numColors](./iohardwarecursordescriptor/api-1505035-numcolors.md)
  Number of colors for indexed pixel types.
- [specialEncodings](./iohardwarecursordescriptor/api-1505679-specialencodings.md)
  Array of pixel values for each supported special encoding.
- [supportedSpecialEncodings](./iohardwarecursordescriptor/api-1506135-supportedspecialencodings.md)
  Mask of supported special pixel values, eg. kTransparentEncodedPixel, kInvertingEncodedPixel.
- [width](./iohardwarecursordescriptor/api-1505052-width.md)
  Maximum size of the cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohardwarecursordescriptor)*