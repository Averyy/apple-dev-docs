# Hot spot information atom ('hsin')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that contains general information about a hot spot.

## Mentions

- [Custom cursor atom](custom_cursor_atom.md)

#### Overview

The hot spot information atom contains general information about a hot spot. Its atom type is `kQTVRHotSpotInfoAtomType` (`'hsin'`). Every hot spot atom should have a hot spot information atom as a child.

The structure of a hot spot information atom is defined by the `QTVRHotSpotInfoAtom` data type:

```c
typedef struct VRHotSpotInfoAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    OSType                              hotSpotType;
    QTAtomID                            nameAtomID;
    QTAtomID                            commentAtomID;
    SInt32                              cursorID[3];
    Float32                             bestPan;
    Float32                             bestTilt;
    Float32                             bestFOV;
    FloatPoint                          bestViewCenter;
    Rect                                hotSpotRect;
    UInt32                              flags;
    UInt32                              reserved1;
    UInt32                              reserved2;
} VRHotSpotInfoAtom, *QTVRHotSpotInfoAtomPtr;
```

> **Note**: In QuickTime VR movie files, all angular values are stored as 32-bit floating-point values that specify degrees. In addition, all floating-point values conform to the IEEE Standard 754 for binary floating-point arithmetic, in big-endian format.

## Topics

### Data fields
- [majorVersion](hot_spot_information_atom/majorversion.md)
  The major version number of the file format.
- [minorVersion](hot_spot_information_atom/minorversion.md)
  The minor version number of the file format.
- [hotSpotType](hot_spot_information_atom/hotspottype.md)
  The hot spot type.
- [nameAtomID](hot_spot_information_atom/nameatomid.md)
  The ID of the string atom that contains the name of the hot spot.
- [commentAtomID](hot_spot_information_atom/commentatomid.md)
  The ID of the string atom that contains a comment for the hot spot.
- [cursorID](hot_spot_information_atom/cursorid.md)
  An array of three IDs for custom hot spot cursors.
- [bestPan](hot_spot_information_atom/bestpan.md)
  The best pan angle for viewing this hot spot.
- [bestTilt](hot_spot_information_atom/besttilt.md)
  The best tilt angle for viewing this hot spot.
- [bestFOV](hot_spot_information_atom/bestfov.md)
  The best field of view for viewing this hot spot.
- [bestViewCenter](hot_spot_information_atom/bestviewcenter.md)
  The best view center for viewing this hot spot.
- [hotSpotRect](hot_spot_information_atom/hotspotrect.md)
  The boundary box for this hot spot, specified as the number of pixels in full panoramic space.
- [flags](hot_spot_information_atom/flags.md)
  A set of hot spot flags.
- [reserved1](hot_spot_information_atom/reserved1.md)
  Reserved.
- [reserved2](hot_spot_information_atom/reserved2.md)
  Reserved.

## See Also

- [Node header atom ('ndhd')](node_header_atom.md)
  An atom that describes the type and ID of a node, as well as other information about the node.
- [Hot spot parent atom ('hspa')](hot_spot_parent_atom.md)
  An atom that is the parent for all hot spot atoms for the node.
- [Specific information atom](specific_information_atom.md)
  An atom that identified the hot spot type.
- [Link hot spot atom ('link')](link_hot_spot_atom.md)
  An atom that specifies information for a link hot spot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/hot_spot_information_atom)*