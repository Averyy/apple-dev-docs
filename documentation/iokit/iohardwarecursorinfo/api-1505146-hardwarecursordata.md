# hardwareCursorData

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Buffer to receive the converted cursor data.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
UInt8 *hardwareCursorData;
```

## See Also

### Fields
- [majorVersion](./api-1505105-majorversion.md)
  Set to kHardwareCursorInfoMajorVersion.
- [minorVersion](./api-1505832-minorversion.md)
  Set to kHardwareCursorInfoMinorVersion.
- [cursorHeight](./api-1505775-cursorheight.md)
  The actual size of the cursor is returned.
- [cursorWidth](./api-1506034-cursorwidth.md)
  The actual size of the cursor is returned.
- [colorMap](./api-1506173-colormap.md)
  Pointer to array of IOColorEntry structures, with the number of elements set by the numColors field of the IOHardwareCursorDescriptor. Zero should be passed for direct pixel formats.
- [cursorHotSpotX](./api-1505685-cursorhotspotx.md)
  Cursor's hotspot.
- [cursorHotSpotY](./api-1505474-cursorhotspoty.md)
  Cursor's hotspot.
- [reserved](./api-1505443-reserved.md)
  Reserved, set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohardwarecursorinfo/1505146-hardwarecursordata)*