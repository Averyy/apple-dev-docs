# IOHardwareCursorInfo

**Framework**: IOKit  
**Kind**: tag

A structure defining the converted data of a hardware cursor.

## Declaration

```c
struct IOHardwareCursorInfo {
   UInt16 majorVersion;
   UInt16 minorVersion;
   UInt32 cursorHeight;
   UInt32 cursorWidth;
   // nil or big enough for hardware's max colors
   IOColorEntry *colorMap;
   UInt8 *hardwareCursorData;
   UInt16 cursorHotSpotX;
   UInt16 cursorHotSpotY;
   UInt32 reserved[5];
};
```

#### Overview

This structure is used by IOFramebuffer to return the data of a hardware cursor by convertCursorImage() after conversion based on the IOHardwareCursorDescriptor passed to that routine.

## Topics

### Fields
- [majorVersion](../iohardwarecursorinfo/api-1505105-majorversion.md)
  Set to kHardwareCursorInfoMajorVersion.
- [minorVersion](../iohardwarecursorinfo/api-1505832-minorversion.md)
  Set to kHardwareCursorInfoMinorVersion.
- [cursorHeight](../iohardwarecursorinfo/api-1505775-cursorheight.md)
  The actual size of the cursor is returned.
- [cursorWidth](../iohardwarecursorinfo/api-1506034-cursorwidth.md)
  The actual size of the cursor is returned.
- [colorMap](../iohardwarecursorinfo/api-1506173-colormap.md)
  Pointer to array of IOColorEntry structures, with the number of elements set by the numColors field of the IOHardwareCursorDescriptor. Zero should be passed for direct pixel formats.
- [hardwareCursorData](../iohardwarecursorinfo/api-1505146-hardwarecursordata.md)
  Buffer to receive the converted cursor data.
- [cursorHotSpotX](../iohardwarecursorinfo/api-1505685-cursorhotspotx.md)
  Cursor's hotspot.
- [cursorHotSpotY](../iohardwarecursorinfo/api-1505474-cursorhotspoty.md)
  Cursor's hotspot.
- [reserved](../iohardwarecursorinfo/api-1505443-reserved.md)
  Reserved, set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iographicstypes_h_user-space/iohardwarecursorinfo)*