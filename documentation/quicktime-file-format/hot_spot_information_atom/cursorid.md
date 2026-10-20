# cursorID

**Framework**: QuickTime File Format  
**Kind**: property  
**Role**: Data field

An array of three IDs for custom hot spot cursors.

#### Overview

Custom hot spot cursors override the default hot spot cursors provided by QuickTime VR. The first ID (`cursorID[0]`) specifies the cursor that is displayed when it is in the hot spot. The second ID (`cursorID[1]`) specifies the cursor that is displayed when it is in the hot spot and the mouse button is down. The third ID (`cursorID[2]`) specifies the cursor that is displayed when it is in the hot spot and the mouse button is released. To retain the default cursor for any of these operations, set the corresponding cursor ID to `0`. Custom cursors should be stored in the VR world atom container, as described in [`VR world atom container`](../vr_world_atom_container.md).

## See Also

### Data fields
- [majorVersion](./majorversion.md)
  The major version number of the file format.
- [minorVersion](./minorversion.md)
  The minor version number of the file format.
- [hotSpotType](./hotspottype.md)
  The hot spot type.
- [nameAtomID](./nameatomid.md)
  The ID of the string atom that contains the name of the hot spot.
- [commentAtomID](./commentatomid.md)
  The ID of the string atom that contains a comment for the hot spot.
- [bestPan](./bestpan.md)
  The best pan angle for viewing this hot spot.
- [bestTilt](./besttilt.md)
  The best tilt angle for viewing this hot spot.
- [bestFOV](./bestfov.md)
  The best field of view for viewing this hot spot.
- [bestViewCenter](./bestviewcenter.md)
  The best view center for viewing this hot spot.
- [hotSpotRect](./hotspotrect.md)
  The boundary box for this hot spot, specified as the number of pixels in full panoramic space.
- [flags](./flags.md)
  A set of hot spot flags.
- [reserved1](./reserved1.md)
  Reserved.
- [reserved2](./reserved2.md)
  Reserved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/hot_spot_information_atom/cursorid)*