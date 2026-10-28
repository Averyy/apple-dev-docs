# flags

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Flags for a display mode.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
UInt32 flags;
```

## Discussion

The possible flag values include:

kDisplayModeInterlacedFlag mode is interlaced.

kDisplayModeSimulscanFlag mode is available on multiple display connections.

kDisplayModeNotPresetFlag mode is not a factory preset for the display (geometry may need correction).

kDisplayModeStretchedFlag mode is stretched/distorted to match the display aspect ratio.

## See Also

### Fields
- [nominalWidth](./api-1506031-nominalwidth.md)
  Number of pixels visible per row.
- [nominalHeight](./api-1505238-nominalheight.md)
  Number of visible pixel rows.
- [refreshRate](./api-1506012-refreshrate.md)
  Refresh rate in fixed point 16.16.
- [maxDepthIndex](./api-1505323-maxdepthindex.md)
  Highest depth index available in this display mode.
- [imageWidth](./api-1506007-imagewidth.md)
  Physical width of active image if known, in millimeters, otherwise zero.
- [imageHeight](./api-1505901-imageheight.md)
  Physical height of active image if known, in millimeters, otherwise zero.
- [reserved](./api-1505975-reserved.md)
  Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iodisplaymodeinformation/1505482-flags)*