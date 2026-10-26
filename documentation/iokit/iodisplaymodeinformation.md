# IODisplayModeInformation

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef struct IODisplayModeInformation {
    ...
} IODisplayModeInformation;
```

## Topics

### Instance Properties
- [flags](./iodisplaymodeinformation/api-1505482-flags.md)
  Flags for a display mode.
- [imageHeight](./iodisplaymodeinformation/api-1505901-imageheight.md)
  Physical height of active image if known, in millimeters, otherwise zero.
- [imageWidth](./iodisplaymodeinformation/api-1506007-imagewidth.md)
  Physical width of active image if known, in millimeters, otherwise zero.
- [maxDepthIndex](./iodisplaymodeinformation/api-1505323-maxdepthindex.md)
  Highest depth index available in this display mode.
- [nominalHeight](./iodisplaymodeinformation/api-1505238-nominalheight.md)
  Number of visible pixel rows.
- [nominalWidth](./iodisplaymodeinformation/api-1506031-nominalwidth.md)
  Number of pixels visible per row.
- [refreshRate](./iodisplaymodeinformation/api-1506012-refreshrate.md)
  Refresh rate in fixed point 16.16.
- [reserved](./iodisplaymodeinformation/api-1505975-reserved.md)
  Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iodisplaymodeinformation)*