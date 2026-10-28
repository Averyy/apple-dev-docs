# toValidFlags

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

A set of flags that indicate which destination node view settings are valid.

## Overview

Specifies which view settings are to be used when moving to a destination node from a hot spot. You can use these bit flags to specify a value for that field:

```c
enum {
    kQTVRValidPan                               = 1 << 0,
    kQTVRValidTilt                              = 1 << 1,
    kQTVRValidFOV                               = 1 << 2,
    kQTVRValidViewCenter                        = 1 << 3
};
```

**Constant Descriptions**

- **`kQTVRValidPan`**: The setting for using the destination pan angle.
- **`kQTVRValidTilt`**: The setting for using the destination tilt angle.
- **`kQTVRValidFOV`**: The setting for using the destination field of view.
- **`kQTVRValidViewCenter`**: The setting for using the destination view center.

## See Also

### Data fields
- [majorVersion](./majorversion.md)
  The major version number of the file format.
- [minorVersion](./minorversion.md)
  The minor version number of the file format.
- [toNodeID](./tonodeid.md)
  The ID of the destination node.
- [fromValidFlags](./fromvalidflags.md)
  A set of flags that indicate which source node view settings are valid.
- [fromPan](./frompan.md)
  The preferred from-pan angle at the source node.
- [fromTilt](./fromtilt.md)
  The preferred from-tilt angle at the source node.
- [fromFOV](./fromfov.md)
  The preferred from-field of view at the source node.
- [fromViewCenter](./fromviewcenter.md)
  The preferred from-view center at the source node.
- [toPan](./topan.md)
  The pan angle to use when displaying the destination node.
- [toTilt](./totilt.md)
  The tilt angle to use when displaying the destination node.
- [toFOV](./tofov.md)
  The field of view to use when displaying the destination node.
- [toViewCenter](./toviewcenter.md)
  The view center to use when displaying the destination node.
- [distance](./distance.md)
  The distance between the source node and the destination node.
- [flags](./flags.md)
  A set of link hot spot flags.
- [reserved1](./reserved1.md)
  Reserved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/link_hot_spot_atom/tovalidflags)*