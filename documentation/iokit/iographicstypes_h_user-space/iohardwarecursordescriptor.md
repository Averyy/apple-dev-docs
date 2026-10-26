# IOHardwareCursorDescriptor

**Framework**: IOKit  
**Kind**: tag

A structure defining the format of a hardware cursor.

## Declaration

```c
struct IOHardwareCursorDescriptor {
   UInt16 majorVersion;
   UInt16 minorVersion;
   UInt32 height;
   UInt32 width;
   UInt32 bitDepth; // bits per pixel, or a QD/QT pixel type
   UInt32 maskBitDepth; // unused
   UInt32 numColors; // number of colors in the colorMap. ie.
   UInt32 *colorEncodings;
   UInt32 flags;
   UInt32 supportedSpecialEncodings;
   UInt32 specialEncodings[16];
};
```

#### Overview

This structure is used by IOFramebuffer to define the format of a hardware cursor.

## Topics

### Fields
- [majorVersion](../iohardwarecursordescriptor/api-1505436-majorversion.md)
  Set to kHardwareCursorDescriptorMajorVersion.
- [minorVersion](../iohardwarecursordescriptor/api-1505743-minorversion.md)
  Set to kHardwareCursorDescriptorMinorVersion.
- [height](../iohardwarecursordescriptor/api-1506025-height.md)
  Maximum size of the cursor.
- [width](../iohardwarecursordescriptor/api-1505052-width.md)
  Maximum size of the cursor.
- [bitDepth](../iohardwarecursordescriptor/api-1505720-bitdepth.md)
  Number bits per pixel, or a QD/QT pixel type, for example kIO8IndexedPixelFormat, kIO32ARGBPixelFormat.
- [maskBitDepth](../iohardwarecursordescriptor/api-1505546-maskbitdepth.md)
  Unused.
- [numColors](../iohardwarecursordescriptor/api-1505035-numcolors.md)
  Number of colors for indexed pixel types.
- [colorEncodings](../iohardwarecursordescriptor/api-1505587-colorencodings.md)
  An array pointer specifying the pixel values corresponding to the indices into the color table, for indexed pixel types.
- [flags](../iohardwarecursordescriptor/api-1505608-flags.md)
  None defined, set to zero.
- [supportedSpecialEncodings](../iohardwarecursordescriptor/api-1506135-supportedspecialencodings.md)
  Mask of supported special pixel values, eg. kTransparentEncodedPixel, kInvertingEncodedPixel.
- [specialEncodings](../iohardwarecursordescriptor/api-1505679-specialencodings.md)
  Array of pixel values for each supported special encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iographicstypes_h_user-space/iohardwarecursordescriptor)*