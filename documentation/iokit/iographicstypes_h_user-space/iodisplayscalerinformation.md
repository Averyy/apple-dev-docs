# IODisplayScalerInformation

**Framework**: IOKit  
**Kind**: tag

A structure defining the scaling capabilities of a framebuffer.

## Declaration

```c
struct IODisplayScalerInformation {
   UInt32 __reservedA[1]; // Init to 0
   UInt32 version; // Init to 0
   UInt32 __reservedB[2]; // Init to 0
   IOOptionBits scalerFeatures;
   UInt32 maxHorizontalPixels;
   UInt32 maxVerticalPixels;
   UInt32 __reservedC[5]; // Init to 0
};
```

## Overview

This structure is used to define the limits for modes programmed as detailed timings by the OS. A data property with this structure under the key kIOFBScalerInfoKey in a framebuffer will allow the OS to program detailed timings that are scaled to a displays native resolution.

## Topics

### Fields
- [__reservedA](./iodisplayscalerinformation/api-2587787-_reserveda.md)
  Set to zero.
- [version](../iodisplayscalerinformation/api-1505407-version.md)
  Set to zero.
- [__reservedB](./iodisplayscalerinformation/api-2587788-_reservedb.md)
  Set to zero.
- [scalerFeatures](../iodisplayscalerinformation/api-1505798-scalerfeatures.md)
  Mask of scaling features. 
- [maxHorizontalPixels](../iodisplayscalerinformation/api-1505378-maxhorizontalpixels.md)
  Maximum number of horizontal source pixels (horizontalScaled).
- [maxVerticalPixels](../iodisplayscalerinformation/api-1505468-maxverticalpixels.md)
  Maximum number of vertical source pixels (verticalScaled).
- [__reservedC](./iodisplayscalerinformation/api-2587789-_reservedc.md)
  Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iographicstypes_h_user-space/iodisplayscalerinformation)*