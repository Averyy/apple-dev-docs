# cursorID

**Framework**: QuickTime File Format  
**Kind**: property

An array of three IDs for custom hot spot cursors.

#### Overview

Custom hot spot cursors override the default hot spot cursors provided by QuickTime VR. The first ID (`cursorID[0]`) specifies the cursor that is displayed when it is in the hot spot. The second ID (`cursorID[1]`) specifies the cursor that is displayed when it is in the hot spot and the mouse button is down. The third ID (`cursorID[2]`) specifies the cursor that is displayed when it is in the hot spot and the mouse button is released. To retain the default cursor for any of these operations, set the corresponding cursor ID to `0`. Custom cursors should be stored in the VR world atom container, as described in [`VR world atom container`](vr_world_atom_container.md).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/hot_spot_information_atom/cursorid)*