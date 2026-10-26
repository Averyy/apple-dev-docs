# IODisplayTimingRange

**Framework**: IOKit  
**Kind**: tag

A structure defining the limits and attributes of a display or framebuffer.

## Declaration

```c
struct IODisplayTimingRange {
   UInt32 __reservedA[2]; // Init to 0
   UInt32 version; // Init to 0
   UInt32 __reservedB[5]; // Init to 0
   UInt64 minPixelClock; // Min dot clock in Hz
   UInt64 maxPixelClock; // Max dot clock in Hz
   UInt32 maxPixelError; // Max dot clock error
   UInt32 supportedSyncFlags;
   UInt32 supportedSignalLevels;
   UInt32 supportedSignalConfigs;
   UInt32 minFrameRate; // Hz
   UInt32 maxFrameRate; // Hz
   UInt32 minLineRate; // Hz
   UInt32 maxLineRate; // Hz
   UInt32 maxHorizontalTotal; // Clocks - Maximum total (active + blanking)
   UInt32 maxVerticalTotal; // Clocks - Maximum total (active + blanking)
   UInt32 __reservedD[2]; // Init to 0
   UInt8 charSizeHorizontalActive;
   UInt8 charSizeHorizontalBlanking;
   UInt8 charSizeHorizontalSyncOffset;
   UInt8 charSizeHorizontalSyncPulse;
   UInt8 charSizeVerticalActive;
   UInt8 charSizeVerticalBlanking;
   UInt8 charSizeVerticalSyncOffset;
   UInt8 charSizeVerticalSyncPulse;
   UInt8 charSizeHorizontalBorderLeft;
   UInt8 charSizeHorizontalBorderRight;
   UInt8 charSizeVerticalBorderTop;
   UInt8 charSizeVerticalBorderBottom;
   UInt8 charSizeHorizontalTotal; // Character size for active + blanking
   UInt8 charSizeVerticalTotal; // Character size for active + blanking
   UInt16 __reservedE; // Reserved (Init to 0)
   UInt32 minHorizontalActiveClocks;
   UInt32 maxHorizontalActiveClocks;
   UInt32 minHorizontalBlankingClocks;
   UInt32 maxHorizontalBlankingClocks;
   UInt32 minHorizontalSyncOffsetClocks;
   UInt32 maxHorizontalSyncOffsetClocks;
   UInt32 minHorizontalPulseWidthClocks;
   UInt32 maxHorizontalPulseWidthClocks;
   UInt32 minVerticalActiveClocks;
   UInt32 maxVerticalActiveClocks;
   UInt32 minVerticalBlankingClocks;
   UInt32 maxVerticalBlankingClocks;
   UInt32 minVerticalSyncOffsetClocks;
   UInt32 maxVerticalSyncOffsetClocks;
   UInt32 minVerticalPulseWidthClocks;
   UInt32 maxVerticalPulseWidthClocks;
   UInt32 minHorizontalBorderLeft;
   UInt32 maxHorizontalBorderLeft;
   UInt32 minHorizontalBorderRight;
   UInt32 maxHorizontalBorderRight;
   UInt32 minVerticalBorderTop;
   UInt32 maxVerticalBorderTop;
   UInt32 minVerticalBorderBottom;
   UInt32 maxVerticalBorderBottom;
   UInt32 maxNumLinks; // number of links, if zero, assume link 1
   UInt32 minLink0PixelClock; // min pixel clock for link  (kHz)
   UInt32 maxLink0PixelClock; // max pixel clock for link  (kHz)
   UInt32 minLink1PixelClock; // min pixel clock for link 1 (kHz)
   UInt32 maxLink1PixelClock; // max pixel clock for link 1 (kHz)
   UInt32 __reservedF[3]; // Init to 0
};
```

#### Overview

This structure is used to define the limits for modes programmed as detailed timings by the OS. The VESA EDID is useful background information for many of these fields. A data property with this structure under the key kIOFBTimingRangeKey in a framebuffer will allow the OS to program detailed timings that fall within its range.

## Topics

### Fields
- [__reservedA](./iodisplaytimingrange/api-2587792-_reserveda.md)
  Set to zero.
- [__reservedB](./iodisplaytimingrange/api-2587793-_reservedb.md)
  Set to zero.
- [__reservedD](./iodisplaytimingrange/api-2587794-_reservedd.md)
  Set to zero.
- [__reservedE](./iodisplaytimingrange/api-2587795-_reservede.md)
  Set to zero.
- [__reservedF](./iodisplaytimingrange/api-2587796-_reservedf.md)
  Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iographicstypes_h_user-space/iodisplaytimingrange)*