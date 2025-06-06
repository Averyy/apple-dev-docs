# Link hot spot atom ('link')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that specifies information for a link hot spot.

**Availability**:
- Unknown ?+ - Deprecated

#### Overview

The link hot spot atom specifies information for hot spots of type `kQTVRHotSpotLinkType` (’`link'`). Its atom type is thus `'link'`. The link hot spot atom contains specific information about a link hot spot.

The structure of a link hot spot atom is defined by the `QTVRLinkHotSpotAtom` data type:

```c
typedef struct VRLinkHotSpotAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    UInt32                              toNodeID;
    UInt32                              fromValidFlags;
    Float32                             fromPan;
    Float32                             fromTilt;
    Float32                             fromFOV;
    FloatPoint                          fromViewCenter;
    UInt32                              toValidFlags;
    Float32                             toPan;
    Float32                             toTilt;
    Float32                             toFOV;
    FloatPoint                          toViewCenter;
    Float32                             distance;
    UInt32                              flags;
    UInt32                              reserved1;
    UInt32                              reserved2;
} VRLinkHotSpotAtom, *VRLinkHotSpotAtomPtr;
```

Certain fields in the link hot spot atom are not used by QuickTime VR. The `fromValidFlags` field is generally set to 0 and the other `from` fields are not used. However, these fields could be quite useful if you have created a transition movie from one node to another. The from angles can be used to swing the current view of the source node to align with the first frame of the transition movie. The `distance` field is intended for use with 3D applications, but is also not used by QuickTime VR.

## Topics

### Data fields
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
- [toValidFlags](link_hot_spot_atom/tovalidflags.md)
  A set of flags that indicate which destination node view settings are valid.
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
- [reserved2](link_hot_spot_atom/reserved2.md)
  Reserved.

## See Also

- [Node header atom ('ndhd')](node_header_atom.md)
  An atom that describes the type and ID of a node, as well as other information about the node.
- [Hot spot parent atom ('hspa')](hot_spot_parent_atom.md)
  An atom that is the parent for all hot spot atoms for the node.
- [Hot spot information atom ('hsin')](hot_spot_information_atom.md)
  An atom that contains general information about a hot spot.
- [Specific information atom](specific_information_atom.md)
  An atom that identified the hot spot type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/link_hot_spot_atom)*