# bitsPerComponent

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Number of bits per component in each pixel.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
UInt32 bitsPerComponent;
```

## See Also

### Fields
- [bytesPerRow](./api-1505591-bytesperrow.md)
  The number of bytes per row.
- [bytesPerPlane](./api-1505598-bytesperplane.md)
  Not used.
- [bitsPerPixel](./api-1505957-bitsperpixel.md)
  The number of bits per pixel, including unused bits and alpha.
- [pixelType](./api-1505700-pixeltype.md)
  One of kIOCLUTPixels (indexed pixels with changeable CLUT), kIORGBDirectPixels (direct pixels).
- [componentCount](./api-1505140-componentcount.md)
  One for indexed pixels, three for direct pixel formats.
- [componentMasks](./api-1505522-componentmasks.md)
  Mask of the bits valid for each component of the pixel - in R, G, B order for direct pixels.
- [pixelFormat](./api-1505071-pixelformat.md)
  String description of the pixel format - IO32BitDirectPixels, IO16BitDirectPixels etc.
- [flags](./api-1505778-flags.md)
  None defined - set to zero.
- [activeWidth](./api-1505617-activewidth.md)
  Number of pixels visible per row.
- [activeHeight](./api-1505946-activeheight.md)
  Number of visible pixel rows.
- [reserved](./api-1505942-reserved.md)
  Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iopixelinformation/1506162-bitspercomponent)*