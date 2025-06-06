# toValidFlags

**Framework**: QuickTime File Format  
**Kind**: property

A set of flags that indicate which destination node view settings are valid.

#### Overview

Specifies which view settings are to be used when moving to a destination node from a hot spot. You can use these bit flags to specify a value for that field:

```c
enum {
    kQTVRValidPan                               = 1 << 0,
    kQTVRValidTilt                              = 1 << 1,
    kQTVRValidFOV                               = 1 << 2,
    kQTVRValidViewCenter                        = 1 << 3
};
```

## See Also

- [majorVersion](link_hot_spot_atom/majorversion.md)
  The major version number of the file format.
- [minorVersion](link_hot_spot_atom/minorversion.md)
  The minor version number of the file format.
- [toNodeID](link_hot_spot_atom/tonodeid.md)
  The ID of the destination node.
- [fromValidFlags](link_hot_spot_atom/fromvalidflags.md)
  A set of flags that indicate which source node view settings are valid.
- [fromPan](link_hot_spot_atom/frompan.md)
  The preferred from-pan angle at the source node.
- [fromTilt](link_hot_spot_atom/fromtilt.md)
  The preferred from-tilt angle at the source node.
- [fromFOV](link_hot_spot_atom/fromfov.md)
  The preferred from-field of view at the source node.
- [fromViewCenter](link_hot_spot_atom/fromviewcenter.md)
  The preferred from-view center at the source node.
- [toPan](link_hot_spot_atom/topan.md)
  The pan angle to use when displaying the destination node.
- [toTilt](link_hot_spot_atom/totilt.md)
  The tilt angle to use when displaying the destination node.
- [toFOV](link_hot_spot_atom/tofov.md)
  The field of view to use when displaying the destination node.
- [toViewCenter](link_hot_spot_atom/toviewcenter.md)
  The view center to use when displaying the destination node.
- [distance](link_hot_spot_atom/distance.md)
  The distance between the source node and the destination node.
- [flags](link_hot_spot_atom/flags.md)
  A set of link hot spot flags.
- [reserved1](link_hot_spot_atom/reserved1.md)
  Reserved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/link_hot_spot_atom/tovalidflags)*