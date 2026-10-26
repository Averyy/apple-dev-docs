# IOHardwareCursorInfo

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef struct IOHardwareCursorInfo {
    ...
} IOHardwareCursorInfo;
```

## Topics

### Instance Properties
- [colorMap](./iohardwarecursorinfo/api-1506173-colormap.md)
  Pointer to array of IOColorEntry structures, with the number of elements set by the numColors field of the IOHardwareCursorDescriptor. Zero should be passed for direct pixel formats.
- [cursorHeight](./iohardwarecursorinfo/api-1505775-cursorheight.md)
  The actual size of the cursor is returned.
- [cursorHotSpotX](./iohardwarecursorinfo/api-1505685-cursorhotspotx.md)
  Cursor's hotspot.
- [cursorHotSpotY](./iohardwarecursorinfo/api-1505474-cursorhotspoty.md)
  Cursor's hotspot.
- [cursorWidth](./iohardwarecursorinfo/api-1506034-cursorwidth.md)
  The actual size of the cursor is returned.
- [hardwareCursorData](./iohardwarecursorinfo/api-1505146-hardwarecursordata.md)
  Buffer to receive the converted cursor data.
- [majorVersion](./iohardwarecursorinfo/api-1505105-majorversion.md)
  Set to kHardwareCursorInfoMajorVersion.
- [minorVersion](./iohardwarecursorinfo/api-1505832-minorversion.md)
  Set to kHardwareCursorInfoMinorVersion.
- [reserved](./iohardwarecursorinfo/api-1505443-reserved.md)
  Reserved, set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohardwarecursorinfo)*