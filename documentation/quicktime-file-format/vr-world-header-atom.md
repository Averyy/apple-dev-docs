# VR world header atom

**Framework**: QuickTime File Format  
**Kind**: class

An atom contains the name of the scene and the default node ID to be used when the file is first opened.

#### Overview

The VR world header atom is a leaf atom. Its atom type is `kQTVRWorldHeaderAtomType` (`'vrsc'`). It contains the name of the scene and the default node ID to be used when the file is first opened as well as fields reserved for future use.

The structure of a VR world header atom is defined by the `QTVRWorldHeaderAtom` data type.

```c
typedef struct VRWorldHeaderAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    QTAtomID                            nameAtomID;
    UInt32                              defaultNodeID;
    UInt32                              vrWorldFlags;
    UInt32                              reserved1;
    UInt32                              reserved2;
} VRWorldHeaderAtom, *QTVRWorldHeaderAtomPtr;
QT
QT
```

## Topics

### Data fields
- [majorVersion](vr_world_header_atom/majorversion.md)
  The major version number of the file format.
- [minorVersion](vr_world_header_atom/minorversion.md)
  The minor version number of the file format.
- [nameAtomID](vr_world_header_atom/nameatomid.md)
  The ID of the string atom that contains the name of the scene.
- [defaultNodeID](vr_world_header_atom/defaultnodeid.md)
  The ID of the default node.
- [vrWorldFlags](vr_world_header_atom/vrworldflags.md)
  A set of flags for the VR world.
- [reserved1](vr_world_header_atom/reserved1.md)
  Reserved.
- [reserved2](vr_world_header_atom/reserved2.md)
  Reserved.

## See Also

- [QTVR string atom](qtvr_string_atom.md)
  An atom that contains a string for QuickTime VR.
- [VR world atom container](vr_world_atom_container.md)
  An atom that contains name for the entire scene, the default node ID, and default imaging properties, as well as a list of the nodes contained in the QTVR track.
- [Imaging parent atom](imaging_parent_atom.md)
  An atom that is the parent atom of one or more node-specific imaging atoms.
- [Panorama imaging atom](panorama_imaging_atom.md)
  An atom describes the default imaging characteristics for all the panoramic nodes in a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/vr_world_header_atom)*