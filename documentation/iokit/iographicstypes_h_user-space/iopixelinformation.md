# IOPixelInformation

**Framework**: IOKit  
**Kind**: tag

A structure defining the format of a framebuffer.

## Declaration

```c
struct IOPixelInformation {
   UInt32 bytesPerRow;
   UInt32 bytesPerPlane;
   UInt32 bitsPerPixel;
   UInt32 pixelType;
   UInt32 componentCount;
   UInt32 bitsPerComponent;
   UInt32 componentMasks[ 8 * 2 ];
   IOPixelEncoding pixelFormat;
   UInt32 flags;
   UInt32 activeWidth;
   UInt32 activeHeight;
   UInt32 reserved[ 2 ];
};
```

#### Overview

This structure is used by IOFramebuffer to define the format of the pixels.

## Topics

### Fields
- [bytesPerRow](../iopixelinformation/api-1505591-bytesperrow.md)
  The number of bytes per row.
- [bytesPerPlane](../iopixelinformation/api-1505598-bytesperplane.md)
  Not used.
- [bitsPerPixel](../iopixelinformation/api-1505957-bitsperpixel.md)
  The number of bits per pixel, including unused bits and alpha.
- [pixelType](../iopixelinformation/api-1505700-pixeltype.md)
  One of kIOCLUTPixels (indexed pixels with changeable CLUT), kIORGBDirectPixels (direct pixels).
- [componentCount](../iopixelinformation/api-1505140-componentcount.md)
  One for indexed pixels, three for direct pixel formats.
- [bitsPerComponent](../iopixelinformation/api-1506162-bitspercomponent.md)
  Number of bits per component in each pixel.
- [componentMasks](../iopixelinformation/api-1505522-componentmasks.md)
  Mask of the bits valid for each component of the pixel - in R, G, B order for direct pixels.
- [pixelFormat](../iopixelinformation/api-1505071-pixelformat.md)
  String description of the pixel format - IO32BitDirectPixels, IO16BitDirectPixels etc.
- [flags](../iopixelinformation/api-1505778-flags.md)
  None defined - set to zero.
- [activeWidth](../iopixelinformation/api-1505617-activewidth.md)
  Number of pixels visible per row.
- [activeHeight](../iopixelinformation/api-1505946-activeheight.md)
  Number of visible pixel rows.
- [reserved](../iopixelinformation/api-1505942-reserved.md)
  Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iographicstypes_h_user-space/iopixelinformation)*