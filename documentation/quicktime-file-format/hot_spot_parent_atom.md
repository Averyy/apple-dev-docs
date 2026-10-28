# Hot spot parent atom ('hspa')

**Framework**: QuickTime File Format  
**Kind**: class  
**Role**: Atom

An atom that is the parent for all hot spot atoms for the node.

> **Deprecated**: VR Media is deprecated in the QuickTime file format. The information that follows documents existing content containing VR Media and should not be used for new development.

## Overview

The hot spot parent atom is the parent for all hot spot atoms for the node. The atom type of the hot spot parent atom is `kQTVRHotSpotParentAtomType` (`'hspa'`) and the atom type of the each hot spot atom is `kQTVRHotSpotAtomType` (`'hots'`). The atom ID of each hot spot atom is the hot spot ID for the corresponding hot spot. The hot spot ID is determined by its color index value as it is stored in the hot spot image track.

The hot spot track is an 8-bit video track that contains color information that indicates hot spots. For more information, refer to Programming With QuickTime VR.

Each hot spot atom is the parent of a number of atoms that contain information about each hot spot.

## See Also

### Specifying node information
- [Node header atom ('ndhd')](./node_header_atom.md)
  An atom that describes the type and ID of a node, as well as other information about the node.
- [Hot spot information atom ('hsin')](./hot_spot_information_atom.md)
  An atom that contains general information about a hot spot.
- [Specific information atom](./specific_information_atom.md)
  An atom that identified the hot spot type.
- [Link hot spot atom ('link')](./link_hot_spot_atom.md)
  An atom that specifies information for a link hot spot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/hot_spot_parent_atom)*