# IOPixelInformation

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef struct IOPixelInformation {
    ...
} IOPixelInformation;
```

## Topics

### Instance Properties
- [activeHeight](./iopixelinformation/api-1505946-activeheight.md)
  Number of visible pixel rows.
- [activeWidth](./iopixelinformation/api-1505617-activewidth.md)
  Number of pixels visible per row.
- [bitsPerComponent](./iopixelinformation/api-1506162-bitspercomponent.md)
  Number of bits per component in each pixel.
- [bitsPerPixel](./iopixelinformation/api-1505957-bitsperpixel.md)
  The number of bits per pixel, including unused bits and alpha.
- [bytesPerPlane](./iopixelinformation/api-1505598-bytesperplane.md)
  Not used.
- [bytesPerRow](./iopixelinformation/api-1505591-bytesperrow.md)
  The number of bytes per row.
- [componentCount](./iopixelinformation/api-1505140-componentcount.md)
  One for indexed pixels, three for direct pixel formats.
- [componentMasks](./iopixelinformation/api-1505522-componentmasks.md)
  Mask of the bits valid for each component of the pixel - in R, G, B order for direct pixels.
- [flags](./iopixelinformation/api-1505778-flags.md)
  None defined - set to zero.
- [pixelFormat](./iopixelinformation/api-1505071-pixelformat.md)
  String description of the pixel format - IO32BitDirectPixels, IO16BitDirectPixels etc.
- [pixelType](./iopixelinformation/api-1505700-pixeltype.md)
  One of kIOCLUTPixels (indexed pixels with changeable CLUT), kIORGBDirectPixels (direct pixels).
- [reserved](./iopixelinformation/api-1505942-reserved.md)
  Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iopixelinformation)*