# Node header atom ('ndhd')

**Framework**: QuickTime File Format  
**Kind**: class

An atom that describes the type and ID of a node, as well as other information about the node.

#### Overview

A node header atom is a leaf atom that describes the type and ID of a node, as well as other information about the node. Its atom type is `kQTVRNodeHeaderAtomType` (`'ndhd'`).

The structure of a node header atom is defined by the QTVRNodeHeaderAtom data type:

```c
typedef struct VRNodeHeaderAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    OSType                              nodeType;
    QTAtomID                            nodeID;
    QTAtomID                            nameAtomID;
    QTAtomID                            commentAtomID;
    UInt32                              reserved1;
    UInt32                              reserved2;
} VRNodeHeaderAtom, *VRNodeHeaderAtomPtr;
```

## Topics

### Data fields
- [majorVersion](node_header_atom/majorversion.md)
  The major version number of the file format.
- [minorVersion](node_header_atom/minorversion.md)
  The minor version number of the file format.
- [nodeType](node_header_atom/nodetype.md)
  The node type.
- [nodeID](node_header_atom/nodeid.md)
  The node ID.
- [nameAtomID](node_header_atom/nameatomid.md)
  The ID of the string atom that contains the name of the node.
- [commentAtomID](node_header_atom/commentatomid.md)
  The ID of the string atom that contains a comment for the node.
- [reserved1](node_header_atom/reserved1.md)
  Reserved.
- [reserved2](node_header_atom/reserved2.md)
  Reserved.

## See Also

- [Hot spot parent atom ('hspa')](hot_spot_parent_atom.md)
  An atom that is the parent for all hot spot atoms for the node.
- [Hot spot information atom ('hsin')](hot_spot_information_atom.md)
  An atom that contains general information about a hot spot.
- [Specific information atom](specific_information_atom.md)
  An atom that identified the hot spot type.
- [Link hot spot atom ('link')](link_hot_spot_atom.md)
  An atom that specifies information for a link hot spot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/node_header_atom)*