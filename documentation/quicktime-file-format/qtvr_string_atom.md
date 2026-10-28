# QTVR string atom

**Framework**: QuickTime File Format  
**Kind**: class  
**Role**: Atom

An atom that contains a string for QuickTime VR.

> **Deprecated**: VR Media is deprecated in the QuickTime file format. The information that follows documents existing content containing VR Media and should not be used for new development.

## Overview

A string atom contains a string. The structure of a string atom is defined by the `QTVRStringAtom` data type.

```
typedef struct QTVRStringAtom {
    UInt16                              stringUsage;
    UInt16                              stringLength;
    unsigned char                       theString[4];
} QTVRStringAtom, *QTVRStringAtomPtr;
```

Each string atom may also have a sibling leaf atom, called the string encoding atom. The string encoding atom’s atom type is `kQTVRStringEncodingAtomType` (`'vrse'`). Its atom ID is the same as that of the corresponding string atom. The string encoding atom contains a single variable, `TextEncoding`, a `UInt32`, as defined in the header file `TextCommon.h`. The value of `TextEncoding` is handed, along with the string, to the routine `QTTextToNativeText` for conversion for display on the current machine. The routine `QTTextToNativeText` is found in the header file `Movies.h`.

> **Note**: The header file TextCommon.h contains constants and routines for generating and handling text encodings.

## Topics

### Data fields
- [stringUsage](./qtvr_string_atom/stringusage.md)
  The string usage.
- [stringLength](./qtvr_string_atom/stringlength.md)
  The length, in bytes, of the string.
- [theString](./qtvr_string_atom/thestring.md)
  The string.

## See Also

### Describing VR worlds
- [VR world atom container](./vr_world_atom_container.md)
  An atom that contains name for the entire scene, the default node ID, and default imaging properties, as well as a list of the nodes contained in the QTVR track.
- [VR world header atom](./vr_world_header_atom.md)
  An atom contains the name of the scene and the default node ID to be used when the file is first opened.
- [Imaging parent atom](./imaging_parent_atom.md)
  An atom that is the parent atom of one or more node-specific imaging atoms.
- [Panorama imaging atom](./panorama_imaging_atom.md)
  An atom describes the default imaging characteristics for all the panoramic nodes in a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/qtvr_string_atom)*