# VR world atom container

**Framework**: QuickTime File Format  
**Kind**: class

An atom that contains name for the entire scene, the default node ID, and default imaging properties, as well as a list of the nodes contained in the QTVR track.

#### Overview

The VR world atom container (VR world for short) includes such information as the name for the entire scene, the default node ID, and default imaging properties, as well as a list of the nodes contained in the QTVR track.

A VR world can also contain custom scene information. QuickTime VR ignores any atom types that it doesn’t recognize, but you can extract those atoms from the VR world using standard QuickTime atom functions.

The following shows the structure of the VR world atom container. The component atoms are defined and their structures are shown in the sections that follow.

```None
VR world
├── VR world header
├── Name string
├── Imaging parent
│   ├── Panorama imaging
│   └── Panorama imaging
├── Node parent
│   ├── Node ID
│   │   └── Node location
│   ├── Node ID
│   │   └── Node location
│   ├── ...
└── Cursor parent
    ├── Cursor
    ├── Color cursor
    ├── ...
```

## See Also

- [QTVR string atom](qtvr_string_atom.md)
  An atom that contains a string for QuickTime VR.
- [VR world header atom](vr_world_header_atom.md)
  An atom contains the name of the scene and the default node ID to be used when the file is first opened.
- [Imaging parent atom](imaging_parent_atom.md)
  An atom that is the parent atom of one or more node-specific imaging atoms.
- [Panorama imaging atom](panorama_imaging_atom.md)
  An atom describes the default imaging characteristics for all the panoramic nodes in a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/vr_world_atom_container)*